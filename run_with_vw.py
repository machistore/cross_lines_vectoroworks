# Created by K.Machida Mar. 2023.
# Edited by K.Machida Oct. 2023

import vs
from cross_lines import CreateDiagonalsCommand  # cross_lines.py ファイルから CreateDiagonalsCommand クラスをインポート

def main():
    # CreateDiagonalsCommand クラスのインスタンスを作成
    command = CreateDiagonalsCommand()
    
    # execute() メソッドを呼び出す
    command.execute()

if __name__ == "__main__":
    main()  # スクリプトを実行
