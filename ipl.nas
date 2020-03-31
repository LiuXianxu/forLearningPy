		
		
		ORG		0x7c00	;指明程序的装载地址
;记述用于标准FAT12格式的软盘	

	
		JMP		entry
		DB		0x90
		DB		"HARIBOTE"   ;启动区的名称可以是任意8字节的字符串
		DW		512			 ;每个扇区的大小(必须是512字节)   有疑问：DW分配的不是16字节吗？
		DB		1			 ;簇(cluster)的大小(必须是1个扇区)
		DW		1			 ;FAT的起始位置(一般从第一个扇区开始)
		DB		2			 ;FAT的个数(必须为2）		
		DW		224			 ;根目录的大小(一般设成224项)
		DW		2880		 ;该磁盘的大小(必须是2880扇区)
		DB		0xf0		 ;磁盘的种类(必须是0xf0)
		DW		9			 ;FAT的长度(必须是9扇区)
		DW		18			 ;1个磁道(track)有几个扇区(必须是18)
		DW		2			 ;磁头数（必须是2）
		DD		0			 ;不使用分区，必须是0
		DD		2880		 ;重写一次磁盘大小
		DB		0,0,0x29	 ;意义不明，固定
		DD		0xffffffff	 ;（可能是）卷标号码
		DB		"HariboteOS" ;磁盘名称（11字节）
		DB		"FAT12   "	 ;磁盘格式名称（8字节）
		RESB	18			 ;先空出18字节

entry:
		mov AX,0
		mov SS,AX
		mov SP,0x7c00
		mov DS,AX
