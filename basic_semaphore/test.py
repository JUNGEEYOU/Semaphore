import threading
import time

# 세마포 객체 생성. 한번에 실행될 쓰레드를 3개로 제한
sem = threading.Semaphore(3)

def run_semaphore():
    sem.acquire()
    print("세마포어 테스트 진행중 ")     # 여기가 3개의 쓰레드 존재
    time.sleep(2)
    sem.release()


threads = []
# 생성할 쓰레드 개수. 여기서는 10개의 쓰레드를 생성한다.
for num in range(10):
    thread = threading.Thread(target=run_semaphore)
    threads.append(thread)

for th in threads:
    th.start()  # 쓰레드 시작

for th in threads:
    th.join()  # 종료대기

print('Finish All Threading ')
