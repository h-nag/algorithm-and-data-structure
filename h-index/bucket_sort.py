def calculate_h_index(citations: List[int]) -> int:
  """
  O(n)の計算量でh-indexを計算します。

  Args:
    citations: 論文の被引用数を格納したリスト (List[int])

  Returns:
    h-index (int)
  """
  n = len(citations)
  # 1. サイズ n+1 の「バケツ」を用意する
  buckets = [0] * (n + 1)

  # 2. 各論文を引用数に応じたバケツに入れる
  for c in citations:
    if c >= n:
      # 引用数がn以上の論文は、まとめてn番目のバケツに入れる
      buckets[n] += 1
    else:
      buckets[c] += 1

  # 3. 後ろから論文数を累積し、h-indexの条件を探す
  paper_count = 0
  for h in range(n, -1, -1): # n, n-1, ..., 0 の順でループ
    paper_count += buckets[h]
    # 論文の累計本数 (paper_count) が 引用回数 (h) 以上になったら、それがh-index
    if paper_count >= h:
      return h

  return 0

# 実行例
if __name__ == "__main__":
  paper_citations = [1, 0, 5, 4, 8, 0, 2]
  h_index = calculate_h_index(paper_citations)

  print(f"与えられたリスト: {paper_citations}")
  print(f"h-index: {h_index}")