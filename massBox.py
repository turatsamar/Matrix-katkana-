from tkinter import*
import tkinter.messagebox as msgbox
win = Tk()
cv = Canvas(win, width=800, height=500)
cv.pack()

print("\n\n2本の直線を引き　その交点を表示する\n")

#原点位置　３５０．３００
#y=y0 x=x0 の立置　３５０＋ｘ０＊４０，３００－ｙ０＊４０
cv.create_line(350, 50, 350, 450, fill="green", width=2)
cv.create_line(100, 300, 700, 300, fill="green", width=2)
cv.create_text(350, 40, text="Y", font= ('FixedSys', 20), fill="green")
cv.create_text(710, 300, text="X", font =('FixedSys', 20), fill="green")
for i in range(12):
    if i-4 != 0:
        cv.create_text(350+(i-4)*40, 300+ 10, text= str(i-4), font = ('FixedSys', 10), fill="black")
    if (i-4 !=-4)and(i-4 !=0)and(i-4!= 7):
        cv.create_text(350+10, 300-(i-4)*40, text=str(i-4), font = ('FixedSys', 10), fill="black")

msgbox.showinfo(title="説明", message="直線 y=ax+b の係数を入力しなさい")
print("直線 1 y=a1*x+b1 の　a1 　と　b1　を入力 ")
a1 = float(input("   -5<a1<5  a1="))
b1 = float(input("    -3<b1<5  b1="))
print("直線 2 y=a2*x+b2 の a2　と b2 　入力")
a2 = float(input("   -5<a2<5 a2="))
b2 = float(input("    -3<b2<5  b2="))
#y=a1*x+b1 のグラフを書く時の　2　点
x11 = -4
y11 = a1*x11+b1
x12 = 7
y12 = a1*x12+b1
#y=a2*x+b2のグラフを書く時の　2点
x21 = -4
y21 = a2*x21+b2
x22 = 7
y22 = a2*x22+b2

cv.create_line(350+x11*40, 300-y11*40, 300+x12*40, 300-y12*40, fill="red", width=2)
cv.create_line(350+x21*40, 300-y21*40, 300+x22*40, 300-y22*40, fill="blue", width=2)
if a1 >= 0:
    if y12 > 7:y12 = 6
    cv.create_text(350+7*40, 300-y12*40-8, text="y=("+str(a1)+")x+("+str(b1)+")", font=('FixedSys', 20), fill="magenta")
else:
    if y11>7:y11=6
    cv.create_text(350-4*40, 300-y11*40-8, text="y=("+str(a1)+")x+("+str(b1)+")", font=('FixedSys', 20), fill="magenta")
if a2>=0:
    if y11>7:y11=6
    cv.create_text(350+7*40, 300-y22*40-8, text="y=("+str(a2)+")x+("+str(b2)+")", font=('FixedSys', 20), fill="black")
else:
    if y21>7:y21=6
    cv.create_text(350-4*40, 300-y21*40-8, text="y=("+str(a2)+")x+("+str(b2)+")", font=('FixedSys', 20), fill="black")

#   交点を求める
print("交点は　x:-4 ~ 7 の雰囲内で計算します。")
x = -4
dx = 0.0001
n = 0
ch = 0
while True:
    n=n+1
    y1=a1*x+b1
    if a2*x+b2<=y1+0.0001 and a2*x+b2>=y1-0.0001:
        ch = 1
        break
    x = x+dx
    if x >7:break
print("繰り返し回数　　"+str(n))
if ch==1:
    x=round(x,2)
    y=round(y1,2)
    if y==-0.0:y=0.0
    print("交点座標　　("+str(x)+","+str(y)+")")
    cv.create_text(500, 450, text="交点座標　("+str(x)+","+str(y)+")", font= ('FixedSys', 20), fill="red")
    X1 = 350+x*40
    Y1 = 300-y*40
    X2 = X1
    Y2 = 300-0*40
    X2 = 350+0*40
    X3 = 350+0*40
    Y3=Y1
    cv.create_line(X1, Y1, X2, Y2, fil="black", width=1)
    cv.create_line(X1, Y1, X3, Y3, fil="black", width=1)
else:
    print("答えはありません")
    cv.create_text(500, 450, text="答えはありません", font=('FixedSys', 20), fill="red")


