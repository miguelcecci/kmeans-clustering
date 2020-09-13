# precision and recall
import random

def getClosercluster(val, cluster):

    # val current data value
    # list containing all cluster values

    # returns the index of cluster which is closest to val

    closest, closestcluster = 100000000, 0 #infinite value, and the index of closest
    for cluster_index, cluster_value in enumerate(cluster):
        if val == cluster_value:
            return cluster_index
        if abs(cluster_value - val) <= closest: #verify if the current value is closer than the closest from previous iterations
            closest, closestcluster = abs(cluster_value-val), cluster_index
    return closestcluster

# print(getCloserK(8, [10, 2, 30]))

def getClusterized(data, cluster):

    # data - list containing all data
    # cluster - cluster values

    new_cluster_list = [[] for i in range(len(cluster))] 
    
    #put data value on list wich cluster is closer
    for i in data:
        new_cluster_list[getClosercluster(i, cluster)].append(i)

    return new_cluster_list

def getNewMean(data, cluster):

    # data - list containing all data
    # cluster - cluster values

    # returns the new values of cluster

    new_cluster_list = getClusterized(data, cluster) #put data value on list wich cluster is closer
    for i in range(len(new_cluster_list)):
        new_cluster_list[i] = sum(new_cluster_list[i])/len(new_cluster_list[i])
    return new_cluster_list
    
# print(getNewMean([2, 10, 10, 10, 30, 31], [2, 2, 30]))

def randomInitializeK(data, K):
    
    # data
    # K: int - cluster size
    # returns random initialization points: 1d list of size K 

    aux = list(set(data))
    new_k = []

    # get 3 distinct values from data
    for i in range(K):
        rand_index = random.randint(0, len(aux)-1)
        new_k.append(aux[rand_index])
        del aux[rand_index]
    
    return new_k
        

def variance(data):

    # data 1d list
    # returns variance

    m = sum(data) / len(data)
    return sum((xi - m) ** 2 for xi in data) / len(data)

def varianceScore(data, cluster):

    # data
    # cluster 

    clusterized_list = getClusterized(data, cluster) #put data value on list wich cluster is closer
    for i in range(len(clusterized_list)):
        clusterized_list[i] = variance(clusterized_list[i])
    return clusterized_list


def kmeans(data, K):

    # data: 1d List - data
    # K: int - cluster size

    clusters = randomInitializeK(data, K)
    previous_clusters = clusters
    print('clusters initialized with: '+str(clusters))


    # iterate until clusters stop changing values
    # while previous_clusters == clusters:
    for i in range(10):
        previous_clusters = clusters
        # print(clusters)
        clusters = getNewMean(data, clusters)
    print('Variance Score: '+str(varianceScore(data, clusters)))
    # print('Variance Score: '+varianceScore(data, clusters))
    return clusters


print(kmeans([1,1,1,2,2,2,7,8,9,20,21,22, 50], 4))

## iterar mais vezes e pegar a menor variancia

                




