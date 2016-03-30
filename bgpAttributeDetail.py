#class bgpAttribute_detail:
def origin(originData,length):
	originType={0x00:'IGP',0x01:'EGP',0x02:'INCOMPLETE'}		
	return  {'Origin':originType[int(originData[0:length*2],16)]}
def aspath(aspathData,length):
	aspathporint=0
	aspathType={0x00:False,0x01:'AS_SET',0x02:'AS_SEQUENCE',0x03:'AS_CONFED_SEQUENCE',0x04:'AS_CONFED_SET'}
	PathsegmentType=aspathType[int(aspathData[aspathporint:(aspathporint+1)*2],16)]
	
	if(PathsegmentType==False):return {'aspath':'Empty'}
	aspathporint+=1
	PathsegmentLength=int(aspathData[aspathporint*2:(aspathporint+1)*2],16)
	aspathporint+=1
	PathsegmentValue=''
	for i in range(aspathporint,aspathporint+PathsegmentLength,1):
		PathsegmentValue+=str(int(aspathData[i*2:(i+4)*2],16))+' '
	return {'PathType':PathsegmentType,'PathLength':PathsegmentLength,'PathValue':PathsegmentValue}
def nexthop(nexthopData,length):
	next_hop=''
	for i in range(0,length,1):
		if i%4==0:
			next_hop+=' '+str(int(nexthopData[i*2:(i+1)*2],16))
		else :
			next_hop+='.'+str(int(nexthopData[i*2:(i+1)*2],16))
	return {'next_hop':next_hop}
def med(medData,length):
	return {'med':int(medData[0:length*2],16)}
def localpreference(localpreferenceData,length):
	return {'local_pref':int(localpreferenceData[0:length*2],16)}
def atomicaggregate(atomicaggregateData,length):
	atomicaggregateValue=''
	for i in range(0,length,1):
		if i%4==0:
			atomicaggregateValue+=' '+str(int(atomicaggregateData[i*2:(i+1)*2],16))
		else :
			atomicaggregateValue+='.'+str(int(atomicaggregateData[i*2:(i+1)*2],16))
	return {'atomicaggregate':atomicaggregateValue}
def aggregator(aggregatorData,length):
	aggregatorValue=''
	for i in range(0,length,1):
		if i%4==0:
			aggregatorValue+=' '+str(int(aggregatorData[i*2:(i+1)*2],16))
		else :
			aggregatorValue+='.'+str(int(aggregatorData[i*2:(i+1)*2],16))
	return {'aggregator':aggregatorValue}
def community(communityData,length):
	communityValue=''
	for i in range(0,length/2,1):
		if i%2==0:
			communityValue+=str(int(communityData[i*4:(i+1)*4],16))+':'
		else :
			communityValue+=str(int(communityData[i*4:(i+1)*4],16))+' '
	return {'community':communityValue}
def originatorid(originatoridData,length):
	originatoridValue=''
	for i in range(0,length,1):
		if i%4==0:
			originatoridValue+=' '+str(int(originatoridData[i*2:(i+1)*2],16))
		else :
			originatoridValue+='.'+str(int(originatoridData[i*2:(i+1)*2],16))
	return {'originatorid':originatoridValue}
def clusterlist(clusterlistData,length):
	clusterlistValue=''
	for i in range(0,length,1):
		if i%4==0:
			clusterlistValue+=' '+str(int(clusterlistData[i*2:(i+1)*2],16))
		else :
			clusterlistValue+='.'+str(int(clusterlistData[i*2:(i+1)*2],16))
	return {'clusterlist':clusterlistValue}
def mpreachnlri(originData,length):
	return {'mpreachnlri':0}
def mpunreachnlri(originData,length):
	return {'mpunreachnlri':0}
def extendedcommunity(extendedcommunityData,length):
	extendedcommunityDataValue=''
	for i in range(0,length/2,1):
		if i%2==0:
			extendedcommunityDataValue+=str(int(extendedcommunityData[i*4:(i+1)*4],16))+':'
		else :
			extendedcommunityDataValue+=str(int(extendedcommunityData[i*4:(i+1)*4],16))+' '
	return {'community':extendedcommunityDataValue}
def as4path(as4pathData,length):
	return {'as4path':as4path[0:length*2]}
def as4aggregator(as4aggregatorData,length):
	return {'as4aggregator':as4aggregatorData[0:length*2]}
def pmsitunnel(pmsitunnelData,length):
	return {'pmsitunnel':pmsitunnelData[0:length*2]}
def tunnelencaps(tunnelencapsData,length):
	return {'tunnelencaps':tunnelencapsData[0:length*2]}
def aigp(originData,length):
	aigpFlagDict={0:'No tunnel',1:'RSVP-TE P2MP LSP',2:'mLDP P2MP LSP',3:'PIM-SSM Tree',4: 'PIM-SM Tree',5: 'BIDIR-PIM Tree',6:'Ingress Replication',7:'mLDP MP2MP LSP'}
	if length<6: 
		return {'aigp':originData} 
	aigpFlag=originData[0:2]
	if int(originData[0:2],16)<8:
		aigpType=aigpFlagDict[int(originData[0:2],16)]
	else:
		aigpType=originData[2:4]
	MPLSLabel=int(originData[4:10],16)
	TunnelIdentifier=int(originData[10:length*2],16)
	return {'aigpFlag':aigpFlag,'aigpType':aigpType,'MPLSLabel':MPLSLabel,'TunnelIdentifier':TunnelIdentifier}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	