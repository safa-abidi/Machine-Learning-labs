
import numpy as np

def create_table(data):
    nb_samples = len(data)
    mat = np.zeros((nb_samples, nb_samples))
    for i in range(nb_samples):
        for j in range(nb_samples):
            mat[i][j] = abs(data[i]-data[j])
    return mat





def diss_moy(cluster,i):
    mat = create_table(cluster)
    return np.mean(mat[i])

def diss_moy_max(dist_matrix):
    max=0
    for i in range(len(dist_matrix[0])):
        temp = np.sum(dist_matrix[i])/(len(dist_matrix[i])-1)
        if(temp>max):
            m = i
            max = temp
    return m

def max_distance(cluster):
    mat = create_table(cluster)
    max = 0
    for i in range(len(mat[0])):
        temp = np.sum(mat[i]) / (len(mat[i]) - 1)
        if (temp > max):
            max = temp
    return max

data = np.array([74,87,51,55,24,28,15,6])

def distTothercluster(A,B,i):
    if(len(B)==1):
        return abs(B[0]-A[i])
    temp = np.copy(B)
    temp= np.append(temp,A[i])
    return diss_moy(temp,len(temp)-1)

def first_split(cluster):
    dist_matrix = create_table(cluster)
    index = diss_moy_max(dist_matrix)
    B = []
    B = np.append(B, cluster[index])
    print("b=",B)
    A = np.delete(cluster, index, 0)
    print("a=", A)

    return A,B


A,B = first_split(data)



#print(diss_moy(A,0))

#print(distTothercluster(A,B,0))
#diff=[]
def processClusters(A,B):
    i = 0
    nb = 0
    l = len(A) - 1
    while (nb < l):
        diff = diss_moy(A, i) - distTothercluster(A, B, i)
        print(diss_moy(A, i), '--', distTothercluster(A, B, i))
        print(diff)
        if (diff > 0):
            B = np.append(B, A[i])
            A = np.delete(A, i, 0)
        else:
            i += 1
        nb += 1

    return A,B

A,B = processClusters(A,B)

#print('aaaa:',A)
#print('bbbbbb:',B)


def nexTosplit(clusters):
    max = 0
    for i in range(len(clusters)):
        temp = max_distance(clusters[i])
        if(temp>max):
            max=temp
            index = i
    return index


clusters = np.array([A,B])
#print(nexTosplit(clusters))

def DIANA(data,k):
    if(k==1):
        return data

    i=1
    cluster = data
    clusters = []

    while(i<k):

        A,B = first_split(cluster)
        A,B = processClusters(A,B)

        if(len(clusters)>0 and i !=1):
            clusters.pop(index)

        clusters.append(A)
        clusters.append(B)
        #clusters = np.stack(B, A)
        #clusters = np.stack(clusters, B)
        print("=============================")
        print(clusters)

        index = nexTosplit(clusters)
        cluster = clusters[index]
        print(cluster)
        #clusters = np.delete(clusters, index, 0)
        i+=1

    return clusters


data2 = np.array([74,87,51,55,24,28,15,6])
#print(create_table(data2))
DIANA(data2,3)



