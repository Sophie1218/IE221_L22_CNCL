from sklearn.cluster import KMeans

try:
    class kmeans(KMeans):
        pass
except:
    print('K - means not installed yet')
