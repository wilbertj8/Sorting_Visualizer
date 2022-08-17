from Visualizer.draw_information import draw_list

def merge(arr, start, mid, end, draw_info, delay):
    start2 = mid + 1

    if (arr[mid] <= arr[start2]):
        return

    while (start <= mid and start2 <= end):
  
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2
  
            while (index != start):
                arr[index] = arr[index - 1]
                index -= 1
                draw_list(draw_info, {index: draw_info.SEAGREEN, index-1: draw_info.PINK}, True, delay)
  
            arr[start] = value
            draw_list(draw_info, {start: draw_info.SEAGREEN, start+1: draw_info.PINK}, True, delay)

            start += 1
            mid += 1
            start2 += 1

def merge_sort(draw_info, ascending=True, delay=10):
    lst = draw_info.lst
    l, r = 0, len(lst)-1
    mergeSort(lst, l, r, draw_info, delay)

def mergeSort(arr, l, r, draw_info, delay):
    if (l < r):
        m = (l + r) >> 1
  
        mergeSort(arr, l, m, draw_info, delay)
        mergeSort(arr, m + 1, r, draw_info, delay)

        merge(arr, l, m, r, draw_info, delay)