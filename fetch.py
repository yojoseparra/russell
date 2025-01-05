
# ---------------------------------------------------------------------
# Input JSON structure
"""

data = {
    "CVNA": [
        {
            "2024-06-30": {
                "dilutedAverageShares": 210897500.0,
                "basicEPS": 6.56,
                "basicAverageShares": 115071500.0,
                "dilutedEPS": 3.16
            }
        },
        {
            "2019-12-31": {
                "otherunderPreferredStockDividend": 0.0
            }
        }
    ]
}

"""



#--------------------------------------------------------------------------------

#incomeStatementHistory
#balanceSheetHistory
#cashflowStatementHistory

import yfinance as yf
import pandas as pd


from yahoofinancials import YahooFinancials as YF
ticker=[
'MSTR',
'CVNA',
'SMC',
'FI',
'DUOL',
'SFM',
'DOC',
'FTAI',
'SMMT',
'INSM',
'CRDO',
'RKLB',
'AUR',
'PR',
'COKE',
'PCVX',
'AAON',
'APG',
'PSN',
'AIT',
'MTSI',
'BRBR',
'APPF',
'HLNE',
'MLI',
'FLR',
'ALTR',
'DRS',
'FN',
'KNTK',
'SUM',
'ITCI',
'CRS',
'GTLS',
'SSB',
'HQY',
'ONTO',
'ENSG',
'LNW',
'ATI',
'ELF',
'SSD',
'UFPI',
'GKOS',
'RVMD',
'EXLS',
'CVLT',
'MARA',
'CHRD',
'WTS',
'ONB']
f = YF(ticker)
a=f.get_financial_stmts(frequency ='annual', statement_type=[ 'income', 'balance', 'cash' ]) 


b=a['incomeStatementHistory']


# Flatten the JSON data
flattened_data = []

data=b
for company, records in data.items():
    for record in records:
        for date, metrics in record.items():
            row = {"Company": company, "Date": date}
            row.update(metrics)  # Add financial metrics
            flattened_data.append(row)

# Create a DataFrame
df = pd.DataFrame(flattened_data)

e = pd.melt(df, id_vars = ['Company', 'Date'], value_name ='fiorres', var_name='fitest')
e.columns = ['subjid', 'fidtc', 'fitest', 'fiorres']
e['fiorresu'] = 'USD'
e['domain'] = 'FI'
e['figrpid'] = 'RUSSEL 2000'
e['ficat'] = 'INCOME STATEMENT'

f = e[ [ 'domain', 'ficat','figrpid', 'subjid', 'fitest','fiorres', 'fiorresu', 'fidtc']]



#### 

c=a['balanceSheetHistory']


# Flatten the JSON data
flattened_data = []
e=[]
df = []

data=c
for company, records in data.items():
    for record in records:
        for date, metrics in record.items():
            row = {"Company": company, "Date": date}
            row.update(metrics)  # Add financial metrics
            flattened_data.append(row)

# Create a DataFrame
df = pd.DataFrame(flattened_data)

e = pd.melt(df, id_vars = ['Company', 'Date'], value_name ='fiorres', var_name='fitest')
e.columns = ['subjid', 'fidtc', 'fitest', 'fiorres']
e['fiorresu'] = 'USD'
e['domain'] = 'FI'
e['figrpid'] = 'RUSSEL 2000'
e['ficat'] = 'BALANCE SHEET'

g = e[ [ 'domain', 'ficat','figrpid', 'subjid', 'fitest','fiorres', 'fiorresu', 'fidtc']]


###

d=a['cashflowStatementHistory']


# Flatten the JSON data
flattened_data = []
e=[]
df = []

data=d
for company, records in data.items():
    for record in records:
        for date, metrics in record.items():
            row = {"Company": company, "Date": date}
            row.update(metrics)  # Add financial metrics
            flattened_data.append(row)

# Create a DataFrame
df = pd.DataFrame(flattened_data)

e = pd.melt(df, id_vars = ['Company', 'Date'], value_name ='fiorres', var_name='fitest')
e.columns = ['subjid', 'fidtc', 'fitest', 'fiorres']
e['fiorresu'] = 'USD'
e['domain'] = 'FI' 
e['figrpid'] = 'RUSSEL 2000'
e['ficat'] = 'CASH FLOWS'

h = e[ [ 'domain', 'ficat','figrpid', 'subjid', 'fitest','fiorres', 'fiorresu', 'fidtc']]

z = pd.concat([f,g,h])

z.to_csv('data/a.csv')


# ___________________________________________________________________________________________________________________________

d = pd.read_csv("data/russell2.csv")
var = "'"+ d['company']+"',"
var.to_csv('data/string.csv')
#incomeStatementHistory
#balanceSheetHistory
#cashflowStatementHistory

import yfinance as yf
import pandas as pd


