		
CYLS 	EQU 	10		;10个柱面		
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
		mov AX,0			 ;初始化寄存器
		mov SS,AX
		mov SP,0x7c00
		mov DS,AX
		
;读磁盘		
		mov AX,0x0820
		mov ES,AX
		mov CH,0			 ;柱面0
		mov DH,0			 ;磁头0
		mov CL,2			 ;扇区2
readloop:
		mov SI,0			 ;记录失败次数的寄存器
retry:
		mov AH,0x02			 ;AH=0x02,读入磁盘
		mov AL,1			 ;1个扇区
		mov BX,0			 
		mov DL,0x00			 ;A驱动器
		INT 0x13			 ;调用磁盘BIOS
		JNC	next			 ;没出错的话就跳转到next
		ADD SI,1			 ;往SI加1
		CMP SI,5			 ;比较SI与5   为啥要和5b比较
		JAE error			 ;SI>=5时，跳转到error
		mov AH,0x00
		mov	DL,0x00			 ; A驱动器
		INT 0x13			 ;重置驱动器
		JMP retry
next:
		mov AX,ES			 ;把内存地址后移0x200
		ADD AX,0x0020
		mov ES,AX			 ;因为没有ADD ES,0x020指令
		ADD CL,1			 ;往CL加1
		CMP CL,18			 ;CL与18比较
		JBE readloop		 ;如果CL<=18,跳转至readloop
		mov CL,1
		ADD DH,1
		CMP DH,2
		JB readloop			 ;如果DH<2,则跳转到readloop
		mov DH,0
		ADD CH,1
		CMP CH,CYLS
		JB readloop			 ;如果CH<CYLS,则跳转到readloop
fin:
		HLT					 ;让CPU停止，等待指令
		JMP fin
error:
		mov SI,msg	
putloop:
		mov AL,[SI]
		ADD SI,1
		CMP AL,0			 
		JE fin
		mov AH,0x0e			 ;显示一个文字   ？？？
		mov BX,15			 ;指定字符颜色
		INT 0x10			 ;调用显卡BIOS
		JMP putloop

msg:  
		DB 0x0a,0x0a		 
		DW "load error"
		DB 0x0a
		DB 0
		RESB 0x7dfe-$
		DB 0x55,0xaa
		
		