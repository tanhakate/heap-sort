from math import floor

def parenti(i):
    return floor(i/2)
def left(i):
    return (2*i)+1
def right(i):
    return 2*i+2


def max_heapify(array, count):
    end = 1 #end is assigned the index of the first (left) child of the root
    while end < count: #sift up the node at index end to the proper place such that all nodes above the end index are in max-heap order.
        # Terminate loop when you have siftedup the last element of the array
        siftUp(array,0,end)
        end = end + 1 #assign to the next child
        #after sifting up for all the elements, all nodes are in heap order

def siftUp(a,start,end):
    #start represents the limit of how far up the heap to sift
    child = end #end is the node to sift up from
    while child>start:  #as long as we have not reach the limit of how far up to heap
        parent = parenti(child) #compute the parent of the child we are considering
        if a[parent]<a[child]: #swap if out-of max heap order
            a[parent], a[child] = a[child], a[parent]
            child = parent # set the child as the new parent to compare with the elements up the heap
        else:
            return


A = [2, 3, 8, 7, 4, 9, 13, 1, 16, 19, 3, 5, 7]
max_heapify(A,len(A))
print(A)