RC=9972;
RE=(118.4+119.4)/2;
R1=9933;
Gdiff=9.060/0.301;
dRC=2;
dR1=2;
dRE=(-118.4+119.4)/2;
dGdiff=sqrt((1/301)^2*100 +(9060/(301)^2)^2);

re1=RC/(2*Gdiff)-RE;
dre1=sqrt((1/(2*Gdiff))^2*dRC^2+     dRE^2+   (-(RE/Gdiff) - (RC - 2*Gdiff*RE)/(2*Gdiff^2))^2*dGdiff^2);


Gc=145/300;
dGc=sqrt((1/300)^2+(145/(300)^2)^2);

re2= RC/Gc-2*R1-RE;
dre2=sqrt((1/Gc)^2*dRC^2+   (RC/(Gc)^2)^2*dGc^2+ (2)^2*dR1^2+  (1)^2*dRE^2);



CMMR=Gdiff/Gc;
dCMMR=sqrt((1/Gc)^2*dGdiff^2 +(Gdiff/(Gc)^2)^2*dGc^2);

CMt=R1/(RE+re1);

I=(15*10/43-0.6)/1500
