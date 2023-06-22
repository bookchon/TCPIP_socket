# TCPIP_socket
TCPIP socket programming

## 1일차
	- 네트워크 프로그래밍과 소켓의 이해
		- 리눅스 기반 파일 조작
		- 윈도우 기반 구현
	
	- 소켓 타입과 프로토콜 설정
		- 데이터 저농 특성(TCP, UDP)
	
	- 주소체계 및 데이터 정렬
		- 소켓 할당 IP 주소 및 PORT 번호 확인

## 2일차
	- 주소체계 및 데이터 정렬
		- 바이트 순서의 변환(endian)
		- 인터넷 주소 초기화 및 할당
	
	- TCP 기반 서버 / 클라이언트
		- TCP, UDP 이해(socket, bind, listedn, accept)

## 3일차
	- TCP 기반 서버 / 클라이언트
		- echo server 연결 정보 출력
		- 계산기 서버 및 클라이언트 서버 생성 및 출력
		- TCP 송신이론 및 동작원리
	
	- UDP 기반 서버 / 클라이언트
		- UDP 소켓 확인 및 내부 동작원리 확인
		- UDP 기반 서버 및 클라이언트 구현
			- 에코 서버 및 에코 클라이언트 구현 및 실행
			
	- 소켓 연결 정보
		- 우아한 종료
			- Half close(shutdown함수)
				- Half close 기반의 파일 전송 프로그램 서버 생성