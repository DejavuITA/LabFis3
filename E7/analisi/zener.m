clear Local user variables;

source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

Volt = -csvread("../dati/E6.csv")(3:(end), 1);
Amp = -csvread("../dati/E6.csv")(3:(end), 2);

w = ones(length(Volt)-10,1).*0.01^(-2);

[A, B, sA, sB] = fit(Amp(11:end), Volt(11:end), w) % w = dy^(-2)

display("");

Vin = csvread("../dati/E6_zener.csv")(3:(end), 1);
Vout = csvread("../dati/E6_zener.csv")(3:(end), 2);

wz = ones(length(Vin)-10,1).*0.01^(-2);

[Av, Bv, sAv, sBv] = fit(Vout(11:end), Vin(11:end), wz) % w = dy^(-2)