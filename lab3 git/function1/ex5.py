def permute_string(s):
    def permute_helper(s, prefix):
        if len(s) == 0:
            print(prefix)
        else:
            for i in range(len(s)):
                permute_helper(s[:i] + s[i+1:], prefix + s[i])

    permute_helper(s, "")

inp = input("Enter a string: ")
permute_string(inp)
