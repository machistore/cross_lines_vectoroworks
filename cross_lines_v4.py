import vs

# 対角線を作成するコマンドクラス
class CreateDiagonalsCommand:
    def __init__(self):
        self.objects = []  # オブジェクトのハンドルを格納するリスト
        self.polygons = []  # 2D四角形または4つの頂点を持つ2D多角形のハンドルを格納するリスト

    def collect_objects(self, handle):
        # 選択されたオブジェクトのハンドルを収集する
        self.objects.append(handle)

    def convert_to_polygons(self):
        # 選択されたオブジェクトを2D多角形に変換
        for obj in self.objects:
            # オブジェクトが2D四角形または4つの頂点を持つ2D多角形であるか確認
            if vs.GetTypeN(obj) == 3 or (vs.GetTypeN(obj) == 5 and vs.GetVertNum(obj) == 4):
                # オブジェクトを2D多角形に変換し、複製されたオブジェクトをリストに追加
                poly = vs.ConvertToPolygon(obj, 8)
                if poly:
                    vs.SetParent(poly, vs.GetLayer(obj))
                    self.polygons.append(poly)

    def create_diagonals(self):
        # 2D多角形オブジェクトに対角線を描く
        for poly in self.polygons:
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

    def execute(self):
        vs.PushAttrs()  # 現在の属性の設定を記憶
        actlayer = vs.ActLayer() # アクティブなレイヤのハンドルを取得しactlayerに代入する
        vs.ForEachObject(self.collect_objects, '((VSEL=TRUE))')  # 選択されたオブジェクトのハンドルを収集
        self.convert_to_polygons()  # 2D四角形または4つの頂点を持つ2D多角形に変換
        vs.ForEachObject(vs.SetDSelect, '((SEL=TRUE))')  # 全てのオブジェクトの選択を解除
        self.create_diagonals()  # 対角線を作成
        vs.PopAttrs()  # 記憶されている属性を現在の設定に戻す
        vs.Layer(vs.GetLName(actlayer)) # レイヤの設定をコマンド実行前と同じレイヤに設定する


if __name__ == "__main__":
    script = CreateDiagonalsCommand()
    script.execute()  # スクリプトを実行
