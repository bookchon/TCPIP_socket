#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
void error_handling(char *message);

int main(int argc, char *argv[])
{//      char 개수<-- 실행파일 및 포트번호 저장
	int serv_sock; // 서버 소켓의 파일 디스크립터 저장
	int clnt_sock; // 클라이언트 소켓의 파일 디스크립터 저장

	struct sockaddr_in serv_addr; // 서버의 주소 정보 저장
	struct sockaddr_in clnt_addr; // 클라이언트 주소 정보 저장
	socklen_t clnt_addr_size;

	char message[] = "Hello World!";

	if(argc!=2)// 실행파일과 포트번호가 있어야 해서 2가 되어야 함
	{
		printf("Usage : %s <port> \n", argv[0]); // argv[0] = 실행파일 명
		exit(1); // 종료
	}

	serv_sock = socket(PF_INET, SOCK_STREAM, 0); // IPV4, TCP TYPE, 0값 전달
	if(serv_sock == -1) // 소켓함수가 정상적으로 생성하지 못하면
		error_handling("socket() error"); // 소켓 에러 알림

	memset(&serv_addr, 0, sizeof(serv_addr)); // memset 구조체 멤버0으로 초기화(serv_addr)
	serv_addr.sin_family = AF_INET; // 주소 랜덤 초기화(상수값) IPv4
	serv_addr.sin_addr.s_addr = htonl(INADDR_ANY); // htonl로 바꿔서 저장
	serv_addr.sin_port = htons(atoi(argv[1])); // htons 네트워크 형태로 바꿔서 저장

	if(bind(serv_sock, (struct sockaddr*) &serv_addr, sizeof(serv_addr)) == -1)
	 // sockaddr 구조체  주소정보를 소켓에다 집어넣어서 초기화
		error_handling("bind_() error!");

	if(listen(serv_sock, 5) == -1) // 5 = 연결요청 대기큐를 다섯개까지 받을 수 있음
	 	error_handling("listen() error!");

	 clnt_addr_size = sizeof(clnt_addr);
	 clnt_sock = accept(serv_sock, (struct sockaddr*)&clnt_addr, &clnt_addr_size);
		// 클라이언트 주소 정보를 저장해주고 있음(sockaddr 에 clnt_addr 주소정보 저장 후 sockaddr를 struct로 형변환
	 if(clnt_sock == -1) // 실패 시 -1 값을 리턴함
	 	error_handling("accept() error");

	 write(clnt_sock, message, sizeof(message));
	 close(clnt_sock);
	 close(serv_sock);
	 return 0;
}

void error_handling(char *message)
{
	fputs(message, stderr);
	fputc('\n', stderr);
	exit(1);
}	
