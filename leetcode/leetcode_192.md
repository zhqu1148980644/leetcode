---
title: Word Frequency
date: 2021-01-04
---
#### Write a bash script to calculate the frequency of each word in a text file words.txt.

#### For simplicity sake, you may assume:

-    words.txt contains only lowercase characters and space ' ' characters.
-    Each word must consist of lowercase characters only.
-    Words are separated by one or more whitespace characters.

```
Example:

Assume that words.txt has the following content:

the day is sunny the the
the sunny is is

Your script should output the following, sorted by descending frequency:

the 4
is 3
sunny 2
day 1
```

#### Note:

-    Don't worry about handling ties, it is guaranteed that each word's frequency count is unique.
-    Could you write it in one-line using Unix pipes?


#### Solutions

1. ##### 

- `egrep -v regex` exlucde lines with the given pattern.
- `uniq -c`  print count of each word

```bash
cat words.txt | sed "s/ /\\n/g" | egrep -v "^$" | sort | uniq -c | sort -nr | awk '{print $2" "$1}'
```

- `tr -s`: squeeze repeated sequence. ie \n\n -> \n 

```bash
cat words.txt | tr -s " " "\n" | sort | uniq -c | sort -nr | awk '{print $2" "$1}'
```