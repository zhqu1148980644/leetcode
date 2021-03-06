---
title: Read N Characters Given Read4 II   Call multiple times
date: 2021-01-04
---
Given a file and assume that you can only read the file using a given method read4, implement a method read to read n characters. Your method read may be called multiple times.

 

Method read4:

The API read4 reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf4
    Returns:    int

Note: buf4[] is destination not source, the results from read4 will be copied to buf4[]
Below is a high level example of how read4 works:



File file("abcde"); // File is "abcde", initially file pointer (fp) points to 'a'
char[] buf = new char[4]; // Create buffer with enough space to store characters
read4(buf4); // read4 returns 4. Now buf = "abcd", fp points to 'e'
read4(buf4); // read4 returns 1. Now buf = "e", fp points to end of file
read4(buf4); // read4 returns 0. Now buf = "", fp points to end of file
 

Method read:

By using the read4 method, implement the method read that reads n characters from the file and store it in the buffer array buf. Consider that you cannot manipulate the file directly.

The return value is the number of actual characters read.

Definition of read:

    Parameters:	char[] buf, int n
    Returns:	int

Note: buf[] is destination not source, you will need to write the results to buf[]
 

Example 1:

File file("abc");
Solution sol;
// Assume buf is allocated and guaranteed to have enough space for storing all characters from the file.
sol.read(buf, 1); // After calling your read method, buf should contain "a". We read a total of 1 character from the file, so return 1.
sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters from the file, so return 2.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
Example 2:

File file("abc");
Solution sol;
sol.read(buf, 4); // After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
 

Note:

Consider that you cannot manipulate the file directly, the file is only accesible for read4 but not for read.
The read function may be called multiple times.
Please remember to RESET your class variables declared in Solution, as static/class variables are persisted across multiple test cases. Please see here for more details.
You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.
It is guaranteed that in a given test case the same buffer buf is called by read.


#### Solutions

1. ##### buffer overflow characters

- A better choice is to use ring buffer instead.

```cpp
/**
 * The read4 API is defined in the parent class Reader4.
 *     int read4(char *buf);
 */

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    queue<char> buffer;

    int read(char *buf, int n) {
        if (!n) return 0;
        int bs = 0;
        // read from buffer
        if (buffer.size()) {
            int rs = min((int)buffer.size(), n);
            for (int i = 0; i < rs; i++) {
                buf[bs++] = buffer.front();
                buffer.pop();
            }
        }
        // if not enough, read from read4
        while (bs < n) {
            int cnt = read4(buf + bs);
            bs += cnt;
            if (cnt < 4)
                break;
        }
        // if overflowed, store in buffer
        if (bs > n) {
            for (int i = 0, ws = bs - n; i < ws; i++) {
                buffer.push(buf[n + i]);
            }
        }

        return min(bs, n);
    }
};
```

- or always treat the buffer as the intermidiate buffer.

```cpp
class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */

    char buffer[4];
    int len = 0;
    int r = 0;

    int read(char *buf, int n) {
        int bs = 0;
        while (bs < n) {
            // Fill our buffer when it's empty.
            if (r == 0 && (len = read4(buffer)) == 0)
                 break;
            // only read from our own buffer
            while (r < len && bs < n) {
                buf[bs++] = buffer[r++];
            }
            if (r == len) r = 0;
        }

        return bs;
    }
};
```