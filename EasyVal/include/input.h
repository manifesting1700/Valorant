#ifndef _I_H_ #define _I_H_ #define _DINPUT_V 0x800 #include <d3d9.h> #include <dinput.h> #pragma comment(lib, "dinput8.lib") #pragma comment(lib, "dxguid.lib") class I { public: void i(HWND h); void u(); bool k(int j) { return !(m.rgbButtons[j] & 0x80); } bool d(int j) { return (m.rgbButtons[j] & 0x80); } bool s() { return m.lZ > 0; } bool r() { return m.lZ < 0; } private: LPDIRECTINPUTDEVICE8 d; LPDIRECTINPUT i; DIMOUSESTATE2 m; }; extern I _i; #endif //_I_H_
