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
	dV_exp_monte = dat_R(:,7);#./sqrt(12); ## <<-- questi non vanno bene perché non si tratta di errore statistico, ma di risoluzione
I_exp_monte = dat_R(:,4);
	dI_exp_monte = dat_R(:,5);#./sqrt(12);

V_exp_valle = dat_R(:,10);
	dV_exp_valle = dat_R(:,11);#./sqrt(12);
I_exp_valle = dat_R(:,8);
	dI_exp_valle = dat_R(:,9);#./sqrt(12);

# valori NON corretti
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

dR_corr_valle = R_eq_vol.^2.* (R_eq_vol.*I_exp_valle .- V_exp_valle).^(-2) .* sqrt(	(dV_exp_valle.*I_exp_valle).^2 .+ (dI_exp_valle.*V_exp_valle).^2);

		# amperometro a monte del voltmetro
R_corr_monte = (V_exp_monte .- R_eq_amp .* I_exp_monte)./I_exp_monte;

dR_corr_monte = (I_exp_monte).^(-1) .* sqrt( dV_exp_monte.^2 .+ (dI_exp_monte.* (V_exp_monte)./I_exp_monte).^2);


display("R_teo   -   R_corr_valle   -   R_corr_monte");
[R_teo R_corr_valle R_corr_monte]

# scarti di R
scar_Rm = (R_teo .- R_corr_monte)./R_teo * 100;
	dscar_Rm = dR_corr_monte.*100./R_teo;
scar_Rv = (R_teo .- R_corr_valle)./R_teo * 100;
	dscar_Rv = dR_corr_valle.*100./R_teo;

display("Lampadina");

# dati lampadina da plottare

V_lamp_monte = dat_lamp_monte(:,3);
	dV_lamp_monte = dat_lamp_monte(:,4);
I_lamp_monte = dat_lamp_monte(:,1);
	dI_lamp_monte = dat_lamp_monte(:,2);

V_lamp_valle = dat_lamp_valle(:,3);
	dV_lamp_valle = dat_lamp_valle(:,4);
I_lamp_valle = dat_lamp_valle(:,1);
	dI_lamp_valle = dat_lamp_valle(:,2);

clear dat_R dat_lamp_monte dat_lamp_valle

Pm = 0.562320
V_lamp_log_monte = log(V_lamp_monte);
I_lamp_log_monte = log(I_lamp_monte);
	dV_lamp_log_monte = (dV_lamp_monte./V_lamp_monte);
	dI_lamp_log_monte = (dI_lamp_monte./I_lamp_monte);
	dy = sqrt(dI_lamp_log_monte.^2 + Pm^2 .* dV_lamp_log_monte.^2);
	w = dy .^ (-2);
[A, B, sA, sB] = fit(I_lamp_log_monte,V_lamp_log_monte, w)
chiM = chi2(I_lamp_monte, V_lamp_monte, sqrt(dI_lamp_monte.^2 .+ A*B.*(V_lamp_monte).^(B-1).*dV_lamp_monte.^2), A, B)
sqrt(dI_lamp_monte.^2 .+ A*B.*(V_lamp_monte).^(B-1).*dV_lamp_monte.^2)
display("");
Pv = 0.58327
V_lamp_log_valle = log(V_lamp_valle);
I_lamp_log_valle = log(I_lamp_valle);
	dV_lamp_log_valle = (dV_lamp_valle./V_lamp_valle);
	dI_lamp_log_valle = (dI_lamp_valle./I_lamp_valle);
	dy = sqrt(dI_lamp_log_valle.^2 + Pv^2 .* dV_lamp_log_valle.^2);
	w = dy .^ (-2);
[A, B, sA, sB] = fit(I_lamp_log_valle,V_lamp_log_valle, w)
chiV = chi2(I_lamp_valle, V_lamp_valle, sqrt(dI_lamp_valle.^2 .+ A*B.*(V_lamp_valle).^(B-1).*dV_lamp_valle.^2), A, B)
display("");
sqrt(dI_lamp_valle.^2 .+ A*B.*(V_lamp_valle).^(B-1).*dV_lamp_valle.^2)