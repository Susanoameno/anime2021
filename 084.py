from anime2021.anime inport Ashape, Atext, Aimage

class AImage(AShape):
    color: any

    def __init__(self, width=100, height=None, cx=None, cy=None, image='buun.png'):
        AShape.__init__(self, width, height, cx, cy)
        if image.startswith('http'):
            # URLから直接読み込む
            self.pic = Image.open(io.BytesIO(requests.get(image).content))
        else:
            self.pic = Image.open(image)

    def render(self, canvas: ACanvas, frame: int):
        ox, oy, w, h = self.bounds()
        pic = self.pic.resize((int(w), int(h)))
        canvas.image.paste(pic, (int(ox), int(oy)), pic)
        
class RollingPolygon(APolygon):

    def render(self, canvas: ACanvas, tick: int):
        theta = math.pi * 2 / self.N
        slope = math.pi * 2 * 30 * (tick/180)  # 自転させる
        # 半径
        r = min(self.width, self.height)/2
        # 頂点の数だけ頂点の座標を計算する
        points = []
        for i in range(self.N):
            x = self.cx + r * math.cos(theta*i + self.slope + slope)
            y = self.cy + r * math.sin(theta*i + self.slope + slope)
            points.append((x, y))
        canvas.draw.polygon(points, fill=self.color)
class BunnBunn(AShape):
    def __init__(self, width=50, height=None, cx=None, cy=None, N=5):
      AShape.__init__(self, width, height, cx, cy)
      self.poly = AText(width=200, data="ﾌﾞｰｰｰｰｰﾝ")
      self.buun = AImage(width, height, image='buun.png')

    def render(self, canvas, tick):
      self.poly.cx =self.cx
      self.poly.cy =self.cy
      self.buun.cx =self.cx
      self.buun.cy =self.cy
      self.poly.render(canvas, tick)
      self.buun.render(canvas, tick)
      
 shape = BunnBunn(80, 80)
IPython.display.Image(test_shape(shape))