from yahoofinancials import YahooFinancials as YF
ticker=[
'SPSC',
'SPXC',
'STEP',
'MTDR',
'UPST',
'MOD',
'ANF',
'DDS',
'CWST',
'ASTS',
'ZWS',
'RHP',
'JXN',
'TMHC',
'BMI',
'MDGL',
'CADE',
'LUMN',
'BECN',
'HIMS',
'AMKR',
'CSWI',
'CMC',
'IONQ',
'LNTH',
'QTWO',
'SATS',
'SOUN',
'GBCI',
'TRNO',
'SKY',
'NUVL',
'RMBS',
'HALO',
'COOP',
'MTH',
'CRVL',
'HOMB',
'MMSI',
'NOVT',
'UMBF',
'CYTK',
'BPMC',
'HRI',
'SITM',
'FSS',
'SIGI',
'ESNT',
'BE',
'JOBY',
'CORT',
'RDNT',
'KNF',
'FFIN',
'WK',
'KRG',
'EPRT',
'GATX',
'BCPC',
'GPI',
'EAT',
'PIPR',
'PIPR',
'WFRD',
'ACIW',
'CNX',
'FG',
'CBT',
'SHAK',
'IBP',
'CHX',
'MC',
'STRL',
'ASAN',
'UBSI',
'BIPC',
'LANC',
'QLYS',
'SMR',
'ROAD',
'PFSI',
'MAC',
'ACA',
'INTA',
'VRNS',
'ACT',
'VKTX',
'KBH',
'DY',
'BCC',
'RRR',
'SWX',
'VLY',
'BBIO',
'CALM',
'TENB',
'NXT',
'ZETA',
'SFBS',
'NSIT']




