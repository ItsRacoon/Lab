module ALU(x,y,sel,z); 
input [7:0]x,y; 
output reg [15:0]z; 
input [2:0]sel; 
parameter ADD=3'b000; 
parameter SUB=3'b001; 
parameter MUL=3'b010; 
parameter DIV=3'b011; 
parameter AND=3'b100; 
parameter OR=3'b101; 
parameter NOT1 =3'b110; 
parameter NOT2 =3'b111; 
always@(*) 
case(sel) 
ADD: z=x+y; 
SUB: z=x-y; 
MUL: z=x*y; 
DIV: z=x/y; 
AND: z=x&y; 
OR: z=x|y; 
NOT1: z=!x; 
NOT2: z=!y; 
endcase 
endmodule