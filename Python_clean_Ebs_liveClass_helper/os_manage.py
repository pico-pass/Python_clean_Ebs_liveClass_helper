import winsound as sd

def beepsound(count = 1):
    """비프음을 냅니다.
        """
    for i in range(0, count):
        fr = 1000
        du = 400
        sd.Beep(fr, du)

def read_FILE():
    """ID.txt.파일을 읽고 3줄까지의 내용을 list형식으로 리턴합니다.

        """
    try:
        line = []
        f = open("ID.txt", 'r', encoding='UTF8')
        for i in range(0,3):
            line.append(f.readline().strip())
            if not line: break
        f.close()
        return line
    except FileNotFoundError:
        print("ID.txt를 읽는중 에러 발생")
        return 0

read_FILE()