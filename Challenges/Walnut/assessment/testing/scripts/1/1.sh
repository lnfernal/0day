#!/bin/bash

params=('science' 'math' 'history' 'trucks' 'cake' ',' ',,' 'jack-in-the-box' '-' 'zzz' 'a' 'qwerty' '&' '%' '!' '@' '#' '$' '^' '*' '(' ')' '')
url='http://127.0.0.1:5000/api/posts?tags='
for p in ${params[@]}; do 
	while read line; do
		curl -i $url$p'&sortBy='$line >> 1_results.txt
	done < /home/maximillian/Documents/wordlists/burp-parameter-names.txt
done
