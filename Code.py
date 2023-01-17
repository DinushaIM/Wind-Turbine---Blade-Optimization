import cmath
n=1;
(a0,b0)=(0.0,0.0);
phy = cmath.atan((1-a0)/(7*(1-b0)));
stp_1 = 3*0.4915*(1-a0)**2;
Ct =(stp_1*(0.933*cmath.cos(phy)+0.0153*cmath.sin(phy)))/(2*cmath.pi*1.2704*(cmath.sin(phy))**2);
Cq =(stp_1*(0.933*cmath.sin(phy)-0.0153*cmath.cos(phy)))/(cmath.pi*1.2704*(cmath.sin(phy))**2);

print (Ct)


a1 = 0.5+0.5*((1-Ct)**(0.5))#or 0.5+0.5*((1-Ct)**(0.5))

b1 = Cq/(56*(1-a1));

print (a0,b0,a1,b1)

while n==1:
    if abs(a1-a0)<0.0001 and abs(b1-b0)<0.0001 or a1 > 0.4:
        break
    
#    if abs(b1-b0)<0.0001:
#        break

    else:
        a0=a1;
        b0=b1;
        phy = cmath.atan((1-a0)/(7*(1-b0)));
        stp_1 = 3*0.4915*(1-a0)**2;
        Ct =(stp_1*(0.933*cmath.cos(phy)+0.0153*cmath.sin(phy)))/(2*cmath.pi*1.2704*(cmath.sin(phy))**2);
        Cq =(stp_1*(0.933*cmath.sin(phy)-0.0153*cmath.cos(phy)))/(cmath.pi*1.2704*(cmath.sin(phy))**2);

        print (Ct)

        a1 = 0.5+0.5*((1-Ct)**(0.5))#or 0.5+0.5*((1-Ct)**(0.5))
        
        b1 = Cq/(56*(1-a1));
        print (a0,b0,a1,b1)
  
print (a0,b0,a1,b1)

#CHECKING THE VALUES

(Ct_BE,Cq_BE)=(0,0)

Ct_BE = Ct
Cq_BE = Cq

Ct_ME = 4*a0*(1-a0)
Cq_ME = 56*b0*(1-a0)

print('Ct_BE =',Ct_BE,'Cq_BE =',Cq_BE)
print('Ct_ME =',Ct_ME,'Cq_ME =',Cq_ME)
