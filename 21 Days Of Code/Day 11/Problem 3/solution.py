def is_balanced(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if stack == [] or bracket_map[char] != stack.pop():
                return "No"
        else:
            return "No"  # In case there's any invalid character
    return "Yes" if stack == [] else "No"

def main():
    s = input().strip()
    print(is_balanced(s))

if __name__ == "__main__":
    main()