ticker =[
'ITRI',
'WHD',
'AI',
'FRSH',
'CNS',
'RDN',
'TGTX',
'MGY',
'CRNX',
'ABG',
'HWC',
'BDC',
'ESGR',
'CTRE',
'ALKS',
'IDCC',
'SLG',
'BRP',
'CRK',
'KTB',
'IESC',
'SMTC',
'MATX',
'IRT',
'PECO',
'FELE',
'LTH',
'URBN',
'FCFS',
'NJR',
'TNET',
'RUSHA',
'EXPO',
'KRYS',
'POR',
'PRCT',
'BOX',
'ITGR',
'CIVI',
'LRN',
'SM',
'ABCB',
'AROC',
'AX',
'GLNG',
'ACLX',
'PLXS',
'GOLF',
'FTDR',
'MUR',
'AVNT',
'AEIS',
'BOOT',
'ADMA',
'RXO',
'RUSHB',
'ORA',
'IPAR',
'FIZZ',
'AXSM',
'BKH',
'IBOC',
'KAI',
'AVAV',
'BGC',
'SANM',
'RIOT',
'SKYW',
'GH',
'BRZE',
'GSHD',
'PI',
'PRIM',
'GBTG',
'MHO',
'MMS',
'BANF',
'MIR',
'DORM',
'VCTR',
'USLM',
'SLAB',
'SBRA',
'BCO',
'RELY',
'GVA',
'HAE',
'NOG',
'PBH',
'MCY',
'IMVT',
'FUL',
'KTOS',
'OPCH',
'GHC',
'CBZ',
'BL',
'SG',
'OGS',
'ALKT',
'BLKB',
'TDS',
'NPO',
'SMPL',
'HGV',
'TCBI',
'SKT',
'CNO',
'CNK',
'CVCO',
'SRRK',
'VRRM',
'NNI',
'ALIT',
'JBT',
'SR',
'CARG',
'BHVN',
'ASGN',
'PJT',
'RNA',
'ASB',
'EBC',
'APLE',
'REZI',
'GEO',
'FULT',
'MWA',
'CCOI',
'APAM',
'YOU',
'GFF',
'ALE',
'CRC',
'IGT',
'AGYS',
'ENS',
'AUB',
'GSAT',
'SIG',
'ASO',
'POWI',
'PAYO',
'CDP',
'SLVM',
'TPH',
'DOCN',
'AXNX',
'KFY',
'WDFC',
'ESE',
'CATY',
'KGS',
'PTCT',
'ACHR',
'WD',
'FIBK',
'MGEE',
'GMS',
'UNF',
'HASI',
'ABM',
'COMP',
'CLSK',
'CBU',
'ENV',
'HL',
'INST',
'AVPT',
'WSFS',
'CEIX',
'CWK',
'ACVA',
'RYTM',
'ATMU',
'EE',
'OSCR',
'PBF',
'SGHC',
'PCH',
'VCYT',
'DEI',
'FA',
'BXMT',
'UEC',
'CRGY',
'ATGE',
'ALRM',
'HP',
'TEX',
'DNLI',
'AEO',
'NHI',
'NARI',
'FORM',
'SXT',
'JJSF',
'FBP',
'BFH',
'HCC',
'SNEX',
'GNW',
'JANX',
'BNL',
'SYNA',
'OTTR',
'CVBF',
'SHOO',
'APPN',
'GEF',
'OUT',
'NWE',
'NSP',
'AWR',
'FLNC',
'LBRT',
'VAL',
'PTVE',
'RSI',
'PRKS',
'HBI',
'TRN',
'OSIS',
'BKU',
'POWL',
'DIOD',
'AMBA',
'PRK',
'AKR',
'PATK',
'HUBG',
'PTEN',
'INDB',
'NMIH',
'LMND',
'SFNC',
'TGNA',
'AMR',
'BOH',
'IIPR',
'ATKR',
'PRGS',
'LCII',
'MGRC',
'PLMR',
'CPK',
'IOSP',
'AVA',
'CWT',
'PSMT',
'WAFD',
'ACAD',
'GRBK',
'GT',
'VERA',
'LAUR',
'SWTX',
'VCEL',
'HTLF',
'TWST',
'AZZ',
'FOLD',
'LIVN',
'ARCH',
'UE',
'STNE',
'GRND',
'FCPT',
'FFBC',
'PAR',
'PDCO',
'LFST',
'KYMR',
'TOWN',
'ABR',
'IBTX',
'JOE',
'ARWR',
'KWR',
'WULF',
'HWKN',
'NEOG',
'IRTC',
'DFH',
'TBBK',
'BTU',
'MYRG',
'KLIC',
'LXP',
'PFS',
'BANC',
'BKE',
'EPAC',
'ENVA',
'YELP',
'ENR',
'PPBI',
'TTMI',
'RVLV',
'CENT',
'DYN',
'CDE',
'EWTX',
'OII',
'VSTO',
'CCS',
'SGRY',
'VC',
'FBK',
'HNI',
'AIN',
'CPRX',
'CAKE',
'BATRA',
'ARCB',
'FRME',
'MTX',
'SEM',
'ZD',
'PRVA',
'SWI',
'RPD',
'SPNT',
'UTZ',
'AESI',
'TDW',
'FLYW',
'WLY',
'NMRK',
'SBCF',
'VICR',
'BANR',
'SHO',
'SXI',
'VIAV',
'PTGX',
'ACLS',
'JBLU',
'STNG',
'NBTB',
'STRA',
'AMRX',
'VSH',
'WRBY',
'CXW',
'EXTR',
'WERN',
'B',
'IVT',
'IOVA',
'ICFI',
'WSBC',
'CXM',
'LGIH',
'LBPH',
'GCMG',
'GERN',
'CALX',
'ALG',
'PAGS',
'RNST',
'MGNI',
'BEAM',
'TFIN',
'VZIO',
'TRMK',
'MTRN',
'AVDX',
'AGM',
'SYBT',
'CENTA',
'NEO',
'UPWK',
'SAH',
'AIR',
'ADUS',
'LMAT',
'HI',
'FIHL',
'ROIC',
'CNMD',
'EVCM',
'EVTC',
'TRUP',
'AGIO',
'LGND',
'VSEC',
'WS',
'TMDX',
'EFSC',
'KAR',
'ALHC',
'IDYA',
'PWP',
'NN',
'DBRG',
'HURN',
'CIFR',
'OMCL',
'HLMN',
'GBX',
'WVE',
'OSW',
'SKWD',
'COCO',
'RAMP',
'KMT',
'ROCK',
'STC',
'PLUS',
'MBC',
'HTH',
'BATRK',
'HEES',
'FL',
'PCT',
'AMPH',
'MIRM',
'MQ',
'AKRO',
'OFG',
'SPT',
'APGE',
'DRH',
'IBRX',
'SUPN',
'LOB',
'RXRX',
'ROG',
'CENX',
'UFPT',
'CMPR',
'EXPI',
'WOR',
'FBNC',
'CASH',
'PRG',
'WMK',
'TARS',
'SEMR',
'AGX',
'IRON',
'CHEF',
'NABL',
'STGW',
'CWH',
'CVI',
'CNXN',
'WWW',
'CHCO',
'JAMF',
'APLD',
'PRM',
'ESRT',
'NHC',
'LC',
'FCF',
'LKFN',
'HRMY',
'EVGO',
'LZB',
'DAN',
'REVG',
'HPK',
'NWBI',
'NEXT',
'GOGL',
'PD',
'VRNT',
'MNKD',
'DSGR',
'PRDO',
'TALO',
'DFIN',
'CODI',
'SJW',
'SONO',
'CLBK',
'THS',
'GTY',
'OI',
'NBHC',
'VVX',
'MBIN',
'CLDX',
'KN',
'MXL',
'UPBD',
'BHE',
'MLKN',
'PEB',
'XNCR',
'EPC',
'XMTR',
'IAS',
'MLNK',
'INSW',
'HLIO',
'NMRA',
'UNFI',
'NIC',
'DVAX',
'CTS',
'VRTS',
'AAT',
'HMN',
'APOG',
'BOWL',
'LTC',
'UCTT',
'MSGE',
'DNUT',
'PLAB',
'NWN',
'CUBI',
'TROX',
'NGVT',
'WTTR',
'GNL',
'WT',
'NTCT',
'SCL',
'SASR',
'WKC',
'WGO',
'XHR',
'NAPA',
'FDP',
'VRE',
'STBA',
'VITL',
'VBTX',
'CSTM',
'HOPE',
'ADNT',
'GDYN',
'MCRI',
'ALGT',
'MTTR',
'ENVX',
'BV',
'SPNS',
'NAVI',
'RLJ',
'TNC',
'TCBK',
'GIII',
'HELE',
'VECO',
'ADEA',
'CSGS',
'INFN',
'BCRX',
'MMI',
'SRCE',
'ATRC',
'SVV',
'HLIT',
'INMD',
'ANDE',
'UMH',
'ZUO',
'DNOW',
'CMRE',
'TILE',
'SDGR',
'LADR',
'SABR',
'BUSE',
'RXST',
'ARIS',
'WABC',
'QCRH',
'KW',
'RBCAA',
'UNIT',
'SCS',
'RCUS',
'FSLY',
'DHT',
'PZZA',
'SAFE',
'NVAX',
'MODG',
'CMPO',
'ELME',
'KNSA',
'CDRE',
'PHR',
'TWKS',
'ATSG',
'NRIX',
'WINA',
'ARQT',
'WLFC',
'VRDN',
'TGI',
'ULCC',
'SFL',
'KOS',
'LNN',
'USPH',
'FOR',
'BLBD',
'HLX',
'PBI',
'TVTX',
'UVV',
'LZ',
'UTI',
'MRTN',
'MDXG',
'BY',
'ATEN',
'JBGS',
'OPEN',
'IMAX',
'ALEX',
'TPC',
'OCUL',
'NX',
'ATEC',
'ENFN',
'NSSC',
'DCOM',
'AUPH',
'ARVN',
'SPHR',
'IMKTA',
'PFBC',
'EVH',
'LILA',
'GABC',
'DSP',
'NTLA',
'MYGN',
'EVEX',
'AOSL',
'LILAK',
'RES',
'AMRC',
'COUR',
'XPRO',
'TNK',
'FOXF',
'EIG',
'BHLB',
'NVEE',
'THRM',
'CNNE',
'DAWN',
'AHCO',
'CRAI',
'BLX',
'CRCT',
'OXM',
'ULH',
'SBH',
'COHU',
'AMWD',
'ARI',
'HROW',
'IDT',
'OLO',
'SCSC',
'DXPE',
'PGNY',
'QNST',
'ARLO',
'SAFT',
'DEA',
'COMM',
'BLFS',
'ACDC',
'RC',
'ARDX',
'BLUE',
'PEBO',
'TWO',
'KALU',
'XPEL',
'CDNA',
'STAA',
'NTST',
'LEU',
'CIM',
'AIV',
'AORT',
'DGII',
'UUUU',
'CTOS',
'MD',
'HCI',
'VTLE',
'ANIP',
'SNDX',
'CARS',
'FLNG',
'FWRG',
'KRO',
'PMT',
'PL',
'PDFS',
'LVWR',
'ECPG',
'EVRI',
'INVA',
'PDM',
'KRUS',
'UDMY',
'SPRY',
'PSFE',
'CSR',
'SBGI',
'KFRC',
'CBRL',
'NXRT',
'NG',
'VMEO',
'OCFC',
'WEAV',
'ELVN',
'BBSI',
'FBMS',
'MRC',
'SSTK',
'EMBC',
'OBK',
'BSIG',
'CECO',
'EFC',
'BRKL',
'RDFN',
'CMCO',
'ADV',
'AMPL',
'PRO',
'AHH',
'MFA',
'DK',
'TMP',
'RCKT',
'JBI',
'ICHR',
'CCB',
'PLSE',
'OPK',
'ARR',
'XRX',
'THR',
'ASPN',
'MDRX',
'OMI',
'FBRT',
'BELFB',
'AMAL',
'TPB',
'BFC',
'PRLB',
'SBSI',
'PGRE',
'GRC',
'LMB',
'MSEX',
'PLAY',
'GIC',
'TRS',
'BKD',
'JBSS',
'CTBI',
'BLMN',
'BHRB',
'AMTB',
'DLX',
'ETWO',
'AMN',
'LQDT',
'VIR',
'AMSF',
'LPG',
'FIGS',
'DX',
'TRNS',
'OEC',
'SXC',
'INOD',
'PNTG',
'PFC',
'CNOB',
'BXC',
'GOGO',
'MGPI',
'BDN',
'FMBH',
'VTOL',
'HSTM',
'NRDS',
'BFS',
'AVAH',
'COLL',
'EEX',
'PUMP',
'ACEL',
'HY',
'KIND',
'NGVC',
'VVI',
'BZH',
'FWRD',
'HOV',
'HCSG',
'RWT',
'DCO',
'AVO',
'STKL',
'ERII',
'SCVL',
'PSTX',
'ADPT',
'IE',
'HSII',
'MATW',
'HTLD',
'LQDA',
'UVSP',
'PARR',
'UTL',
'PAHC',
'PCRX',
'FIP',
'CLB',
'GDEN',
'COGT',
'BMBL',
'EYE',
'ACMR',
'INDI',
'TELL',
'HFWA',
'CMTG',
'ATLC',
'JACK',
'NUVB',
'ECVT',
'HCKT',
'CAL',
'EGBN',
'JELD',
'SWIM',
'ZYME',
'CFFN',
'MCBS',
'PLYM',
'REPL',
'FNA',
'YEXT',
'TH',
'PRA',
'ASTE',
'WNC',
'PLRX',
'ARRY',
'ARKO',
'CPF',
'FCBC',
'PPTA',
'BFST',
'CFB',
'MBUU',
'PRAA',
'ODP',
'ASIX',
'AVNS',
'OSBC',
'BRSP',
'BJRI',
'SITC',
'MLR',
'ETNB',
'CSTL',
'SNCY',
'GLDD',
'CRSR',
'BASE',
'DAKT',
'VTS',
'CTKB',
'KREF',
'GRNT',
'RPAY',
'TIPT',
'MBWM',
'IBCP',
'PUBM',
'CDMO',
'GES',
'RLAY',
'HAFC',
'GCI',
'UFCS',
'DJCO',
'HAYN',
'MNRO',
'AXL',
'CVLG',
'CEVA',
'GSBC',
'HBNC',
'RDW',
'KROS',
'ETD',
'TYRA',
'BFLY',
'HLF',
'IIIV',
'ORRF',
'PAX',
'KURA',
'DMRC',
'HBT',
'GOOD',
'SHLS',
'CCO',
'WSR',
'TRTX',
'NTGR',
'EOLS',
'MCB',
'SMP',
'REX',
'INN',
'SEAT',
'SHEN',
'ERAS',
'BALY',
'SCHL',
'AVXL',
'RBBN',
'MAX',
'SMBC',
'EQBK',
'CGEM',
'HAIN',
'RYI',
'EOSE',
'PTLO',
'FSBC',
'PRTH',
'RMR',
'NBR',
'TRST',
'REPX',
'USNA',
'HZO',
'MLAB',
'GPRE',
'OFIX',
'MCS',
'PRTA',
'OSPN',
'KOP',
'THRY',
'LPRO',
'HIPO',
'XPOF',
'VHI',
'ADTN',
'VEL',
'CTLP',
'WRLD',
'MOFG',
'CNDT',
'IMXI',
'NR',
'CAC',
'IRMD',
'EZPW',
'SPTN',
'TRDA',
'NPK',
'ABUS',
'AMRK',
'CCBG',
'WEST',
'PLPC',
'KRT',
'MATV',
'BRCC',
'NVTS',
'ALT',
'ESQ',
'ORC',
'HTBI',
'PACK',
'LIND',
'HTBK',
'STOK',
'AMBC',
'VREX',
'FNKO',
'SPFI',
'ALTI',
'BBAI',
'LXU',
'GNK',
'ODC',
'ATEX',
'TTGT',
'EVER',
'AXGN',
'PGC',
'SLP',
'BGS',
'CLNE',
'OLP',
'CSV',
'LEGH',
'AMPS',
'RGR',
'FPI',
'CTO',
'INNV',
'FFWM',
'UVE',
'NVRI',
'LYTS',
'EU',
'FLGT',
'WASH',
'FRPH',
'CASS',
'HIFS',
'ORIC',
'CCRN',
'MLYS',
'GDOT',
'EVLV',
'RSVR',
'NYMT',
'PLOW',
'DHC',
'WLDN',
'MNTK',
'CLMB',
'THFF',
'TK',
'GAMB',
'IIIN',
'SMBK',
'ATRO',
'FMNB',
'OPFI',
'SRDX',
'CCNE',
'BORR',
'MEG',
'MSBI',
'HONE',
'SHBI',
'IRWD',
'GMRE',
'SIBN',
'BIGC',
'PACB',
'TERN',
'PFIS',
'ALRS',
'EBF',
'CNSL',
'SMLR',
'SENEA',
'BBW',
'UHT',
'DGICA',
'NFBK',
'NAT',
'METCB',
'SVRA',
'RXT',
'KODK',
'ACCO',
'CMP',
'PHAT',
'DDD',
'BH',
'ATXS',
'KIDS',
'OABI',
'GCBC',
'LASR',
'TREE',
'EBTC',
'HNRG',
'BHB',
'NWPX',
'PROK',
'HYLN',
'EAF',
'AROW',
'RDVT',
'DH',
'KRNY',
'FARO',
'RYAM',
'HUMA',
'TWI',
'IVR',
'BAND',
'EGY',
'FUBO',
'MPB',
'CHCT',
'GLRE',
'EYPT',
'CRMD',
'FLWS',
'CBNK',
'ITIC',
'XERS',
'NOVA',
'LINC',
'VALU',
'FFIC',
'YORW',
'TCBX',
'SFIX',
'KELYA',
'OMER',
'RDUS',
'BOC',
'LMNR',
'HCAT',
'TBPH',
'SWBI',
'GCO',
'TTI',
'CYH',
'VERV',
'BWMN',
'VLGEA',
'UIS',
'FC',
'MGTX',
'SLQT',
'DIN',
'RNAC',
'WALD',
'ASC',
'ANAB',
'ANNX',
'CVGW',
'CLDT',
'HOUS',
'RICK',
'NRIM',
'AGS',
'UNTY',
'XPER',
'TMCI',
'KE',
'CLFD',
'ARCT',
'CCSI',
'CELC',
'GLUE',
'MOV',
'HPP',
'MEI',
'MYE',
'CDXS',
'EBS',
'CRMT',
'CLPT',
'MXCT',
'LESL',
'ORGO',
'ZEUS',
'ZVRA',
'PKST',
'BSRR',
'FISI',
'SNBR',
'ESPR',
'CURV',
'KOD',
'SIGA',
'SHYF',
'FMAO',
'DCGO',
'YMAB',
'MLP',
'SKYT',
'ACTG',
'ALNT',
'DHIL',
'TCMD',
'PTSI',
'KALV',
'EHAB',
'NNOX',
'AMCX',
'SGMO',
'WOW',
'IGMS',
'CARE',
'SANA',
'BSVN',
'GNTY',
'AURA',
'SD',
'QUAD',
'SVC',
'PKOH',
'NRC',
'BWB',
'TRC',
'MVST',
'RBB',
'RGNX',
'QTRX',
'LOVE',
'EGHT',
'CLW',
'CWCO',
'FBIZ',
'LAND',
'MITK',
'NL',
'JILL',
'RRBI',
'HBCP',
'COOK',
'BMRC',
'WTBA',
'ALLO',
'GNE',
'OOMA',
'BKKT',
'JOUT',
'ZUMZ',
'SB',
'ACRE',
'ACNB',
'LRMR',
'BBCP',
'NECB',
'OLMA',
'ZIMV',
'BARK',
'PMTS',
'CYRX',
'PRME',
'HVT',
'NVEC',
'NUS',
'USCB',
'GTN',
'LOCO',
'GEVO',
'NEWT',
'ANGO',
'LSEA',
'LXFR',
'LAW',
'TRUE',
'FSBW',
'MEC',
'CIVB',
'HEAR',
'BRT',
'SMRT',
'IHRT',
'ISPR',
'BTBT',
'SSBK',
'CIX',
'MTW',
'RM',
'BTMD',
'NODK',
'SFST',
'ARTNA',
'EB',
'EWCZ',
'RNGR',
'HLLY',
'VYGR',
'TITN',
'AEHR',
'IBEX',
'ONEW',
'WEYS',
'NATH',
'SPOK',
'VMD',
'KLTR',
'MPX',
'MCFT',
'OBT',
'RIGL',
'RLGT',
'COFS',
'DBI',
'IPI',
'CZFS',
'XOMA',
'SAGE',
'AIRS',
'TNGX',
'ASLE',
'PNRG',
'BKSY',
'OB',
'SLRN',
'PSTL',
'RVNC',
'OIS',
'DENN',
'PCYO',
'FHTX',
'BCML',
'TRVI',
'RCEL',
'FDMT',
'BRY',
'CERS',
'DSGN',
'REFI',
'BLDE',
'FNLC',
'CRNC',
'VPG',
'PDLB',
'SMTI',
'FDBC',
'SNFCA',
'MBI',
'CVRX',
'FLIC',
'PBFS',
'PCB',
'JMSB',
'CZNC',
'FRST',
'TTSH',
'FORR',
'CDZI',
'CBAN',
'GWRS',
'EXFY',
'PKE',
'NREF',
'IMMR',
'JAKK',
'RGP',
'PBPB',
'ALDX',
'OSUR',
'ONTF',
'NRDY',
'NATR',
'PLBC',
'WSBF',
'FRBA',
'DOMO',
'AMLX',
'MVBF',
'NRGV',
'ITOS',
'ACCD',
'PFMT',
'MG',
'REI',
'TG',
'AFRI',
'ATNI',
'PKBK',
'VNDA',
'IRBT',
'URGN',
'MRSN',
'CPS',
'EVI',
'MYPS',
'TBI',
'TSBK',
'ZYXI',
'WTI',
'CHMG',
'BWFG',
'SAMG',
'FOA',
'HDSN',
'PWOD',
'SBT',
'BPRN',
'OVLY',
'CFFI',
'ANIK',
'MBCN',
'ASUR',
'PANL',
'BYND',
'EVBN',
'AMPY',
'AVIR',
'FVCB',
'GOCO',
'TTEC',
'ZVIA',
'MODV',
'NWFL',
'BRBS',
'QSI',
'ALTG',
'INSE',
'NAUT',
'PINE',
'LWLG',
'HRTX',
'BYON',
'BLFY',
'LCNB',
'LUNG',
'CPSS',
'CIO',
'AEVA',
'VUZI',
'KFS',
'FF',
'ACRS',
'CHGG',
'VABK',
'AVNW',
'BHR',
'RMAX',
'ONL',
'EVC',
'ZNTL',
'PLL',
'NC',
'FCEL',
'AOMR',
'ACRV',
'TNYA',
'UHG',
'ATOM',
'HMST',
'LAZR',
'INGN',
'UTMD',
'ESCA',
'BCBP',
'INBX',
'DC',
'RGCO',
'PVBC',
'AFCG',
'MED',
'PGEN',
'FATE',
'HQI',
'SWKH',
'BMEA',
'ESSA',
'RELL',
'OBIO',
'HSHP',
'MYFW',
'HFFG',
'MGNX',
'ALEC',
'LXRX',
'STRS',
'NKSH',
'FCCO',
'ALCO',
'KRMD',
'LYEL',
'SLDP',
'FRGE',
'SKIN',
'BCOV',
'TSE',
'INZY',
'ARAY',
'CLAR',
'LNZA',
'ELA',
'CDLX',
'INFU',
'CRGE',
'SSP',
'GPRO',
'SPCE',
'CHRS',
'EPM',
'TCX',
'FET',
'SGHT',
'AMPX',
'SRI',
'HOFT',
'EQC',
'VOXX',
'RMNI',
'MVIS',
'DOUG',
'RCKY',
'III',
'CCRD',
'JRVR',
'SMHI',
'BW',
'STRO',
'CRBU',
'PAYS',
'TDUP',
'GPMT',
'TSVT',
'EHTH',
'ORGN',
'FENC',
'NKTX',
'JYNT',
'MKTW',
'PLCE',
'VTYX',
'SCPH',
'IAUX',
'EGAN',
'TSQ',
'SSTI',
'BLNK',
'FLL',
'MNSB',
'NOTE',
'RILY',
'NVRO',
'PEPG',
'SKIL',
'AVD',
'ATLO',
'MCRB',
'BOOM',
'ZURA',
'APPS',
'SES',
'CMT',
'SEER',
'AMWL',
'TUSK',
'CTGO',
'CABA',
'DXLG',
'STHO',
'MHLD',
'SGMT',
'PLX',
'SAVA',
'CMCL',
'QIPT',
'ENTA',
'VRA',
'POWW',
'DM',
'EDIT',
'WW',
'CNTY',
'MPLN',
'VGAS',
'XFOR',
'SCWO',
'PETS',
'AKYA',
'KVHI',
'TELA',
'SKYX',
'SAVE',
'LCTX',
'DLTH',
'TLYS',
'IPSC',
'DTC',
'GRWG',
'XGN',
'PRPL',
'FOSL',
'VERI',
'SPWH',
'CMTL',
'HLVX',
'SCLX',
'INTT',
'HBIO',
'ALLK',
'IVAC',
'STKS',
'OPRX',
'NVCT',
'KPTI',
'DHX',
'ASRT',
'RBOT',
'ME',
'CVGI',
'NKLA',
'PMVP',
'VIGL',
'KLXE',
'GNLX',
'RRGB',
'SST',
'IKNA',
'UONE',
'ACET',
'GBIO',
'ALXO',
'OPI',
'MASS',
'PIII',
'OVID',
'AVTE',
'VATE',
'LPSN',
'AGEN',
'OPTN',
'CLPR',
'BCAB',
'PDSB',
'CATO',
'VOR',
'BIRD',
'GWH',
'MURA',
'CUE',
'ATRA',
'TPIC',
'OM',
'LUNA',
'PRTS',
'STEM',
'OMGA',
'ALVR',
'IMRX',
'KZR',
'PRLD',
'UONEK',
'RLYB',
'WKHS',
'LICY',
'ATNM',
'FTCI',
'BGFV',
'OTLK',
'VRCA',
'RENT',
'XAIR',
'FGEN',
'DZSI',
'RAPT',
'NDLS',
'FEAM',
'CMBM',
'DFLI',
'CARM',
'CTXR',
'BTAI',
'BGXX',
'MRNS',
'CARA',
'GORV',
'DNMR',
'BHIL',
'TSBX',
'AKTS',
'EGRX',
'CUTR',
'EYEN',
'MOND',
'MAXN',
'LPTV',
'CMAX',
'ATHX',
'PRST',
'VAXX',
'EVLO',
'GENC',
'NBN',
'OFLX',
'ARL',
'ALX',
'NTB',
'NXDT',
'WLLAW',
'WLLBW',
'TCI']

