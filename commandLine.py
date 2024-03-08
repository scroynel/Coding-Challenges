'''
Have the function CommandLine(strParam) take the
strParam parameter being passed which represents the
parameters given to a command in an old PDP
system. The parameters are alphanumeric tokens
(without spaces) followed by an equal sign and by
their corresponding value. Multiple parameters/value
pairs can be placed on the command line with a single
space between each pair. Parameter tokens and values
cannot contain equal signs but values can contains 
spaces. The purpose of the function is to isolate
the parameters and values to return a list of 
parameter and value lengths. It must provide its
result in the same format and in the same order
by replacing each entry (tokens and values) by its
corresponding length.

For example, if strParam is: "SampleNumber=3234 provider=
Dr. M. Welby patient=John Smith priority=High" then
your function should return the strParaming "12=4 8=12 
7=10 8=4" because "SampleNumber" is a 12 character
token with a 4 character value("3234") followed by 
"provider" which is an 8 character token by a 12
character value ("Dr. M. Welby"), etc.

Examples:

Input: "letters=A B Z T numbers=1 2 26 20 combine=true"
Output "7=7 7=9 7=4"

'''

def CommandLine(strParam):
    strParam = strParam.split('=')
    print(strParam)

    new_list = []

    result = []

    for i in range(len(strParam)):
        if strParam[i].count(" ") > 1:
            print("Here")
            new_list.append(strParam[i][:strParam[i].rfind(" ")])
            new_list.append(strParam[i][strParam[i].rfind(" "):].strip())
        else:    
            new_list.append(strParam[i])

    for i in range(0, len(new_list), 2):
        result.append(str(len(new_list[i])) + "=" + str(len(new_list[i+1])))

    return ' '.join(result)

print(CommandLine("letters=A B Z T numbers=1 2 26 20 combine=true"))