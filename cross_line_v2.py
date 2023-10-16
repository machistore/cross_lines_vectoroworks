# Created by Katsutoshi Machida Oct. 2023.

import vs

# 選択したオブジェクトのハンドルを"selected_object"に代入
selected_object = vs.FSActLayer()

# 選択したオブジェクトの選択を外す(全ての選択を外す)
# (本コマンド終了後にこのコマンドで作成したオブジェクトだけを選択状態にしたいため)
vs.DSelectAll()

def cross_line_rect(selected_object):

    # selected_objectを多角形オブジェクトに変換し(解像度は仮に8とし)、"polygon_object"に代入
    polygon_object = vs.ConvertToPolygon(selected_object, 8)

    #ここから先のオブジェクトをグループにしたい
    vs.BeginGroup()

    p1, vertexType, arcRadius = vs.GetPolylineVertex(polygon_object, 1)
    vs.MoveTo(p1)
    
    p1, vertexType, arcRadius = vs.GetPolylineVertex(polygon_object, 3)
    vs.LineTo(p1)
    
    p1, vertexType, arcRadius = vs.GetPolylineVertex(polygon_object, 2)
    vs.MoveTo(p1)
    
    p1, vertexType, arcRadius = vs.GetPolylineVertex(polygon_object, 4)
    vs.LineTo(p1)

    #ここまでのオブジェクトをグループにする
    vs.EndGroup()

    # 多角形オブジェクトに変換したときに複製された多角形オブジェクトを消去する
    vs.DelObject(polygon_object)


def cross_line_poly(selected_object):
      
    vs.BeginGroup()
        
    p1, vertexType, arcRadius = vs.GetPolylineVertex(selected_object, 1)
    vs.MoveTo(p1)
    
    p1, vertexType, arcRadius = vs.GetPolylineVertex(selected_object, 3)
    vs.LineTo(p1)
    
    p1, vertexType, arcRadius = vs.GetPolylineVertex(selected_object, 2)
    vs.MoveTo(p1)
    
    p1, vertexType, arcRadius = vs.GetPolylineVertex(selected_object, 4)
    vs.LineTo(p1)

    #ここまでのオブジェクトをグループにする
    vs.EndGroup()


for i in range(vs.NumSObj(selected_object)):
    # もし選択しているオブジェクト(selected_object)が[四角形]オブジェクトだったら
    if vs.GetTypeN(selected_object) == 3: # 3 -> Object type: 四角形
        
        cross_line_rect()
        
        # 次の選択されたオブジェクトへハンドルを移動する
        selected_object = vs.NextSObj(selected_object)

    # もし選択しているオブジェクト(selected_object)が[多角形]オブジェクトだったら
    elif vs.GetTypeN(selected_object) == 5 and vs.GetVertNum(selected_object) == 4: # 5 -> Object type: 多角形
        
        
        cross_line_poly()
        
        # 次の選択されたオブジェクトへハンドルを移動する
        selected_object = vs.NextSObj(selected_object)

    else:
        # アラートダイアログを表示する
        vs.AlrtDialog("オブジェクトの種類が\n「四角形」または\n「頂点数が4つの多角形」ではありません") 

        selected_object = vs.NextSObj(selected_object)
            
