# [단어 정렬](https://www.acmicpc.net/problem/1181)
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로

<br>

### 입력
첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

### 출력
조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.


### Example Input
```
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
```
### Example Output
```
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
```

## 접근방식
**정렬**
- 입력된 단어들 중복제거, 리스트 변환
- key에 람다 함수를 주고 첫번째 우선 순위로 len(x) 길이 짧은 것 (역순은 -)
- 두번째로 알파벳순 값을 그대로 넣으면 알파벳 순으로 정렬 (sort함수는 문자열도 그대로 정렬)
