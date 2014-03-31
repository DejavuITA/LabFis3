

for i=1:32
Fase1(i)=Fase(i)*pi/180;
%phi2(i)=atan(V1(i)*sin(Fase1(i))/(V1(i)*cos(Fase1(i))-V2(i)))*180/pi;
phi(i)=asin(V1(i)/VM(i)*sin(Fase1(i)))*180/pi;
end

dV1_=10^-3;
dV2_=10^-3;
dVM_=10^-3;
dFase=0.01*pi/180;

for i=1:32
   V1_(i)=V1(i)*10^(-3);
   V2_(i)=V2(i)*10^(-3);
   VM_(i)=VM(i)*10^(-3);
   
   dphi(i)= sqrt((V1_(i)*cos(Fase1(i))/VM_(i)*(dFase))^2+ (sin(Fase1(i))\VM_(i)*(dV1_))^2+ (V1_(i)*sin(Fase1(i))\VM_(i)*(dVM_))^2);
   
end