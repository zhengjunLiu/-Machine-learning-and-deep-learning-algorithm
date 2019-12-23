import sys
import math
from collections import defaultdict

class MaxEnt:
    def __init__(self):
        self._samples = []
        self._Y = set([]) # 标签集合，相当于去重之后的y
        self._numXY = defaultdict(int) # key是(xi,yi)对，value是count(xi,yi)
        self._N = 0 #样本数量
        self._n = 0 #特征对(xi,yi)总数量
        self._xyID = {} # 对（x，y）对做的顺序编号(ID)，key是(xi,yi)对，value是ID
        self._C = 0 # 样本最大的特征数量，用于求参数的迭代，见IIS原理说明
        self._ep_ = [] # 样本分布的特征期望值
        self._ep = [] # 模型分布的特征期望值
        self._w = [] # 对应n个特征的权值
        self._lastw = [] # 上一轮迭代的权值
        self._EPS = 0.01 # 判断是否收敛的阈值

    def load_data(self,filename):#初始化数据
        for line in open(filename,"r"):
            sample = line.strip().split(",")
            print(sample)
            if len(sample) < 2:
                print("数据数量不符合要求")
                continue
            y = sample[6]
            print(y)
            X = sample[0:6]
            print(X)
            self._samples.append(sample)
            self._Y.add(y)
            for x in set(X):
                self._numXY[(x,y)] += 1

    def _initparams(self):#赋值
        self._N = len(self._samples)
        self._n = len(self._numXY)
        self._C = max([len(sample) -1 for sample in self._samples])
        self._w = [0.0] * self._n
        self._lastw = self._w[:]
        self._sample_ep_()

    def _convergence(self):#设定停止条件
        for w,lw in zip(self._w,self._lastw):
            if math.fabs(w-lw) >= self._EPS:
                return False
        return True

    def _sample_ep_(self):
        self._ep_ = [0.0] * self._n
        for i,xy in enumerate(self._numXY):
            self._ep_[i] = self._numXY[xy] * 1.0 / self._N
            self._xyID[xy] = i

    def _zx(self,X):#计算ZX
        ZX = 0.0
        for y in self._Y:
            sum = 0.0
            for x in X:
                if(x,y) in self._numXY:
                    sum += self._w[self._xyID[(x,y)]]
            ZX += math.exp(sum)
        return ZX
    def _pyx(self,X):#计算P（y\x）
        ZX = self._zx(X)
        results = []
        for y in self._Y:
            sum = 0.0
            for x in X:
                if(x,y) in self._numXY:
                    sum += self._w[self._xyID[(x,y)]]
            pyx = 1.0 / ZX * math.exp(sum)
            results.append((y,pyx))
        return results
    def _model_ep(self):#训练模型
        self._ep = [0.0] * self._n
        for sample in self._samples:
            X = sample[0:6]
            pyx = self._pyx(X)
            for y,p in pyx:
                for x in X:
                    if(x,y) in self._numXY:
                        self._ep[self._xyID[(x,y)]] += p * 1.0 / self._N
    def train(self,maxiter = 100):
        self._initparams()
        for i in range(0,maxiter):
            print("Iter:%d...."%i)
            self._lastw = self._w[:]
            self._model_ep()

            for i,w in enumerate(self._w):
                self._w[i] += 1.0 / self._C * math.log(self._ep_[i] / self._ep[i])
            #
            print(self._w)

            if self._convergence():
                break
    def predict(self,inp):
        # X = inp.strip().split(",")
        prob = self._pyx(inp)
        return prob

if __name__ == "__main__":
    maxent = MaxEnt()
    maxent.load_data('data.txt')
    maxent.train()
    rght=0
    unaccrght=0
    accrght = 0
    goodrght = 0
    vgoodrght=0
    wrg=0
    unaccwrg = 0#unacc 分错个数
    accwrg = 0#acc分错个数
    goodwrg = 0#good分错个数
    vgoodwrg = 0#vgood分错个数
    unaccwrg1=0#unacc 预测错误
    accwrg1 = 0#acc 预测错误
    goodwrg1 = 0#good预测错误
    vgoodwrg1 = 0#vgood预测错误
    for line in open("test.txt", "r"):
        sample = line.strip().split(",")
        a=maxent.predict(sample[0:6])
        print (maxent.predict(sample[0:6]),",真实类:",sample[6])
        for i in range(0, 4):
            if a[i][1] == max(a[0][1], a[1][1], a[2][1], a[3][1]):
                if a[i][0] == sample[6]:
                    if sample[6]=="unacc":
                        unaccrght+=1
                    if sample[6]=="acc":
                        accrght+=1
                    if sample[6]=="good":
                        goodrght+=1
                    if sample[6]=="vgood":
                        vgoodrght+=1
                    rght += 1
                else:
                    if a[i][0]=="unacc":
                        unaccwrg1+=1
                    if a[i][0]=="acc":
                        accwrg1+=1
                    if a[i][0]=="good":
                        goodwrg1+=1
                    if a[i][0]=="vgood":
                        vgoodwrg1+=1


                    if sample[6]=="unacc":
                        unaccwrg+=1
                    if sample[6]=="acc":
                        accwrg+=1
                    if sample[6]=="good":
                        goodwrg+=1
                    if sample[6]=="vgood":
                        vgoodwrg+=1
                    wrg += 1
    print("---------------精确率--------召回率----------")
    print("unacc：        "+str(unaccrght/(unaccrght+unaccwrg1))+"---------"+str(unaccrght/(unaccrght+unaccwrg)))
    print("acc：        " + str(accrght / (accrght + accwrg1)) + "---------" + str(accrght / (accrght + accwrg)))
    # print("good：        " + str(goodrght / (goodrght + goodwrg1)) + "---------" + str(goodrght / (goodrght + goodwrg)))
    # print("vgood：        " + str(vgoodrght / (vgoodrght + vgoodwrg1)) + "---------" + str(vgoodrght / (vgoodrght + vgoodwrg)))


    print("正确数:"+str(rght),"  ，",str(rght/400)+",  错误数",str(wrg),"， "+str(wrg/400))

    sys.exit(0)