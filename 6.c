module sipo_shift_register_design(input clk,b,output[3:0]q); 
d_ff dut1(.clk(clk),.d(b),.q(q[3]),.rst()); 
d_ff dut2(.clk(clk),.d(q[3]),.q(q[2]),.rst()); 
d_ff dut3(.clk(clk),.d(q[2]),.q(q[1]),.rst()); 
d_ff dut4(.clk(clk),.d(q[1]),.q(q[0]),.rst()); 
endmodule
// d flip flop
module d_ff ( 
 input clk, 
 input d, 
 input rst, 
 output reg q); 
 always @(posedge clk) 
 begin
 if (rst) 
 q <= 1'b0; 
 else
 q <= d; 
 end
endmodule 
testbench
;()module sipo_tb
;reg clk,b
;wire [3:0]q
;sipo_shift_register_design uut(.clk(clk),.b(b),.q(q))
initial
begin
;clk=1'b0
;forever #5clk=~clk
end
initial
begin
;monitor("clk=%d,b=%d,q=%d",clk,b,q)$
end
initial
begin
;b=1
;10#
;b=0
;10#
;b=1
;10#
;b=0
;50#
;finish$
end





///PISO
module piso_design(input clk,sl,input[3:0]b,output q); 
wire w1,w2,w3,w4,w5,w6,w7; 
wire o1,o2,o3; 
d_ff d0(.clk(clk),.d(b[0]),.q(w1),.rst()); 
ao a1(.a(w1),.b(sl),.c(sl),.d(b[1]),.z(o1)); 
d_ff d1(.clk(clk),.d(o1),.q(w4),.rst()); 
ao a2(.a(w4),.b(sl),.c(sl),.d(b[2]),.z(o2)); 
d_ff d2(.clk(clk),.d(o2),.q(w7),.rst()); 
ao a3(.a(w7),.b(sl),.c(sl),.d(b[3]),.z(o3)); 
d_ff d3(.clk(clk),.d(o3),.q(q),.rst()); 
endmodule
// d flip flop
module d_ff ( 
 input clk, // clock input
 input d, // data input
 input rst, // asynchronous reset input
 output reg q // output
); 
 always @(posedge clk) 
 begin
 if (rst) // asynchronous reset
 q <= 1'b0; 
 else // normal operation
 q <= d; 
 end
endmodule
//test bench 
;()module piso_tb
;reg [3:0]b 
;reg clk,sl 
;wire q 
;piso_design dut(clk,sl,b,q) 
initial begin 
;clk=1'b0 
;forever #5 clk=~clk 
end 
initial begin 
;sl=0;b=4'b0101
;sl=1 20# 
;sl=1 20# 
;sl=0 10# 
;sl=0;//b=4'b0110 10# 
;finish$ 100# 
end 
endmodule