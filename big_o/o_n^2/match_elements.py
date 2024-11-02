

def match_elements(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i!=j and arr[i]==arr[j]:
                print(f"Match found at {arr[i]} and {arr[j]}")
    return f"No other match found"


fruits =["🍉", "🍊", "🍏", "🥭", "🍑", "🍌", "🍍", "🍈", "🍇", "🍋", "🍏", "🥝", "🥑", "🥧", "🍉", "🍒", "🍐"]

print(match_elements(fruits))
