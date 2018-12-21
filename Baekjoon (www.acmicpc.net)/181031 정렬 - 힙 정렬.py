array = [1,5,4,2,1,6]

def heapify(arr, idx):
    length = len(arr)
    if idx*2+2 < length:
        if arr[idx*2 +1] > arr[idx*2 +2]:
            child_idx= idx*2+1
        else:
            child_idx  = idx*2+2
    elif idx*2+1 <length : # 자식 노드가 한 개뿐일 때
        child_idx = idx*2+1
    else: # 자식 노드가 없을 경우
        return(arr)

    if arr[idx] < arr[child_idx]:
        arr[idx], arr[child_idx] = arr[child_idx], arr[idx]
    else:
        pass
    return arr

print(heapify(array, 0))