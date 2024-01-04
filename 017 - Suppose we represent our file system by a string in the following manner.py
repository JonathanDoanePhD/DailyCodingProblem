# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Suppose we represent our file system by a string in the following manner:

# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

# We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

# Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

# Note:

# The name of a file contains at least a period and an extension.

# The name of a directory or sub-directory will not contain a period.

a0 = r'dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext'
a1 = r'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'

# def Depth(in_dir=a1):
#     d = in_dir
#     UB = len(d) // 2
#     it = UB
#     condition = len(d.split(r'\t'*it)) == 1
#     while condition:
#         it -= 1
#         condition = len(d.split(r'\t'*it)) == 1
#     return it

# print(Depth())

def ANS(in_dir=a1):
    d = in_dir.split(r'\n')
    lvl_old = 0
    out = []
    for i, x in enumerate(d):
        lxt = len(x)
        if i == 0:
            out.append(lxt)
            print(f'Iteration {i}: len(dir)={out[-1]}')
            print()
            tracker = [] # [lxt]
        else:
            lx = len(x.replace(r'\t', ''))
            lvl_new = (lxt - lx) // 2
            print(f'Iteration {i}:')
            print(f'lvl new/old: {lvl_new}/{lvl_old}')
            print(f'Tracker: {tracker}')
            if lvl_new > lvl_old:
                lvl_old = lvl_new
                tracker.append(out[-1])
                # print(x)
                result = out[-1] + 1 + lx
                # tracker.append(result)
                print(f'Forw {out[-1]} + 1 + {lx} = {result}')
                print()
                out.append(result)
            elif lvl_new == lvl_old:
                result = tracker[-1] + 1 + lx
                print(f'Same {tracker[-1]} + 1 + {lx} = {result}')
                print()
                out.append(result)
            else:
                result = tracker[-2] + 1 + lx
                print(f'Back {tracker[-2]} + 1 + {lx} = {result}')
                print()
                out.append(result)
        
    return out

# print([x for x in a1.split(r'\n\t\t\t') if r'\t' not in x])
# print(a1.split(r'\n\t\t'))

# print(a1)
# print(a1.split(r'\n'))
# print(a1.split(r'\n\t'))

A = ANS()
print(A, A == [3, 11, 21, 22, 11, 22, 32])

# print()
# print(a1.replace(r'\n', ''))

# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext

# [3]
# [[3+1+7], [3+1+7]]
# [[[11+1+9], [11+1+10]], [[11+10]]]