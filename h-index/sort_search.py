"""
ソート後、それぞれの値を降順に比較していく。その際、前回と同様にindexをカウントし、
この場合h-index）そのindexがcitationsの値より同値または大きくなった場合にreturnする
入力：各論文の引用数（リスト）
"""
def hIndex(citations: List[int]) -> int:
    # 引用数のソート（昇順）
    citations = sorted(citations)
    
    # ソートした引用数のリストを後ろ（降順）にh_indexをカウント
    h_index = 0
    for i in range(len(citations)-1, -1, -1):
      # 引用数がh-indexより大きければh-indexをカウントアップ
      if citations[i] > h_index:
        h_index += 1

    return h_index # 引用数がカウントされるh-indexと以下となれば修了