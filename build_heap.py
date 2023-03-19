def sift_down(arr, i, swaps):
    n = len(arr)
    min_index = i
    left_child = 2*i + 1
    if left_child < n and arr[left_child] < arr[min_index]:
        min_index = left_child
    right_child = 2*i + 2
    if right_child < n and arr[right_child] < arr[min_index]:
        min_index = right_child
    if i != min_index:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps.append((i, min_index))
        sift_down(arr, min_index, swaps)

def build_heap(arr):
    n = len(arr)
    swaps = []
    for i in range(n//2, -1, -1):
        sift_down(arr, i, swaps)
    return swaps

n = int(input())
arr = list(map(int, input().split()))
swaps = build_heap(arr)

def main():
    text = input()
    if 'I' in text:
        text = input()
    elif 'F' in text:
        file = "./test/5"
        with open(file) as f:
            text = f.read()
    mismatch = find_mismatch(text)
    if not mismatch:
        print("Success")
    else:
        print(mismatch)
if __name__ == "__main__":
    main()

print(len(swaps))
for i, j in swaps:
    print(i, j)
