dt= [5.4 6.2 7.6 8.5]*10^-3;
r=[50.16 100.19 199.91 249.97];
f=50;
omega=50*2*pi;
v=7.5*sqrt(2);
c=0;
H=10;
for j=-25:0.001:25
   for i=1:4
     A(i)=acos(j*r(i)/(omega*v))/omega +dt(i);
   end  
   B=sum(A)/4;
   ds=sqrt(sum((A-B).^2)/4);
    if (ds<H)
       H=ds;
       m=j;
     end 
      
end

m
H
for i=1:4
    F(i)=acos(m*r(i)/(omega*v))/omega+dt(i);
    
end

F