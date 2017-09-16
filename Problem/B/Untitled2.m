
data = xlsread("Appendix-1.xls");
data_location = data(:,1:2);
[num,text,raw]=xlsread("Appendix-2.xlsx");
R = regexp(text(2:length(text),2)," ","split");
usrGeo = zeros(length(R),2);
for t=1:length(R)
    usrGeo(t,1) = str2double(R{t}{1});
    usrGeo(t,2) = str2double(R{t}{2});
end
usrGeo(1175,:)=[];
scatter(data_location(:,1),data_location(:,2),'o');
hold all
scatter(usrGeo(:,1),usrGeo(:,2),'ok');