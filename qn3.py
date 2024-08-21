'''Problem statement
You are required to implement the following function:
char* FrequentCharacterReplaced(char*' str, char x); 
The function accepts a string 'str' and a character 'x' as its arguments. You are 
required to find the most frequent character in string 'str' and replace it with character 'x' across
 the string, and return the same. 
Note :
If the frequency of two characters are the same, we have to consider the character with lower ascii value. 
Example:
Input: 
bbadbbababb 
t
Output: 
ttadttatatt 
Explanation: 
The most frequent character in string 'str' is 'b', replacing 'b' with 't' will 
form string 'ttadttatatt', hence 'ttadttatatt' is returned. '''
a = input().strip()
b = input().strip()
total = {}
for i in a:
    if i not in total:
        total[i] = 1
    else:
        total[i] += 1
c = max(total, key = total.get)
print(a.replace(c,b))
