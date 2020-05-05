#include<stdio.h>
#include<stdlib.h>
#include<Windows.h>
#include<time.h>

// 提供死锁的解法和非死锁的解法

int s[5] = {5,5,5,5,5};//信号量表示i号筷子被i号哲学家使用  当筷子没被使用时=5
HANDLE chopsticks[5];
HANDLE philosophers[5];
DWORD WINAPI philosopher(LPVOID no);
DWORD threadID;
HANDLE sem;
void init();
int pickch(int n,int i);
void putdownch(int n,int i);
int check(int, int);
void breakCircle(int, int,int );
int judge();

int main() {
    init();
    sem = CreateSemaphore(NULL, 1, 1, "sem");//判断是否分配资源时使用的信号量
    for (int i = 0;i < 5;i++) {
        philosophers[i] = CreateThread(NULL, 0, philosopher, (LPVOID)i, 0, &threadID);

    }
    
    WaitForMultipleObjects(5, philosophers, true, INFINITE);
}


void init() {
    chopsticks[0] = CreateMutex(NULL, false,"c0");
    chopsticks[1] = CreateMutex(NULL, false,"c1");
    chopsticks[2] = CreateMutex(NULL, false,"c2");
    chopsticks[3] = CreateMutex(NULL, false,"c3");
    chopsticks[4] = CreateMutex(NULL, false,"c4");
    for (int i = 0;i < 4;i++) {
        if (chopsticks[i] == 0)
            printf("fail to create mutex%d\n", i);
    }
}
DWORD WINAPI philosopher(LPVOID no) {
    //OpenMutex(NULL,false,"c0");
    int flag;
    int i = (int)no;
    printf("%d号哲学家入座\n", i);
    while (1) {
        Sleep(30);
        //思考
        //休息

        //方法二分配筷子前判断是否发生死锁
        while (1) {
            if (check(i, i) == 0){
                break;
            }
            else {
                Sleep(300);
            }
                
        }
            

        WaitForSingleObject(chopsticks[i], INFINITE);
        pickch(i,i);

        //方法一 发生死锁 破坏环路
        
        //WaitForSingleObject(sem, INFINITE);
        //flag = 0;
        //if (judge() == 1) {
        //    breakCircle(i, i,1);
        //    flag = 1;
        //}
        //ReleaseSemaphore(sem, 1, NULL);
        ////Sleep(50);
        //if (flag == 1) {
        //    Sleep(500);
        //    //Sleep(30);
        //    continue;
        //}
            
        Sleep(500);
        

        //方法二
        while (1) {
            if (check(i, (i+4)%5) == 0)
                break;
            else
                Sleep(300);
        }
       
        WaitForSingleObject(chopsticks[(i + 4) % 5], INFINITE);
        pickch(i,(i + 4) % 5);

        //方法一
        //WaitForSingleObject(sem, INFINITE);
        //flag = 0;
        //if (judge() == 1) {
        //    breakCircle(i, i,2);
        //    flag = 1;
        //}
        //ReleaseSemaphore(sem, 1, NULL);
        Sleep(50);
        //if (flag == 1) {
        //    Sleep(500);
        //    continue;
        //}
            

        printf("%d号哲学家开始吃饭\n", i);
        Sleep(50);//吃饭
        ReleaseMutex(chopsticks[i]);
        putdownch(i,i);
        //Sleep(300);
        ReleaseMutex(chopsticks[(i + 4) % 5]);
        putdownch(i,(i + 4) % 5);
        printf("%d号哲学家放下筷子\n", i);
        //Sleep(50);


    }
}
int pickch(int n,int i) {
    printf("%d哲学家成功拿到%d号筷子\n",n,i);
    s[i] = n;
    return 1;
}
void putdownch(int n,int i) {
    printf("%d哲学家放下%d号筷子\n", n,i);
    s[i] = 5;
    return;
}

//判断是否死锁
//情况1 都拿右侧的筷子  情况2  都拿左侧的筷子

//判断是否发生死锁  发生死锁返回1  否则返回0
int judge() {
    //int flag = 0;
    for (int i = 0;i < 5;i++) {
        if (s[i] == i){//拿左侧筷子
            if (i == 4)
                return 1;
            continue;
        }
        else
            break;
        
    }
    for (int i = 0;i < 5;i++) {
        if (s[i] == (i + 4) % 5) {
            if (i == 4)
                return 1;
            continue;
        }       
        else
            break;
    }
    return 0;
   
}
//解法1 破坏环路条件
void breakCircle(int no,int i,int type) {
    if (type == 1) {//只拿了一直筷子
        ReleaseMutex(chopsticks[i]);
        s[i] = 5;//5代表筷子处于空闲状态
        printf("发生死锁，%d号哲学家放下%d号筷子\n", no, i);
    }
    else {//拿了俩只筷子
        ReleaseMutex(chopsticks[i]);
        s[i] = 5;//5代表筷子处于空闲状态
        s[(i + 4) % 5] = 5;
        printf("发生死锁，%d号哲学家放下%d号和%d号筷子\n", no, i,(int)((i+4)%5));
    }
   
}
//解法二 分配筷子前检查是否会发生死锁  发生死锁返回1  否则返回0
int check(int no,int i) {
    WaitForSingleObject(sem, INFINITE);
    int flag = 0;
    s[no] = i;
    if (judge() == 1) {
        s[no] = 5;
        printf("分配%d筷子给%d号哲学家会发生死锁，拒绝分配\n",i,no);
        flag= 1;
    }
    ReleaseSemaphore(sem, 1, NULL);
    return flag;
}