clear Local user variables;

source("../../algoritmi/alg1.m");
source("../../algoritmi/utils.m");

dat_R = csvread("../dati/resistenze.csv")(2:(end), 1:(end));
dat_lamp_monte = csvread("../dati/lampadina_monte.csv")(2:(end), 2:(end));
dat_lamp_valle = csvread("../dati/lampadina_valle.csv")(2:(end), 2:(end));

display("");
display("Resistenze");

#dati
R_teo = dat_R(:,3);

V_exp_monte = dat_R(:,6);
	dV_exp_monte = dat_R(:,7);
I_exp_monte = dat_R(:,4);
	dI_exp_monte = dat_R(:,5);

V_exp_valle = dat_R(:,10);
	dV_exp_valle = dat_R(:,11);
I_exp_valle = dat_R(:,8);
	dI_exp_valle = dat_R(:,9);


R_exp_monte = V_exp_monte./I_exp_monte
R_exp_valle = V_exp_valle./I_exp_valle

##### per le correzioni #####

	# per le misure a monte!
R_eq_amp = [1,2,3,4,5,6,7]';

	# per le misure a valle!
#R_eq_vol = [];



# Rx = V Rv /(Rv Ia - V)		# amperometro a valle del voltmetro

# Rx = (V - Ra Ia)/Ia		# amperometro a monte del voltmetro


display("Lampadina");