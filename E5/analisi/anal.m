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
	C = i*0.01/w/V0;
	
	for j = 1:100000
		Tau = j*10^-6;
		for l = 1:4
			At(l,1) = acos(C.*w.*V0./Ohm(l,1)) + Tau - T;
		endfor
	
		ki = sqrt( (1/4) .* sum( (At.-Delta_t).^2) );
	
		if (ki<k	)
			k = ki;
			ki = i;
			kj = j;
		endif
	endfor
endfor

kTau = kj*10^-6;
kC = i*0.01/w/V0;
[i j]
[k kTau kC]