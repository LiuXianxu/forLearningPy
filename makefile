ipl.bin : ipl.nas Makefile
	nask.exe ipl.nas ipl.bin ipl.lst
helloos.img : ipl.bin Makefile
	edimg.exe   imgin:F:\A1\tolset\z_tools\fdimg0at.tek  \
	 wbinimg src:ipl.bin len:512 from:0 to:0   imgout:helloos.img
img :
	make.exe -r helloos.img
asm :
	make.exe -r ipl.bin 
run :
	make.exe img
	copy helloos.img F:\A1\tolset\z_tools\qemu\fdimage0.bin
	make.exe	-C F:\A1\tolset\z_tools\qemu
install :
	make.exe img
	imgtol.com w a: helloos.img
	