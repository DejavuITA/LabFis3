clear Local user variables;

source("/home/dejavu/Documents/Secondo\ Anno/Optoelettronica/algoritmi/utils.m");

Volt = -csvread("/home/dejavu/Documents/Secondo\ Anno/Optoelettronica/E7/dati/E6.csv")(3:(end), 1);
Amp = -csvread("/home/dejavu/Documents/Secondo\ Anno/Optoelettronica/E7//dati/E6.csv")(3:(end), 2);

w = ones(length(Volt)-10,1).*0.01^(-2);

[A, B, sA, sB] = fit(Amp(11:end), Volt(11:end), w) % w = dy^(-2)

display("");

Vin = csvread("/home/dejavu/Documents/Secondo\ Anno/Optoelettronica/E7//dati/E6_zener.csv")(3:(end), 1);
Vout = csvread("/home/dejavu/Documents/Secondo\ Anno/Optoelettronica/E7//dati/E6_zener.csv")(3:(end), 2);

wz = ones(length(Vin)-10,1).*0.01^(-2);

[Av, Bv, sAv, sBv] = fit(Vout(11:end), Vin(11:end), wz) % w = dy^(-2)
