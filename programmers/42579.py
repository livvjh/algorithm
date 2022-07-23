"""
https://programmers.co.kr/learn/courses/30/lessons/42579?language=python3#
문제명: 베스트 앨범

문제 포인트
- 정렬 순서 (내림차순)
    - 많이 재생 장르
    - 많이 재생 노래
    - 동일할 때 고유 번호가 낮은 노래 우선 순위

풀이 접근 방법
1. dict를 이용해 key값으로 구분하고 sum한 값을 구하기
2. sum한 값의 우선 순위 정하기
3. key값을 기준으로 빈배열에 2개씩 넣기
"""


def solution(genres, plays):
    best_album = {}
    total_sum = {}
    for i in range(len(plays)):
        album_info = {
            "index": i,
            "point": plays[i]
        }
        if best_album.get(genres[i]):
            total_sum[genres[i]] += plays[i]
            best_album[genres[i]].append(album_info)
        else:
            total_sum[genres[i]] = plays[i]
            best_album[genres[i]] = [album_info]
    # fail point -> target을 직접 정해줘야함 sorted 할 타겟
    # sorted_total_sum = sorted(total_sum.items(), reverse=True)
    sorted_total_sum = sorted(total_sum.items(), key=lambda item: item[1], reverse=True)
    result = []
    for key, _ in sorted_total_sum:
        genre_list = sorted(best_album[key], key=lambda album: -album['point'])
        result += [genre['index'] for genre in genre_list][:2]
    return result


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

# sexy code
# def solution(genres, plays):
#     answer = []
#     d = {e:[] for e in set(genres)}
#     for e in zip(genres, plays, range(len(plays))):
#         d[e[0]].append([e[1] , e[2]])
#     genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
#     for g in genreSort:
#         temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
#         answer += temp[:min(len(temp),2)]
#     return answer
