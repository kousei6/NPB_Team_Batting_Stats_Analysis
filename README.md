# NPB_Team_Batting_Stats_Analysis


このリポジトリは、NPB公式サイトのチーム打撃（セ・リーグ: tmb_c.html、パ・リーグ: tmb_p.html）のURLを生成し、2015年〜2025年の各年についてテーブルをスクレイピングしてCSVにまとめます。

## 概要
- **URL生成**: 年度ごとの打撃ページURL（セ・リーグ/パ・リーグ）を作成して出力・保存
- **スクレイピング**: URL一覧から各ページのテーブルを取得しCSVへ保存
- **出力**: 年・リーグごとのテーブルを縦に連結したCSV

## 前提・セットアップ
- **Python**: 3.8+ を推奨（Anacondaでも可）
- **必要パッケージ**: `requests`, `beautifulsoup4`

インストール例（必要な場合のみ）:

```bash
pip install requests beautifulsoup4
```

## 使い方
1. **URLリスト生成**（2015〜2025）
	 - スクリプト: [url_list_baseball_c_p.py](url_list_baseball_c_p.py)
	 - 実行:
		 ```bash
		 python url_list_baseball_c_p.py
		 ```
	 - 出力: ルートに `baseball_urls.txt` を作成（例: 打者URLと投手URLの一覧）
	 - 備考: もし [save_txt/baseball_urls.txt](save_txt/baseball_urls.txt) を使う場合は、`npb_c_p_scraping.py` の読み込みパスをその場所に合わせて変更してください。

2. **スクレイピング実行**
	 - スクリプト: [npb_c_p_scraping.py](npb_c_p_scraping.py)
	 - 実行:
		 ```bash
		 python npb_c_p_scraping.py
		 ```
	 - 出力: [save_csv/scraped_baseball_stats.csv](save_csv/scraped_baseball_stats.csv)

## 主要ファイル
- [url_list_baseball_c_p.py](url_list_baseball_c_p.py): 2015〜2025年の打撃ページURL（セ・リーグ/パ・リーグ）を生成し、`baseball_urls.txt` に保存
- [npb_c_p_scraping.py](npb_c_p_scraping.py): URL一覧からページを取得し、テーブルを抽出してCSVに保存（1秒の待機を挿入）
- [save_csv/scraped_baseball_stats.csv](save_csv/scraped_baseball_stats.csv): 取得したテーブルをURLごとに区切って連結したCSV
- 参考: [save_txt/baseball_urls.txt](save_txt/baseball_urls.txt): URL一覧の保存例（別フォルダ）

## 出力フォーマット
- 各URLごとに `URL: https://...` の行を先頭に付与
- 続けて対象ページの表（ヘッダー含む）をそのままCSV行として保存
- URL間は空行で区切り

## 注意事項・カスタマイズ
- **アクセス配慮**: サーバー負荷軽減のため 1 秒の待機を標準設定
- **User-Agent**: `requests` のヘッダで簡易設定（必要に応じて編集可）
- **年範囲変更**: [url_list_baseball_c_p.py](url_list_baseball_c_p.py) の `range(2015, 2026)` を変更
- **読み込み元の変更**: [npb_c_p_scraping.py](npb_c_p_scraping.py) の `read_urls_from_file('baseball_urls.txt')` を目的のパスに変更

## 実行例（Windows PowerShell）
```powershell
python url_list_baseball_c_p.py
python npb_c_p_scraping.py
```

## 補足
- 公式サイトの構造変更により、テーブルのクラス名や構造が変わる場合があります。その際は `table = soup.find('table', {'class': 'mdl-data-table'})` 部分のロジックを調整してください。
