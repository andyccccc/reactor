#class bgpAttribute_Flag:
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
def GetFlag(flagsData):		
	flagsData=(flagsData>>4)
	flags=''
	for i in range(3,-1,-1):
		if (flagsData & (1<<i)):
			flags+=Flags[1<<(i+4)]+' '
	return flags+' '+str(flagsData) 