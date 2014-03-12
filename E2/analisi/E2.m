%vettore resistenze
R=[2992.4 3998.5 3998.4];

%vettore capacità
C=[1.13e-09 73.2e-09 0.226e-06];

%vettore incertezze resistenze
dR=[1 01 1];

%vettore incertezze capacità
dC=[0.05e-09 0.3e-09 0.002e-06];

%vettore tau
tauexp=[3.698e-06 300e-06 920e-06];

%incertezza tauexp
dt=[0.005e-06 2e-06 5e-06];

%voltaggio
V=0.6325;
dV=0.025;

%calcolo tauteo
for i=1:3
tauteo(i)=R(i)*C(i);
end

tauteo

for i=1:3
dtt(i)=sqrt((C(i)*dR(i))^2+(R(i)*dC(i))^2);
end

dtt

for i=1:3
   detau(i)=-tauteo(i)+tauexp(i);
   dt2(i)=sqrt((dtt(i))^2+(dt(i))^2);
   k(i)=detau(i)/dt2(i);
end    

k


%capacità incognita
R2=[5982.6 6979.6 7977.0 8975.3];
dR2=0.1;

%tau misurati
t2=[780e-09 888e-09 1025e-09 1150e-09];
dt2=[10e-09 10e-09 0.01e-06 0.01e-06];

%capacità ed errore

for i=1:4
   C2(i)=t2(i)/R2(i); 
   dC2(i)=sqrt((dt2(i)/R2(i))^2+(dR2*t2(i)/(R2(i))^2)^2); 
end

C2
dC2


w_C2 = 1./(dC2.^2);
mean_pes= sum(w_C2 .* C2)/sum(w_C2)
dmean_pes= 1 / sqrt(sum(w_C2))