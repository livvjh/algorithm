# [잃어버린 괄호](https://www.acmicpc.net/problem/1541)
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

<br>

### 입력
첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

### 출력
첫째 줄에 정답을 출력한다.


### Example Input
```
55-50+40
```
### Example Output
```
-35
```

### Example Input 2
```
10+20+30+40
```
### Example Output 2
```
100
```

## 접근방식
   - 회의 종료시간 기준 정렬하기 (회의 종료 시간이 빨라야 많이 회의를 진행 가능)
   - 반복 돌면서 끝시간에 맞춰 바로 이어질 수 있는 시작시간을 비교 (시작시간을 초기화 0으로 해서 end 시간을 temp 0번째 값으로 할당)
   - 시작시간이 끝시간과 같거나 크면 count + 1, 끝시간을 temp로 설정
   - 국룰 (정렬, 종료 시간 기준 접근)