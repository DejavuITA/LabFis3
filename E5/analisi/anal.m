clear Local user variables;

source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

Ohm = csvread("../dati/tau.csv")(2:(end), 1);
Delta_t = csvread("../dati/tau.csv")(2:(end), 2);

f = 50;
T = 1/f;
w = 2*pi*f

Veff = 7.5;
V0 = Veff*sqrt(2);

Ieff = 26.5*10^(-3);

%modifiche ai dati
Iatt = Ieff*sqrt(2);

%OK = V0/Iatt - 300;
%Ohm = Ohm .+ OK

% calcolo K per ogni resistenza grazie alla corrente di attivazione calcolata nella prima parte dell'esperienza
for i = 1:4
	K(i,1) = V0 .* w ./ Ohm(i,1) .* sin (w * acos( abs(Iatt .* Ohm(i,1) ./ V0) ) );
endfor

K

% ottengo un valore medio di K
Kmed = sum(K)/length(K)
display("");

% calcolo il tempo t* tale per cui la derivata della corrente è sufficientemente alta affinché l'interruttore si apra
for i = 1:4
	t_star(i,1) = 1/w * asin(Kmed .* Ohm(i,1) ./ V0 ./ w);
endfor

t_star

% calcolo il tempo Tau che dovrebbe essere una costante (DOVREBBE)
Tau = T/4 .- t_star .+ Delta_t;

Taumed = sum(Tau)/length(Tau);
sigmaTau = sqrt(sum((Tau .- Taumed).^2)/(length(Tau)-1));

[Taumed*1000 sigmaTau*1000]
%display("");display("");display("");
% metto K in valore assoluto..?

for i = 1:4
	t_star_2(i,1) = 1/w * asin(Iatt .* Ohm(i,1) ./ V0);
endfor

Tau_2 = T/4 .- t_star_2 .+ Delta_t;

Tau_med_2 = sum(Tau_2)/length(Tau_2);
sigmaTau_2 = sqrt(sum((Tau_2 .- Tau_med_2).^2)/(length(Tau_2)-1));

[Tau_med_2*1000 sigmaTau_2*1000]

%errori pt2%
Kmed_2 = Iatt.*w;
dK = sqrt(2)*w*0.3/1000;
dt_star = Ohm./w .*((V0.*w).^2 .-(K.^2).*(Ohm.^2)).^-0.5.*dK;
dTau = sqrt((ones(4,1).*0.0001).^2 .+ dt_star.^2);

%media pesata
wm = weighted_mean(Tau_2, dTau);
we = weighted_mean_err(dTau);
[wm*1000 we*1000]