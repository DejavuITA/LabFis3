clear Local user variables;

source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

dat_R = csvread("../dati/resistenze.csv")(2:(end), 1:(end));
dat_lamp_monte = csvread("../dati/lampadina_monte.csv")(2:(end), 2:(end));
dat_lamp_valle = csvread("../dati/lampadina_valle.csv")(2:(end), 2:(end));

display("");

R_exp_monte = dat_R(:,6)./dat_R(:,4)
R_exp_valle = dat_R(:,10)./dat_R(:,8)