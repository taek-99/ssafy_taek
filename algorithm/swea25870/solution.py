from typing import List

computer_list = {}


def init(N: int, mShareFileCnt: List[int], mFileID: List[List[int]], mFileSize: List[List[int]]) -> None:
    global computer_list

    computer_list = {x: {} for x in range(1, N+1)}
    
    pass


def makeNet(K: int, mComA: List[int], mComB: List[int], mDis: List[int]) -> None:
    global computer_list

    for i in range(1, K+1):
        ma = mComA[i]
        mb = mComB[i]
        md = mDis[i]

        computer_list[ma][mb] = md
        computer_list[mb][ma] = md



def addLink(mTime: int, mComA: int, mComB: int, mDis: int) -> None:
    global computer_list

    computer_list[mComA][mComB] = mDis
    pass


def addShareFile(mTime: int, mComA: int, mFileID: int, mSize: int) -> None:
    pass


def downloadFile(mTime: int, mComA: int, mFileID: int) -> int:
    return 0


def getFileSize(mTime: int, mComA: int, mFileID: int) -> int:
    return 0