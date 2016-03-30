"""
HexByteConversion

Convert a byte string to it's hex representation for output or visa versa.

ByteToHex converts byte string "\xFF\xFE\x00\x01" to the string "FF FE 00 01"
HexToByte converts string "FF FE 00 01" to the byte string "\xFF\xFE\x00\x01"
"""

#-------------------------------------------------------------------------------
import pprint
import math
from  bgpAttributeFlag import *
def ByteToHex( byteStr ):
	"""
	Convert a byte string to it's hex string representation e.g. for output.
	"""
	
	# Uses list comprehension which is a fractionally faster implementation than
	# the alternative, more readable, implementation below
	#   
	#    hex = []
	#    for aChar in byteStr:
	#        hex.append( "%02X " % ord( aChar ) )
	#
	#    return ''.join( hex ).strip()        
	
	return ''.join( [ "%s" % x.encode('hex') for x in byteStr ] )

#-------------------------------------------------------------------------------

def HexToByte( hexStr ):
	bytes = []

	hexStr = ''.join( hexStr.split(" ") )

	for i in range(0, len(hexStr), 2):		
		bytes.append( chr( int (hexStr[i:i+2], 16 ) ) )
		#print 'hexStr=%s' % hexStr[i:i+2]
	#print 'hexStr=%s' % bytes
	return ''.join( bytes )

#-------------------------------------------------------------------------------

# test data - different formats but equivalent data
__hexStr1  = "FFFFFF5F8121070C0000FFFFFFFF5F8129010B"
__hexStr2  = "FF FF FF 5F 81 21 07 0C 00 00 FF FF FF FF 5F 81 29 01 0B"
__byteStr = "\xFF\xFF\xFF\x5F\x81\x21\x07\x0C\x00\x00\xFF\xFF\xFF\xFF\x5F\x81\x29\x01\x0B"
EXTENDED_LENGTH = 0x10  # .  16 - 0001 0000
PARTIAL         = 0x20  # .  32 - 0010 0000
TRANSITIVE      = 0x40  # .  64 - 0100 0000
OPTIONAL        = 0x80  # . 128 - 1000 0000

MASK_EXTENDED   = 0xEF  # . 239 - 1110 1111
MASK_PARTIAL    = 0xDF  # . 223 - 1101 1111
MASK_TRANSITIVE = 0xBF  # . 191 - 1011 1111
MASK_OPTIONAL   = 0x7F  # . 127 - 0111 1111
	
Flags={
EXTENDED_LENGTH:'EXTENDED_LENGTH',
PARTIAL:'PARTIAL',
TRANSITIVE:'TRANSITIVE',
OPTIONAL:'OPTIONAL',
MASK_EXTENDED:'MASK_EXTENDED',
MASK_PARTIAL:'MASK_PARTIAL',
MASK_TRANSITIVE:'MASK_TRANSITIVE',
MASK_OPTIONAL:'MASK_OPTIONAL'
}
def community(originData,length):
	communityValue=''
	for i in range(0,length/2,1):
		if i%2==0:
			next_hop+=str(int(originData[i*4:(i+1)*4],16))+':'
		else :
			next_hop+=str(int(originData[i*4:(i+1)*4],16))+' '
	return {'community':communityValue}
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

def Getnlris(nlribody,length):
	nlripoint=0
	ips=[]
	while nlripoint<length :
		mask=int(nlribody[nlripoint*2:(nlripoint+1)*2],16)
		mask_slash=int(math.ceil(mask/8))
		nlripoint+=1
		upnlri=nlribody[nlripoint*2:(nlripoint+mask_slash)*2]
		ip=''
		print '----------'
		print length
		print '%s' % upnlri
		print '++++++++++'
		nlripoint+=mask_slash			
		for i in range(0,mask_slash*2,2):
			if(i==0):
				ip=ip+str(int(upnlri[i:i+2],16))
			else:
				ip=ip+'.'+str(int(upnlri[i:i+2],16))
		for j in range(mask_slash,4,1):			
			ip=ip+'.0 '
		ips.append({'ip':ip,'mask':mask})
	return ips
def aggregator(aggregatorData,length):
	aggregatorValue=''
	for i in range(0,length,1):
		if i%4==0:
			aggregatorValue+=' '+str(int(aggregatorData[i*2:(i+1)*2],16))
		else :
			aggregatorValue+='.'+str(int(aggregatorData[i*2:(i+1)*2],16))
	return {'aggregator':aggregatorValue}
def recive_update(header,body,length):
	Body_strHex=body
	
	
	bodyPoint=0 #UnfeasibleRouteLength begin lenth
	bodylength=length-19
	recive_nlri=dict() 

	UnfeasibleRouteLength=int(Body_strHex[bodyPoint:bodyPoint+4],16)	
	bodyPoint+=2
	bodylength-=2
	
	
	WithdrawnRoutes=Body_strHex[bodyPoint*2:(bodyPoint+UnfeasibleRouteLength)*2]
	print UnfeasibleRouteLength
	print '@#@@@@@@@@@@'
	bodyPoint+=UnfeasibleRouteLength
	bodylength-=UnfeasibleRouteLength
	WithdrawNlri=Getnlris(WithdrawnRoutes,UnfeasibleRouteLength)
	for i in WithdrawNlri:
		recive_nlri_withdraw.append(i)
	print recive_nlri_withdraw
recive_nlri_withdraw=[]
recive_attribute=dict()
if __name__ == "__main__":
	print aggregator('01010101',4)
	#  print "Test 3 - HexToByte - Passed: ", HexToByte( __hexStr2 ) == __byteStr

    # turn a non-space separated hex string into a space separated hex string!
  #  print "Test 4 - Combined  - Passed: ", ByteToHex( HexToByte( __hexStr1 ) ) == __hexStr2