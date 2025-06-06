str1 = "my name is vaidehi deep ."
str2 = 'pce purnea'
str3 =23105131013
str4 = """"C.S.E""" #why we use single and double or tripple inverted commas in python
#'this is vaidehi's tutorial' here we are already a single approstes ' for vaidehi so our compiler might get confused therefore in that case we use double inverted comma 
#escape sequence characters are some special characters used for formatting like next line ,tab we do not do directly in code
str4 = "komal\n vaidehi \nmuskan \n kajal \n kunal"#\n for next line inpython.
#concatenation = simply use '+', between any two string 
print(str1+str2)
print(str4)
print(len(str1)) #len(str) used to caalulate langth of string , also counts space 
#indexing = position , intrnally starting from 0 , used to access characters  str[1],str[3]....
print(str2[5])#u
#but we can not change value of string using index like str2[5]= k ; not allowed 
#slicing =accessing parts of string str[starting index :ending index] where ending index value is not included
print(str1[0:13])
print(str2[3:])#last index nahi likhege to woo khud se last index tak le lega 