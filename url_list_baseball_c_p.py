# 2015年から2025年までの野球統計ページのURLリスト生成

# 打者（Catcher: tmb_c.html）のURLリスト
batting_urls = []
for year in range(2015, 2026):
    url = f"https://npb.jp/bis/{year}/stats/tmb_c.html"
    batting_urls.append(url)

# 投手（Pitcher: tmb_p.html）のURLリスト
pitching_urls = []
for year in range(2015, 2026):
    url = f"https://npb.jp/bis/{year}/stats/tmb_p.html"
    pitching_urls.append(url)

# 両方のURLリスト
all_urls = batting_urls + pitching_urls

# 打者のURLを出力
print("=== 打者（tmb_c.html）のURLリスト ===")
for url in batting_urls:
    print(url)

print("\n=== 投手（tmb_p.html）のURLリスト ===")
for url in pitching_urls:
    print(url)

print(f"\n=== 合計 ===")
print(f"打者URL数: {len(batting_urls)}")
print(f"投手URL数: {len(pitching_urls)}")
print(f"合計URL数: {len(all_urls)}")

# ファイルに保存
with open('baseball_urls.txt', 'w', encoding='utf-8') as f:
    f.write("=== 打者（tmb_c.html）のURLリスト ===\n")
    for url in batting_urls:
        f.write(url + "\n")
    
    f.write("\n=== 投手（tmb_p.html）のURLリスト ===\n")
    for url in pitching_urls:
        f.write(url + "\n")

print("\n✓ URLリストを 'baseball_urls.txt' に保存しました")
