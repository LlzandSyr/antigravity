	.file	"C:\\Users\\86135\\.gemini\\antigravity\\brain\\4db8a194-36a7-43c2-9998-3f6b805866f9\\scratch\\compilation_stages_demo.c"
	.text
	.globl	g_flag
	.data
	.align 4
g_flag:
	.long	1
	.def	__main;	.scl	2;	.type	32;	.endef
	.text
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$48, %rsp
	.seh_stackalloc	48
	.seh_endprologue
	call	__main
	movl	$10, -4(%rbp)
	movl	-4(%rbp), %edx
	movl	%edx, %eax
	sall	$2, %eax
	addl	%edx, %eax
	movl	%eax, -8(%rbp)
	nop
.L2:
	movl	g_flag(%rip), %eax
	cmpl	$1, %eax
	je	.L2
	movl	$0, %eax
	addq	$48, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.ident	"GCC: (GNU) 9.3.0"
