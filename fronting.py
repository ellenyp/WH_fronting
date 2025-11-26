#!/usr/bin/env python3
#coding:utf-8

from WH_fronting.main import askLoki

def main():
    return None

if __name__ == "__main__":
    inputSTR = "蘇東坡看過那份檔案以後就離開了"
    inputSTR = "李白在阿拉伯遇到王維"
    refDICT = {"fronted": []}
    result = askLoki(inputSTR, refDICT=refDICT)
    print(result)