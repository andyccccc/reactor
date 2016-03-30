#from  bgpAttributeDetail import *
import bgpAttributeDetail
class bgpAttribute_Type:
	ORIGIN             = 0x01
	AS_PATH            = 0x02
	NEXT_HOP           = 0x03
	MED                = 0x04
	LOCAL_PREF         = 0x05
	ATOMIC_AGGREGATE   = 0x06
	AGGREGATOR         = 0x07
	# RFC 1997
	COMMUNITY          = 0x08
	# RFC 4456
	ORIGINATOR_ID      = 0x09
	CLUSTER_LIST       = 0x0A  # 10
	# RFC 4760
	MP_REACH_NLRI      = 0x0E  # 14
	MP_UNREACH_NLRI    = 0x0F  # 15
	# RFC 4360
	EXTENDED_COMMUNITY = 0x10  # 16
	# RFC 4893
	AS4_PATH           = 0x11  # 17
	AS4_AGGREGATOR     = 0x12  # 18
	# RFC6514
	PMSI_TUNNEL        = 0x16  # 22
	# RFC5512
	TUNNEL_ENCAP       = 0x17  # 23
	AIGP               = 0x1A  # 26

	INTERNAL_NAME      = 0xFFFC
	INTERNAL_WITHDRAW  = 0xFFFD
	INTERNAL_WATCHDOG  = 0xFFFE
	INTERNAL_SPLIT     = 0xFFFF

	names = {
		ORIGIN:             'origin',
		AS_PATH:            'as-path',
		NEXT_HOP:           'next-hop',
		MED:                'med',              # multi-exit-disc
		LOCAL_PREF:         'local-preference',
		ATOMIC_AGGREGATE:   'atomic-aggregate',
		AGGREGATOR:         'aggregator',
		COMMUNITY:          'community',
		ORIGINATOR_ID:      'originator-id',
		CLUSTER_LIST:       'cluster-list',
		MP_REACH_NLRI:      'mp-reach-nlri',    # multi-protocol reacheable nlri
		MP_UNREACH_NLRI:    'mp-unreach-nlri',  # multi-protocol unreacheable nlri
		EXTENDED_COMMUNITY: 'extended-community',
		AS4_PATH:           'as4-path',
		AS4_AGGREGATOR:     'as4-aggregator',
		PMSI_TUNNEL:        'pmsi-tunnel',
		TUNNEL_ENCAP:       'tunnel-encaps',
		AIGP:               'aigp',
		0xfffc:             'internal-name',
		0xfffd:             'internal-withdraw',
		0xfffe:             'internal-watchdog',
		0xffff:             'internal-split'
	}
	Attribute_fun={'origin':bgpAttributeDetail.origin,
	'as-path':bgpAttributeDetail.aspath,
	'next-hop':bgpAttributeDetail.nexthop,
	'med':bgpAttributeDetail.med,
	'local-preference':bgpAttributeDetail.localpreference,
	'aggregator':bgpAttributeDetail.aggregator,
	'community':bgpAttributeDetail.community,
	'originator-id':bgpAttributeDetail.originatorid,
	'cluster-list':bgpAttributeDetail.clusterlist,
	'mp-reach-nlri':bgpAttributeDetail.mpreachnlri,
	'mp-unreach-nlri':bgpAttributeDetail.mpunreachnlri,
	'extended-community':bgpAttributeDetail.extendedcommunity,
	'as4-path':bgpAttributeDetail.as4path,
	'as4-aggregator':bgpAttributeDetail.as4aggregator,
	'pmsi-tunnel':bgpAttributeDetail.pmsitunnel,
	'tunnel-encaps':bgpAttributeDetail.tunnelencaps,
	'aigp':bgpAttributeDetail.aigp
	}
	
	