"""
打印杨辉三角
ver:0.1
author:Frank.Xiang
"""

def main():
    num = int(input('Number of rows: '))
    L = [1]
    S = []
    for _ in range(num):
    	yield L
    	L = [1] + S + [1]
    	S = []
    	for i in range(len(L)-1):
    		S.append(L[i] + L[i+1])



if __name__ == '__main__':
    main()