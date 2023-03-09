#Created by K.Machida Mar. 2023.
import vs


def cross_line(sobj):
	vs.BeginGroup() #ここから先のオブジェクトをグループにしたい
	
	(p1, p2) = vs.GetBBox(sobj) #オブジェクトの左上(p1)と右下(p2)の座標を(p1, p2)とする
	
	vs.MoveTo(p1) #p1の座標にポイントを置く(ラインの始点となる座標を指定する)
	vs.LineTo(p2) #p1座標からp2座標までラインをひく
	objH = vs.LNewObj() #引いたラインのハンドルをobjHとする
	
	cent = vs.HCenter(objH) #引いたラインのセンターの座標をcentとする
	centx = cent[0] #センター座標のXの値をcentｘとする
	centy = cent[1] #センター座標のYの値をcentyとする
	
	centtop = (centx,p1[1]) #センター座標のXの値(centx)と最初に引いたラインの始点(p1)のY座標の値(p1[1])をcentupとする
	
	vs.Mirror(objH, True, cent, centtop) #最初に引いたラインを反転複製する(cent座標とcenttop座標からなる軸を基準としてとして)
	
	vs.EndGroup() #ここまでのオブジェクトをグループにする


sobj = vs.FSActLayer() #アクティブレイヤ上で選択したオブジェクトの最も上のオブジェクトのハンドルをsobjとする


for i in range(vs.NumSObj(vs.ActLayer())): #アクティブレイヤ上で選択されたオブジェクトの数だけ以下のforでくくった実行文を繰り返し実行する
	cross_line(sobj) #先に定義したcross_line(sobj)を25行目で選択したオブジェクトに実行する
	sobj = vs.NextSObj(sobj) #25行目で選択したオブジェクトの次のオブジェクトをsobjとする->28行目のrange()でカウントした数だけ29行目と30行目を繰り返す


vs.DSelectAll() #全ての選択を解除
vs.SelectObj("T=GROUP") #グループ図形を選択
