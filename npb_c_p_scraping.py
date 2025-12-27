import requests
from bs4 import BeautifulSoup
import time
import csv
from pathlib import Path

def scrape_baseball_stats(url):
    """
    NPBの統計ページをスクレイピング
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        
        if response.status_code != 200:
            print(f"❌ 失敗: {url} (ステータスコード: {response.status_code})")
            return None
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # テーブルを抽出
        table = soup.find('table', {'class': 'mdl-data-table'})
        if not table:
            table = soup.find('table')
        
        if not table:
            print(f"⚠️ テーブルなし: {url}")
            return None
        
        # テーブルデータを解析
        rows = table.find_all('tr')
        data = []
        
        for row in rows:
            cols = row.find_all(['th', 'td'])
            row_data = [col.get_text(strip=True) for col in cols]
            if row_data:
                data.append(row_data)
        
        print(f"✓ 成功: {url}")
        print(f"  → {len(rows)}行のデータを取得")
        
        return {
            'url': url,
            'data': data,
            'row_count': len(rows)
        }
    
    except Exception as e:
        print(f"❌ エラー: {url}")
        print(f"  → {str(e)}")
        return None

def read_urls_from_file(filename='baseball_urls.txt'):
    """
    baseball_urls.txtからURLを読み込む
    """
    urls = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and line.startswith('https://'):
                    urls.append(line)
        return urls
    except FileNotFoundError:
        print(f"❌ ファイルが見つかりません: {filename}")
        return []

def save_to_csv(results, filename='scraped_stats.csv'):
    """
    スクレイピング結果をCSVに保存
    """
    # 最初のデータセットを確認
    if not results or not results[0]['data']:
        print("保存するデータがありません")
        return
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            for result in results:
                if result['data']:
                    # URLをヘッダーとして追加
                    writer.writerow([f"URL: {result['url']}"])
                    
                    # テーブルデータを書き込み
                    for row in result['data']:
                        writer.writerow(row)
                    
                    writer.writerow([])  # 空行を追加（区切り）
        
        print(f"\n✓ CSVに保存: {filename}")
    except Exception as e:
        print(f"❌ CSV保存エラー: {str(e)}")

def main():
    print("=" * 60)
    print("NPB統計ページスクレイピング開始")
    print("=" * 60)
    
    # URLを読み込む
    urls = read_urls_from_file('baseball_urls.txt')
    
    if not urls:
        print("URLが見つかりません")
        return
    
    print(f"読み込みURL数: {len(urls)}\n")
    
    results = []
    
    # スクレイピング実行
    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] スクレイピング中...", end=" ")
        result = scrape_baseball_stats(url)
        
        if result:
            results.append(result)
        
        # サーバーへの負荷軽減（1秒待機）
        time.sleep(1)
    
    # 結果をCSVに保存
    print("\n" + "=" * 60)
    save_to_csv(results, 'save_csv/scraped_baseball_stats.csv')
    
    print("=" * 60)
    print(f"スクレイピング完了: {len(results)}/{len(urls)}件成功")
    print("=" * 60)

if __name__ == "__main__":
    main()
