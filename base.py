# OUTPUTFILE    解の生成とログファイル名を表す変数
# ZABUTON       解の折り返し上に座布団を敷いているかどうかのフラグ

# case 1
# OUTPUTFILE = 'result.txt'
# ZABUTON = False
# DODAI = [
#     "  XXXX",
#     "GRXXXX",
#     "GGRXXX",
#     "RRBXXX"]

# case 2
# OUTPUTFILE = 'result2.txt'
# ZABUTON = False
# DODAI = [
#     "  XXXX",
#     "GRXXXX",
#     "GGRXXX",
#     "RRGXXX"]

# case 3
# OUTPUTFILE = 'result_zabuton.txt'
# ZABUTON = True
# DODAI = [
#     "YYYXXX",
#     "GRXXXX",
#     "GGRXXX",
#     "RRBXXX"]

# case 4
OUTPUTFILE = 'result_zabuton2.txt'
ZABUTON = True
DODAI = [
    "YYYXXX",
    "GRXXXX",
    "GGRXXX",
    "RRGXXX"]

# ぷよの色を表す変数、 enum class 使ってもいいです
NULL = 0
RED = 1
GREEN = 2
BLUE = 3
YELLOW = 4

MAXRETU = 6  # 今回探索する幅数と行数
MAXDAN = 4

RENSA = 5  # 全探索領域を使い切ると最大5連鎖になるはず(座布団有りの場合の+1連鎖分は考慮しなくてよい)


t = {"R": RED, "B": BLUE, "G": GREEN, "Y": YELLOW}  # 文字列から色を表す変数への辞書


def make_adjacent(i, j):
    """隣接するぷよのインデックスを返す"""
    if i != 0:
        yield (i-1, j)
    if j != 0:
        yield (i, j-1)
    if j != MAXRETU-1:
        yield (i, j+1)
    if i != MAXDAN-1:
        yield (i+1, j)


def make_children(i, j):
    """
    隣接するぷよのうち、インデックスが辞書順で若くないもののそれを返す
    探索の仕組み上、枝刈りのための連結数計算にはこれらのみを考慮すればよいです
    """
    if i != 0:
        yield (i-1, j)
    if j != 0:
        yield (i, j-1)


def show(ans: dict):
    """ログファイルへの解の表示用のフォーマット関数"""
    f = [["0"]*MAXRETU for j in range(MAXDAN)]
    for (i, j) in ans:
        f[i][j] = str(ans[i, j])
    return ','.join(map(''.join, f))
