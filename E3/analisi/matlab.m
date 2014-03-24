%%Passa basso
%Valore teorico di taglio:
R=997.81;
dR=0.01;
C=161*10^(-9);
dC=2*10^(-9);
f_b=1/(2*pi*R*C)
df_b=sqrt((1/(2*pi*C*R^2)*dR)^2+(1/(2*pi*(C^2)*R)*dC)^2)


%%Reiezione di banda
L=1E-3;
dL=0.01E-3;
C2=250.40E-9;
dC2=0.1E-9;
R_L=2.41;
f_r=1/(2*pi*sqrt(L*C2))
df_r=1/(2*pi)*sqrt((0.5*(L*C2)^(-1.5)*C2*dL)^2+(0.5*(L*C2)^(-1.5)*L*dC2)^2)

%%Passa banda
%valori uguali alla REIEZIONE DI BANDA





