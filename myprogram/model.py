# import libraries
from sklearn.cluster import KMeans

try:
    class kmeans(KMeans):
        """
        A derived class of class KMeans in sklearn.cluster module
         """
        pass
except:
    print('K - means not installed yet')