f = YF(ticker)
a=f.get_financial_stmts(frequency ='annual', statement_type=[ 'income', 'balance', 'cash' ]) 


b=a['incomeStatementHistory']


# Flatten the JSON data
flattened_data = []

data=b
for company, records in data.items():
    for record in records:
        for date, metrics in record.items():
            row = {"Company": company, "Date": date}
            row.update(metrics)  # Add financial metrics
            flattened_data.append(row)

# Create a DataFrame
df = pd.DataFrame(flattened_data)

e = pd.melt(df, id_vars = ['Company', 'Date'], value_name ='fiorres', var_name='fitest')
e.columns = ['subjid', 'fidtc', 'fitest', 'fiorres']
e['fiorresu'] = 'USD'
e['domain'] = 'FI'
e['figrpid'] = 'RUSSEL 2000'
e['ficat'] = 'INCOME STATEMENT'

f = e[ [ 'domain', 'ficat','figrpid', 'subjid', 'fitest','fiorres', 'fiorresu', 'fidtc']]



#### 

c=a['balanceSheetHistory']


# Flatten the JSON data
flattened_data = []
e=[]
df = []

data=c
for company, records in data.items():
    for record in records:
        for date, metrics in record.items():
            row = {"Company": company, "Date": date}
            row.update(metrics)  # Add financial metrics
            flattened_data.append(row)

