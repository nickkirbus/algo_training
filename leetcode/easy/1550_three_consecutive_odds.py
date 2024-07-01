def threeConsecutiveOdds(arr) -> bool:
    window_width = 3
    for i in range(len(arr)):
        end_index = i+3
        if end_index > len(arr):
            break
        cur_slice = arr[i:end_index]
        odds = [ num%2!=0 for num in cur_slice]
        if all(odds) and len(odds)==window_width:
            return True
    return False
