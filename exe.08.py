medida=float (input('Digite uma medida em metros:'))
centi=medida*100
milim=medida*1000
#print('A medida em centimetros e:', centi,'cm', 'e a medida em milimetros e:', milim, 'mm')
print('A medida de {}m em centimetros e: {:.0f} cm e a medida em milimetros e: {:.0f} mm'.format(medida,centi,milim))