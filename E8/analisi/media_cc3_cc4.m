clear Local user variables;

source("../../algoritmi/utils.m");

A = csvread("../dati/scope_4_2.csv")(3:(end), 2);
B = csvread("../dati/scope_4_2.csv")(3:(end), 3);

display("");

M=sum(A.-B)/length(A)

dM=sqrt((sum(M.-(A.-B))).^2/length(M))