# Create a DataFrame
df = pd.DataFrame(flattened_data)

e = pd.melt(df, id_vars = ['Company', 'Date'], value_name ='fiorres', var_name='fitest')
e.columns = ['subjid', 'fidtc', 'fitest', 'fiorres']
e['fiorresu'] = 'USD'
e['domain'] = 'FI'
e['figrpid'] = 'RUSSEL 2000'
e['ficat'] = 'BALANCE SHEET'

g = e[ [ 'domain', 'ficat','figrpid', 'subjid', 'fitest','fiorres', 'fiorresu', 'fidtc']]


###

d=a['cashflowStatementHistory']


# Flatten the JSON data
flattened_data = []
e=[]
df = []

data=d
for company, records in data.items():
    for record in records:
        for date, metrics in record.items():
            row = {"Company": company, "Date": date}
            row.update(metrics)  # Add financial metrics
            flattened_data.append(row)

# Create a DataFrame
df = pd.DataFrame(flattened_data)

e = pd.melt(df, id_vars = ['Company', 'Date'], value_name ='fiorres', var_name='fitest')
e.columns = ['subjid', 'fidtc', 'fitest', 'fiorres']
e['fiorresu'] = 'USD'
e['domain'] = 'FI' 
e['figrpid'] = 'RUSSEL 2000'
e['ficat'] = 'CASH FLOWS'

