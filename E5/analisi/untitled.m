m50=sum(ohm50)/length(ohm50);
m100=sum(ohm100)/length(ohm100);
m200=sum(ohm200)/length(ohm200);
m250=sum(ohm250)/length(ohm250)

dm50=sqrt((sum((m50-ohm50).^2))/(length(ohm50)));
dm100=sqrt((sum((m100-ohm100).^2))/(length(ohm100)));
dm200=sqrt((sum((m200-ohm200).^2))/(length(ohm200)));
dm250=sqrt((sum((m250-ohm250).^2))/(length(ohm250)))