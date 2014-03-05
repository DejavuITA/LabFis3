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


R_exp_valle = V_exp_valle./I_exp_valle;
R_exp_monte = V_exp_monte./I_exp_monte;

display("T_teo   -   R_exp_valle   -   R_exp_monte");
[R_teo R_exp_valle R_exp_monte]

##### per le correzioni #####

	# per le misure a monte!
R_eq_amp = [2000,588.8,63.488,63.488,6.395,6.395,6.395]';

	# per le misure a valle!
R_eq_vol = [200000,1000000,1000000,200000,200000,40000,2000]';


		# amperometro a valle del voltmetro
R_corr_valle = (V_exp_valle .* R_eq_vol) ./(R_eq_vol.*I_exp_valle .- V_exp_valle);

		# amperometro a monte del voltmetro
R_corr_monte = (V_exp_monte .- R_eq_amp .* I_exp_monte)./I_exp_monte;

display("R_teo   -   R_corr_valle   -   R_corr_monte");
[R_teo R_corr_valle R_corr_monte]


display("Lampadina");