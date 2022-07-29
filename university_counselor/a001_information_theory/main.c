#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main()
{
	FILE* fp;
	fp = fopen("D:\\英文信源文档.txt","r");
	int d, i = 0, j = 0;
	int p[6000];
	int b, c, add = 0;
	float num[27] = { 0 }, space = 0;
	float t;
	float shang;
	float f[27] = { 0 };
	float M[27][27] = { 0 }, N[27][27] = { 0 };

	if (fp == NULL) {
		printf("打开文件失败\n");
		exit(0);
	}

	while ((d = fgetc(fp)) != EOF) {
		p[i++] = d;
	}

	for (i = 0; p[i] > 0; i++) {
		if (p[i] >= 97) p[i] = p[i] - 32;
	}

	for (i = 0; p[i] > 0; i++) {
		if (p[i] == 32) {
			int g = p[i + 1];
			if (g == 32) {
				M[0][0] = M[0][0] + 1;
			}
			else {
				g = g - 64;
				M[0][g]++;

			}
		}
	}
	for (i = 0; p[i] > 0; i++) {
		if (p[i] != 32) {
			int h, k;
			h = p[i] - 64;
			k = p[i + 1];
			if (k > 0) {
				if (k == 32) { k = 0; }
				else { k = k - 64; }
				M[h][k] = M[h][k] + 1;
			}
		}
	}

	float total = 0;
	for (i = 0; i < 27; i++) {
		for (j = 0; j < 27; j++) {
			total = total + M[i][j];
		}
	}
	for (i = 0; i < 27; i++) {
		for (j = 0; j < 27; j++) {
			N[i][j] = M[i][j];
		}
	}
	float s[27] = { 0 };
	for (j = 0; j < 27; j++) {
		for (i = 0; i < 27; i++) {
			s[j] = s[j] + M[i][j];
		}
	}
	for (i = 0; i < 27; i++) {
		for (j = 0; j < 27; j++) {
			M[i][j] = M[i][j] / total;
		}
	}
	for (j = 0; j < 27; j++) {
		for (i = 0; i < 27; i++) {
			if(s[j]!=0) 
			N[i][j] = N[i][j] / s[j];
		}
	}
	for(i=0;i<27;i++){
	 	for(j=0;j<27;j++){
	 		printf("%f ",N[i][j]);
		 }
		 printf("\n");
	}
	for (i = 0; i < 27; i++) {
		for (j = 0; j < 27; j++) {
			if (N[i][j] != 0) {
				M[i][j] = M[i][j] * log(1 / N[i][j]);
			}
		}
	}

	float Hxy = 0.0;
	for (i = 0; i < 27; i++) {
		for (j = 0; j < 27; j++) {
			Hxy = Hxy + M[i][j];
		}
	}

	printf("信道损失熵为:%f\n", Hxy);
	printf("\n");
	fp = fopen("D:\\英文信源文档.txt","r");

	if (fp == NULL) {
		printf("打开文件失败\n"); exit(0);
	}
	while ((c = fgetc(fp)) != EOF) {
		if (c >= 'a' && c <= 'z') {
			num[c - 'a']++;
		}
		else if (c >= 'A' && c <= 'Z') {
			num[c - 'A']++;
		}
		if (c == 32) {
			space++;
		}
	}
	t = 0; shang = 0;
	for (i = 0; i < 26; i++) {
		t = t + num[i];
	}
	t =t + space;
	
	printf("各字母的概率为：\n");
	for (i = 0; i < 26; i++) {
		f[i] = num[i] / t;
		if (f[i] != 0) printf("P(%c)=%f\n", 97 + i, f[i]);
		if (f[i] == 0) printf("P(%c)=%f\n", 97 + i, 0);
	}
	printf("\n");
	float ps;
	printf("space=%f\n", ps = space / t);
	for (i = 0; i < 27; i++) {
		if (f[i] != 0) shang = shang - f[i] * log(f[i]);
	}
	if (ps != 0) shang -= ps * log(ps);
	printf("\n信息熵为：%f", shang);
	printf("\n");
	fclose(fp);
	float I;
	I = shang - Hxy;
	printf("\n"); 
	printf("平均互信息I(X;Y)为：%f", I);
	fp = fopen("互信息的计算.txt", "a");
	fprintf(fp, "条件熵为：%f \n", Hxy);
	fprintf(fp, "信息熵为：%f \n", shang);
	fprintf(fp, "平均互信息为：%f \n", I);
	fclose(fp);
	return 0;
}
