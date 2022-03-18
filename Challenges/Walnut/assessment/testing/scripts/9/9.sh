#!/bin/bash

start=$(date +%s.%3N)
curl -i "http://127.0.0.1:5000/api/posts?tags=science"
end=$(date +%s.%3N)
total_time=$(echo "scale=3; $end - $start" | bc)
echo ""
echo "Request: http://127.0.0.1:5000/api/posts?tags=science ; Total Time: "$total_time
echo "+----------------------------------------------------------------+"

start=$(date +%s.%3N)
curl -i "http://127.0.0.1:5000/api/posts?tags=history,math,culture"
end=$(date +%s.%3N)
total_time=$(echo "scale=3; $end - $start" | bc)
echo ""
echo "Request: http://127.0.0.1:5000/api/posts?tags=history,math,culture ; Total Time: "$total_time
echo "+----------------------------------------------------------------+"

start=$(date +%s.%3N)
curl -i "http://127.0.0.1:5000/api/posts?tags=science"
end=$(date +%s.%3N)
total_time=$(echo "scale=3; $end - $start" | bc)
echo ""
echo "Request: http://127.0.0.1:5000/api/posts?tags=science ; Total Time: "$total_time
echo "+----------------------------------------------------------------+"

start=$(date +%s.%3N)
curl -i "http://127.0.0.1:5000/api/posts?tags=culture&sortBy=id"
end=$(date +%s.%3N)
total_time=$(echo "scale=3; $end - $start" | bc)
echo ""
echo "Request: http://127.0.0.1:5000/api/posts?tags=culture&sortBy=id ; Total Time: "$total_time
echo "+----------------------------------------------------------------+"

start=$(date +%s.%3N)
curl -i "http://127.0.0.1:5000/api/posts?tags=culture&sortBy=reads"
end=$(date +%s.%3N)
total_time=$(echo "scale=3; $end - $start" | bc)
echo ""
echo "Request: http://127.0.0.1:5000/api/posts?tags=culture&sortBy=reads ; Total Time: "$total_time
echo "+----------------------------------------------------------------+"

start=$(date +%s.%3N)
curl -i "http://127.0.0.1:5000/api/posts?tags=culture&sortBy=likes"
end=$(date +%s.%3N)
total_time=$(echo "scale=3; $end - $start" | bc)
echo ""
echo "Request: http://127.0.0.1:5000/api/posts?tags=culture&sortBy=likes ; Total Time: "$total_time
echo "+----------------------------------------------------------------+"

start=$(date +%s.%3N)
curl -i "http://127.0.0.1:5000/api/posts?tags=culture&sortBy=popularity"
end=$(date +%s.%3N)
total_time=$(echo "scale=3; $end - $start" | bc)
echo ""
echo "Request: http://127.0.0.1:5000/api/posts?tags=culture&sortBy=popularity ; Total Time: "$total_time
echo "+----------------------------------------------------------------+"

start=$(date +%s.%3N)
curl -i "http://127.0.0.1:5000/api/posts?tags=culture&sortBy=id"
end=$(date +%s.%3N)
total_time=$(echo "scale=3; $end - $start" | bc)
echo ""
echo "Request: http://127.0.0.1:5000/api/posts?tags=culture&sortBy=id ; Total Time: "$total_time
echo "+----------------------------------------------------------------+"

start=$(date +%s.%3N)
curl -i "http://127.0.0.1:5000/api/posts?tags=culture&sortBy=reads"
end=$(date +%s.%3N)
total_time=$(echo "scale=3; $end - $start" | bc)
echo ""
echo "Request: http://127.0.0.1:5000/api/posts?tags=culture&sortBy=reads ; Total Time: "$total_time
echo "+----------------------------------------------------------------+"

start=$(date +%s.%3N)
curl -i "http://127.0.0.1:5000/api/posts?tags=culture&sortBy=likes"
end=$(date +%s.%3N)
total_time=$(echo "scale=3; $end - $start" | bc)
echo ""
echo "Request: http://127.0.0.1:5000/api/posts?tags=culture&sortBy=likes ; Total Time: "$total_time
echo "+----------------------------------------------------------------+"

