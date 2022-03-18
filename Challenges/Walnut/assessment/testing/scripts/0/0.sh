#!/bin/bash
url="http://127.0.0.1:5000/api/posts?tags="
params=('science' 'math' 'history' 'trucks' 'cake' ',' ',,' 'jack-in-the-box' '-' 'zzz' 'a' 'qwerty' '&' '%' '!' '@' '#' '$' '^' '*' '(' ')' '')
for p in ${params[@]}; do 
	curl -i $url$p >> '0_results1.txt'
done
