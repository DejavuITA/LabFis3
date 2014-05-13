clear Local user variables;

source("../../algoritmi/utils.m");

Ib = csvread("../dati/circ1.csv")(3:15, 1);
Ic = csvread("../dati/circ1.csv")(3:15, 2);
Ic = Ic .- Ib;
dIb = Ib./50;
dIc = Ic./50;

%w = ones(length(Ic)-10,1).*0.01^(-2);
w = dIb.^(-2);

[A, B, sA, sB] = fit(Ic, Ib, w) % w = dy^(-2)

display("");