h = e[ [ 'domain', 'ficat','figrpid', 'subjid', 'fitest','fiorres', 'fiorresu', 'fidtc']]

z = pd.concat([f,g,h])

z.to_csv('data/c.csv')

y = z.dropna()


y.to_csv('data/c_not_na.csv')

#--------------------------------------------- Company profile download

# connecting to postgreSQL
exec(open('connect2sql.py').read())

a = pd.read_sql_query("SELECT distinct subjid from ru.fi", conn)
conn.close()


# List of tickers
subjid =a['subjid'].tolist()


# Initialize an empty dictionary
d = {}

import time
# Loop through each ticker
for i in subjid:
    try:
        # Fetch data for the current ticker
        ticker = yf.Ticker(i)
        info = ticker.info  # Access ticker info
        
        # Safely fetch the 'longBusinessSummary'
        summary = info.get('longBusinessSummary', 'No summary available')
        
        # Add to the dictionary
        d[i] = summary

        # Delay to avoid overwhelming the server
        time.sleep(2)  # Wait 2 seconds before the next request
    except Exception as e:
        # Handle errors gracefully
        print(f"Failed to fetch data for {i}: {e}")
        d[i] = "Error fetching data"


e=pd.DataFrame([d])

f=pd.melt(e, var_name='subjid', value_name= 'profile')

f.to_csv('data/pr.csv', index=False)







#-------------------------------------------------------------------------------Debugging Tips
#If the problem persists:

#Inspect the Data: Print info for each ticker to ensure the data is being fetched:

#python
#Copy code
print(f"Data for {i}: {info}")
#Verify the Iteration: Print the current ticker in each iteration:

#python
#Copy code
print(f"Processing ticker: {i}")
#Check API Limits: yfinance may throttle requests if you query too frequently. Introduce a delay between requests:

#python
#Copy code
import time
time.sleep(1)  # Wait 1 second between requests
#Check subjid for Valid Tickers: If any ticker in subjid is invalid, it can cause issues. Verify:

#python
#Copy code
print([i for i in subjid if yf.Ticker(i).info])
