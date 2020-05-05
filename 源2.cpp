#include<stdio.h>
#include<stdlib.h>
#include<Windows.h>
#include<time.h>

// �ṩ�����Ľⷨ�ͷ������Ľⷨ

int s[5] = {5,5,5,5,5};//�ź�����ʾi�ſ��ӱ�i����ѧ��ʹ��  ������û��ʹ��ʱ=5
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
    sem = CreateSemaphore(NULL, 1, 1, "sem");//�ж��Ƿ������Դʱʹ�õ��ź���
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
    printf("%d����ѧ������\n", i);
    while (1) {
        Sleep(30);
        //˼��
        //��Ϣ

        //�������������ǰ�ж��Ƿ�������
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

        //����һ �������� �ƻ���·
        
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
        

        //������
        while (1) {
            if (check(i, (i+4)%5) == 0)
                break;
            else
                Sleep(300);
        }
       
        WaitForSingleObject(chopsticks[(i + 4) % 5], INFINITE);
        pickch(i,(i + 4) % 5);

        //����һ
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
            

        printf("%d����ѧ�ҿ�ʼ�Է�\n", i);
        Sleep(50);//�Է�
        ReleaseMutex(chopsticks[i]);
        putdownch(i,i);
        //Sleep(300);
        ReleaseMutex(chopsticks[(i + 4) % 5]);
        putdownch(i,(i + 4) % 5);
        printf("%d����ѧ�ҷ��¿���\n", i);
        //Sleep(50);


    }
}
int pickch(int n,int i) {
    printf("%d��ѧ�ҳɹ��õ�%d�ſ���\n",n,i);
    s[i] = n;
    return 1;
}
void putdownch(int n,int i) {
    printf("%d��ѧ�ҷ���%d�ſ���\n", n,i);
    s[i] = 5;
    return;
}

//�ж��Ƿ�����
//���1 �����Ҳ�Ŀ���  ���2  �������Ŀ���

//�ж��Ƿ�������  ������������1  ���򷵻�0
int judge() {
    //int flag = 0;
    for (int i = 0;i < 5;i++) {
        if (s[i] == i){//��������
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
//�ⷨ1 �ƻ���·����
void breakCircle(int no,int i,int type) {
    if (type == 1) {//ֻ����һֱ����
        ReleaseMutex(chopsticks[i]);
        s[i] = 5;//5������Ӵ��ڿ���״̬
        printf("����������%d����ѧ�ҷ���%d�ſ���\n", no, i);
    }
    else {//������ֻ����
        ReleaseMutex(chopsticks[i]);
        s[i] = 5;//5������Ӵ��ڿ���״̬
        s[(i + 4) % 5] = 5;
        printf("����������%d����ѧ�ҷ���%d�ź�%d�ſ���\n", no, i,(int)((i+4)%5));
    }
   
}
//�ⷨ�� �������ǰ����Ƿ�ᷢ������  ������������1  ���򷵻�0
int check(int no,int i) {
    WaitForSingleObject(sem, INFINITE);
    int flag = 0;
    s[no] = i;
    if (judge() == 1) {
        s[no] = 5;
        printf("����%d���Ӹ�%d����ѧ�һᷢ���������ܾ�����\n",i,no);
        flag= 1;
    }
    ReleaseSemaphore(sem, 1, NULL);
    return flag;
}