start=$(date +%s.%3N)
curl -i "http://127.0.0.1:5000/api/posts?tags=culture&sortBy=popularity"
end=$(date +%s.%3N)
total_time=$(echo "scale=3; $end - $start" | bc)
echo ""
echo "Request: http://127.0.0.1:5000/api/posts?tags=culture&sortBy=popularity ; Total Time: "$total_time
echo "+----------------------------------------------------------------+"

start=$(date +%s.%3N)
curl -i "http://127.0.0.1:5000/api/posts?tags=culture&sortBy=id&direction=desc"
end=$(date +%s.%3N)
total_time=$(echo "scale=3; $end - $start" | bc)
echo ""
echo "Request: http://127.0.0.1:5000/api/posts?tags=culture&sortBy=id ; Total Time: "$total_time
echo "+----------------------------------------------------------------+"

start=$(date +%s.%3N)
curl -i "http://127.0.0.1:5000/api/posts?tags=culture&sortBy=reads&direction=desc"
end=$(date +%s.%3N)
total_time=$(echo "scale=3; $end - $start" | bc)
echo ""
echo "Request: http://127.0.0.1:5000/api/posts?tags=culture&sortBy=reads ; Total Time: "$total_time
echo "+----------------------------------------------------------------+"

start=$(date +%s.%3N)
curl -i "http://127.0.0.1:5000/api/posts?tags=culture&sortBy=likes&direction=desc"
end=$(date +%s.%3N)
total_time=$(echo "scale=3; $end - $start" | bc)
echo ""
echo "Request: http://127.0.0.1:5000/api/posts?tags=culture&sortBy=likes ; Total Time: "$total_time
echo "+----------------------------------------------------------------+"

start=$(date +%s.%3N)
curl -i "http://127.0.0.1:5000/api/posts?tags=culture&sortBy=popularity&direction=desc"
end=$(date +%s.%3N)
total_time=$(echo "scale=3; $end - $start" | bc)
echo ""
echo "Request: http://127.0.0.1:5000/api/posts?tags=culture&sortBy=popularity&direction=desc ; Total Time: "$total_time
echo "+----------------------------------------------------------------+"

start=$(date +%s.%3N)
curl -i "http://127.0.0.1:5000/api/posts?tags=culture&sortBy=id&direction=desc"
end=$(date +%s.%3N)
total_time=$(echo "scale=3; $end - $start" | bc)
echo ""
echo "Request: http://127.0.0.1:5000/api/posts?tags=culture&sortBy=id ; Total Time: "$total_time
echo "+----------------------------------------------------------------+"

start=$(date +%s.%3N)
curl -i "http://127.0.0.1:5000/api/posts?tags=culture&sortBy=reads&direction=desc"
end=$(date +%s.%3N)
total_time=$(echo "scale=3; $end - $start" | bc)
echo ""
echo "Request: http://127.0.0.1:5000/api/posts?tags=culture&sortBy=reads ; Total Time: "$total_time
echo "+----------------------------------------------------------------+"

start=$(date +%s.%3N)
curl -i "http://127.0.0.1:5000/api/posts?tags=culture&sortBy=likes&direction=desc"
end=$(date +%s.%3N)
total_time=$(echo "scale=3; $end - $start" | bc)
echo ""
echo "Request: http://127.0.0.1:5000/api/posts?tags=culture&sortBy=likes ; Total Time: "$total_time
echo "+----------------------------------------------------------------+"

start=$(date +%s.%3N)
curl -i "http://127.0.0.1:5000/api/posts?tags=culture&sortBy=popularity&direction=desc"
end=$(date +%s.%3N)
total_time=$(echo "scale=3; $end - $start" | bc)
echo ""
echo "Request: http://127.0.0.1:5000/api/posts?tags=culture&sortBy=popularity&direction=desc ; Total Time: "$total_time
echo "+----------------------------------------------------------------+"