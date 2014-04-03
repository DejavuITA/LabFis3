clear Local user variables;

source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

Ohm = csvread("../dati/tau.csv")(2:(end), 1);
Delta_t = csvread("../dati/tau.csv")(2:(end), 2);

f = 50;
T=1/f;
w=2*pi*f;
V0 = 7.5*sqrt(2);

% At = acos(C.*w.*V0./Ohm) + Tau - T;
k = 10^10;
for i = 1:100	
	for j = 1:500
		Tau = j*10^-4;
		for l = 1:4
			C = i*0.01/w/V0*Ohm(l,1);
			At(l,1) = acos(C) + Tau - T;
		endfor
	
		khi = sqrt( (1/4) .* sum( (At.-Delta_t).^2) );
	
		if ( khi<k )
			k = khi;
			ki = i;
			kj = j;
		endif
	endfor
endfor

kTau = kj*10^-4;
kC = ki*0.01;
[ki kj]
[k kTau kC]