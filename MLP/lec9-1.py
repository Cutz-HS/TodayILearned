class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None
    
    def foward(self, x, y):
        self.x = x
        self.y = y
        out = x * y
        return out
    
    def backward(self, dout):
        dx = dout * self.y
        dy = dout * self.x
        return dx, dy
    
class AddLayer(MulLayer):
    def __init__(self):
        pass
    
    def fowrard(self, x, y):
        out = x + y
        return out
    
apple = 100
apple_num = 2
tax = 1.1

mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

# 순전파 #
apple_price = mul_apple_layer.foward(apple, apple_num)
price = mul_tax_layer.foward(apple_price, tax)

dprice = 1
dapple_price, dtax = mul_tax_layer.backward(dprice)
daaple, dapple_num = mul_apple_layer.backward(dapple_price)

print(price)
print(daaple)
print(dapple_num)
print(dtax)