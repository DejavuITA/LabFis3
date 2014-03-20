clear Local user variables;

source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

dat_low = csvread("../dati/low.csv")(2:(end), 1:4);
dat_bpf = csvread("../dati/bpf.csv")(2:(end), 1:4);
dat_notch = csvread("../dati/notch.csv")(2:(end), 1:4);

display("");

db_low = 20*log10(dat_low(1:(end),2)./dat_low(1:(end),1))
db_bpf = 20*log10(dat_bpf(1:(end),2)./dat_bpf(1:(end),1))
db_notch = 20*log10(dat_notch(1:(end),2)./dat_notch(1:(end),1))