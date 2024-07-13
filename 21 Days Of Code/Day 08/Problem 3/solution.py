def is_possible(books, n, m, max_pages):
    student_count = 1
    current_pages = 0
    
    for i in range(n):
        if current_pages + books[i] > max_pages:
            student_count += 1
            current_pages = books[i]
            
            if student_count > m:
                return False
        else:
            current_pages += books[i]
    
    return True

def find_min_max_pages(books, n, m):
    low = max(books)
    high = sum(books)
    result = high
    
    while low <= high:
        mid = (low + high) // 2
        
        if is_possible(books, n, m, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return result

# Reading input
import sys
input = sys.stdin.read
data = input().strip().split()
index = 0
t = int(data[index])
index += 1

results = []
for _ in range(t):
    n = int(data[index])
    m = int(data[index + 1])
    index += 2
    books = list(map(int, data[index:index + n]))
    index += n
    result = find_min_max_pages(books, n, m)
    results.append(result)

# Printing results for each test case
for result in results:
    print(result)
