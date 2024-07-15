#Example 10.8 Search keywords in news feed import re

search_list = ['bbc', 'google', 'yahoo']
long_string = 'Read RSS news from bbc and '
if re.compile('|'.join(search_list),re.IGNORECASE).search(long_string): 
    print("Key words present")
else:
    print("Key words not present")


results = any(item in long_string for item in search_list)
print(results)
