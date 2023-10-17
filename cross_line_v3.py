# Created by Katsutoshi Machida Oct. 2023.

import vs


def execute():

    OBJECTS = []
    POLYGONS = []

    # 現在の属性の設定を記憶する
    vs.PushAttrs()

    # アクティブなレイヤのハンドルを取得しactlayerに代入する
    actlayer = vs.ActLayer()

    def collect(handle):
        OBJECTS.append(handle)

    vs.ForEachObject(collect, '((VSEL=TRUE))')

    for obj in OBJECTS:
        # オブジェクトが四角形または頂点数が4つの多角形でなければ選択を解除する
        if not(vs.GetTypeN(obj) == 3 or (vs.GetTypeN(obj) == 5 and vs.GetVertNum(obj) == 4)):
            vs.SetDSelect(obj)

        else:
            # 四角形または頂点数が4つの多角形を多角形に変換
            poly = vs.ConvertToPolygon(obj, 8)
            if poly != None:
                # 複製されたオブジェクトを複製元のオブジェクトと同じレイヤに移動
                vs.SetParent(poly, vs.GetLayer(obj))
                POLYGONS.append(poly)

    # 全てのオブジェクトの選択を解除
    vs.ForEachObject(vs.SetDSelect, '((SEL=TRUE))')

    # 多角形に変換したオブジェクトだけを選択
    for poly in POLYGONS:
        vs.SetSelect(poly)
        # 選択しているポリゴンと同じレイヤをアクティブにする
        vs.Layer(vs.GetLName(vs.GetLayer(poly)))
        # 頂点インデックス1と3、2と4を結ぶ線オブジェクトを作成し、グループ化
        vs.BeginGroup()        
        for i in [1, 3, 2, 4]:
            p = vs.GetPolyPt(poly, i)

            if i == 1 or i == 2:
                vs.MoveTo(p)
            else:
                vs.LineTo(p)

        vs.EndGroup()
        # 複製された多角形オブジェクトを削除
        vs.DelObject(poly)

    # 記憶されている属性を現在の設定にする
    vs.PopAttrs()

    # レイヤの設定をコマンド実行前と同じレイヤに設定する
    vs.Layer(vs.GetLName(actlayer))

if __name__ == "__main__":
    execute()