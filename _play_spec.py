#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

class CM3u8Spec:
#{
  def __init__(self):
  #{
    self.m_dictSkipSegment = {
      'head':{},
      'tail':{},
    }

    self._SetHeadSkipSegment('test', 10)
    
    # 综艺10秒
    self._SetHeadSkipSegment('QGUG106968', 10)
    self._SetHeadSkipSegment('RXIH242959', 10)
    self._SetHeadSkipSegment('BBDN818610', 10)
    self._SetHeadSkipSegment('OKRL639786', 10)
    self._SetHeadSkipSegment('ACJF912028', 10)
    self._SetHeadSkipSegment('ZIVX995615', 10)
    self._SetHeadSkipSegment('TEAV624863', 10)
    self._SetHeadSkipSegment('NKZA781124', 10)
    self._SetHeadSkipSegment('VWYC251745', 10)
    self._SetHeadSkipSegment('OQAM801595', 10)
    self._SetHeadSkipSegment('NTQN618946', 10)
    self._SetHeadSkipSegment('KEIM433755', 10)
    self._SetHeadSkipSegment('KAIG334356', 10)
    self._SetHeadSkipSegment('QXFS964564', 10)
    self._SetHeadSkipSegment('MVVV607093', 10)
    self._SetHeadSkipSegment('GPGR393694', 10)
    self._SetHeadSkipSegment('BJIN060702', 10)
    self._SetHeadSkipSegment('TAQU045727', 10)
    self._SetHeadSkipSegment('HJCG953723', 10)
    self._SetHeadSkipSegment('BTQI353850', 10)
    self._SetHeadSkipSegment('AFRU811873', 10)
    self._SetHeadSkipSegment('EUWH248603', 10)
    self._SetHeadSkipSegment('WGFT568498', 10)
    self._SetHeadSkipSegment('LAUY614979', 10)
    self._SetHeadSkipSegment('EAET502880', 10)
    self._SetHeadSkipSegment('BTYD281698', 10)
    self._SetHeadSkipSegment('NQIQ434777', 10)
    self._SetHeadSkipSegment('QDDM999043', 10)
    self._SetHeadSkipSegment('APTD452542', 10)
    self._SetHeadSkipSegment('LTZR803922', 10)
    self._SetHeadSkipSegment('WAUA120031', 10)
    self._SetHeadSkipSegment('FGAC328262', 10)
    self._SetHeadSkipSegment('CLQE333201', 10)
    self._SetHeadSkipSegment('KDNP666612', 10)
    self._SetHeadSkipSegment('ZCDT659501', 10)
    self._SetHeadSkipSegment('XEVA187448', 10)
    self._SetHeadSkipSegment('AUAR245880', 20)
    self._SetHeadSkipSegment('CAOK723427', 10)
    self._SetHeadSkipSegment('XGTQ086288', 10)
    self._SetHeadSkipSegment('TQNL109160', 10)
    self._SetHeadSkipSegment('OOEG799014', 10)
    self._SetHeadSkipSegment('EIJJ901806', 10)
    self._SetHeadSkipSegment('STIO711238', 10)
    self._SetHeadSkipSegment('JBCH721776', 10)
    self._SetHeadSkipSegment('LOCG252123', 10)
    self._SetHeadSkipSegment('NZGC515603', 10)
    self._SetHeadSkipSegment('TRWD904978', 10)
    self._SetHeadSkipSegment('MSXD676377', 10)
    self._SetHeadSkipSegment('YYCG198658', 10)
    self._SetHeadSkipSegment('PINT208432', 10)
    self._SetHeadSkipSegment('GALD278717', 10)
    self._SetHeadSkipSegment('BYYB984792', 10)
    self._SetHeadSkipSegment('KGPB636614', 10)
    self._SetHeadSkipSegment('UJQI087680', 10)
    self._SetHeadSkipSegment('KVCO571606', 10)
    self._SetHeadSkipSegment('FGEY939258', 10)
    self._SetHeadSkipSegment('ZRDQ788055', 10)
    self._SetHeadSkipSegment('KLDK024655', 10)
    self._SetHeadSkipSegment('ISZY816624', 10)
    self._SetHeadSkipSegment('LOSE348705', 10)
    self._SetHeadSkipSegment('TGSG334427', 10)
    self._SetHeadSkipSegment('SXBM843669', 10)
    self._SetHeadSkipSegment('CXUH065798', 10)
    self._SetHeadSkipSegment('AEBH259609', 10)
    self._SetHeadSkipSegment('JEVA646215', 10)
    self._SetHeadSkipSegment('NMQE581457', 10)
    self._SetHeadSkipSegment('SPMO332417', 10)
    self._SetHeadSkipSegment('PCGL869555', 10)
    self._SetHeadSkipSegment('DKRR006267', 10)
    self._SetHeadSkipSegment('BGKT557211', 10)
    self._SetHeadSkipSegment('YANJ393961', 10)
    self._SetHeadSkipSegment('ZWPC209770', 10)
    
    # 20秒
    self._SetHeadSkipSegment('CAOK723427', 20)
    self._SetHeadSkipSegment('XGTQ086288', 20)
    self._SetHeadSkipSegment('MSXD676377', 20)
    self._SetHeadSkipSegment('YYCG198658', 20)
    self._SetHeadSkipSegment('PINT208432', 20)
    self._SetHeadSkipSegment('GALD278717', 20)
    self._SetHeadSkipSegment('BYYB984792', 20)
    self._SetHeadSkipSegment('KGPB636614', 20)
    self._SetHeadSkipSegment('UJQI087680', 20)
    self._SetHeadSkipSegment('KVCO571606', 20)
    self._SetHeadSkipSegment('FGEY939258', 20)
    self._SetHeadSkipSegment('ZRDQ788055', 20)
    self._SetHeadSkipSegment('QGUG106968', 20)
    self._SetHeadSkipSegment('RXIH242959', 20)
    self._SetHeadSkipSegment('BBDN818610', 20)
    self._SetHeadSkipSegment('OKRL639786', 20)
    self._SetHeadSkipSegment('ACJF912028', 20)
    self._SetHeadSkipSegment('ZIVX995615', 20)
    self._SetHeadSkipSegment('TEAV624863', 20)
    self._SetHeadSkipSegment('NKZA781124', 20)
    self._SetHeadSkipSegment('VWYC251745', 20)
    self._SetHeadSkipSegment('OQAM801595', 20)
    self._SetHeadSkipSegment('MVVV607093', 20)
    self._SetHeadSkipSegment('GPGR393694', 20)
    self._SetHeadSkipSegment('BJIN060702', 20)
    self._SetHeadSkipSegment('TAQU045727', 20)
    self._SetHeadSkipSegment('HJCG953723', 20)
    self._SetHeadSkipSegment('BTQI353850', 20)
    self._SetHeadSkipSegment('AFRU811873', 20)
    self._SetHeadSkipSegment('EUWH248603', 20)
    self._SetHeadSkipSegment('WGFT568498', 20)
    self._SetHeadSkipSegment('NQIQ434777', 20)
    self._SetHeadSkipSegment('LTZR803922', 20)
    self._SetHeadSkipSegment('WAUA120031', 20)
    self._SetHeadSkipSegment('EIJJ901806', 20)
    self._SetHeadSkipSegment('STIO711238', 20)
    self._SetHeadSkipSegment('JBCH721776', 20)
    self._SetHeadSkipSegment('SXBM843669', 20)
    self._SetHeadSkipSegment('CXUH065798', 20)
    self._SetHeadSkipSegment('AEBH259609', 20)
    self._SetHeadSkipSegment('JEVA646215', 20)
    self._SetHeadSkipSegment('NMQE581457', 20)
    self._SetHeadSkipSegment('SPMO332417', 20)
    self._SetHeadSkipSegment('PCGL869555', 20)
    self._SetHeadSkipSegment('DKRR006267', 20)
    self._SetHeadSkipSegment('BGKT557211', 20)
    self._SetHeadSkipSegment('YANJ393961', 20)
    self._SetHeadSkipSegment('ZWPC209770', 20)
    self._SetHeadSkipSegment('NEEN859190', 20)
    self._SetHeadSkipSegment('UAKX720992', 20)
    self._SetHeadSkipSegment('REDG135449', 20)
    self._SetHeadSkipSegment('HZHY671063', 20)
    self._SetHeadSkipSegment('OVVO837498', 20)
    self._SetHeadSkipSegment('KBTM765407', 20)
    self._SetHeadSkipSegment('OZSK981378', 20)
    self._SetHeadSkipSegment('CAPC772743', 20)
    self._SetHeadSkipSegment('UDKY632619', 20)
    self._SetHeadSkipSegment('HUPH720251', 20)
    self._SetHeadSkipSegment('KFCD434679', 20)
    self._SetHeadSkipSegment('XGNJ688215', 20)
    self._SetHeadSkipSegment('UORW499129', 20)
    self._SetHeadSkipSegment('MSVN435193', 20)
    self._SetHeadSkipSegment('MLEW570555', 20)
    self._SetHeadSkipSegment('SDMK918732', 20)
    self._SetHeadSkipSegment('FWZK729758', 20)
    self._SetHeadSkipSegment('RCAI802656', 20)
    self._SetHeadSkipSegment('AUPI626707', 20)
    self._SetHeadSkipSegment('IDBL569368', 20)
    self._SetHeadSkipSegment('HOSB630620', 20)
    self._SetHeadSkipSegment('CCRI980163', 20)
    self._SetHeadSkipSegment('VNIE856131', 20)
    self._SetHeadSkipSegment('CQKG768441', 20)
    self._SetHeadSkipSegment('QXGO447030', 20)
    self._SetHeadSkipSegment('DMRH568590', 20)
    self._SetHeadSkipSegment('TCHC216618', 20)
    self._SetHeadSkipSegment('UJWB110554', 20)
    self._SetHeadSkipSegment('PZFF006640', 20)
    self._SetHeadSkipSegment('PVIG681088', 20)
    self._SetHeadSkipSegment('FMOV763172', 20)
    self._SetHeadSkipSegment('FYLU231971', 20)
    self._SetHeadSkipSegment('NUGK937538', 20)
    self._SetHeadSkipSegment('ZOGK446128', 20)
    self._SetHeadSkipSegment('GMYE846966', 20)
    self._SetHeadSkipSegment('CPSC095390', 20)
    self._SetHeadSkipSegment('FGWP164943', 20)
    self._SetHeadSkipSegment('YBZZ293608', 20)
    self._SetHeadSkipSegment('SSRW400380', 20)
    self._SetHeadSkipSegment('SROA514262', 20)
    self._SetHeadSkipSegment('EAIG175304', 20)
    self._SetHeadSkipSegment('NTAV893862', 20)
    self._SetHeadSkipSegment('DRAY100209', 20)
    self._SetHeadSkipSegment('SMXM731241', 20)
    self._SetHeadSkipSegment('NJDO181564', 20)
    self._SetHeadSkipSegment('EPHH528689', 20)
    self._SetHeadSkipSegment('UKTH220094', 20)
    self._SetHeadSkipSegment('AZGK765807', 20)
    self._SetHeadSkipSegment('SHHW949053', 20)
    self._SetHeadSkipSegment('DRGX157625', 20)
    self._SetHeadSkipSegment('VPNI497508', 20)
    self._SetHeadSkipSegment('OZVG021695', 20)
    self._SetHeadSkipSegment('XLRJ329998', 20)
    self._SetHeadSkipSegment('XDRE688574', 20)
    self._SetHeadSkipSegment('SPIK688185', 20)
    self._SetHeadSkipSegment('ZPIV649500', 20)
    self._SetHeadSkipSegment('PQJV528786', 20)
    self._SetHeadSkipSegment('ZPPL111014', 20)
    self._SetHeadSkipSegment('GNHF241425', 20)
    self._SetHeadSkipSegment('WKPA350096', 20)
    self._SetHeadSkipSegment('PCWK390446', 20)
    self._SetHeadSkipSegment('LASS613096', 20)
    self._SetHeadSkipSegment('QPNZ141847', 20)
    self._SetHeadSkipSegment('EDWS983124', 20)
    # 电视剧10秒
    self._SetHeadSkipSegment('AYID779015', 10)
    self._SetHeadSkipSegment('KUBE306727', 10)
    self._SetHeadSkipSegment('MGQD904488', 10)
    self._SetHeadSkipSegment('QWAB148492', 10)
    self._SetHeadSkipSegment('SZVN102763 ', 10)
    self._SetHeadSkipSegment('UZIY995878', 10)
    self._SetHeadSkipSegment('KRYY417400', 10)
    self._SetHeadSkipSegment('YLGH406654', 10)
    self._SetHeadSkipSegment('OMEP848886', 10)
    self._SetHeadSkipSegment('IYTG513602', 10)
    self._SetHeadSkipSegment('JFRJ881575', 10)
    self._SetHeadSkipSegment('RNHA909484', 10)
    self._SetHeadSkipSegment('RIAH777193', 10)
    self._SetHeadSkipSegment('VTXD727067', 10)
    self._SetHeadSkipSegment('CYWD818677', 10)
    self._SetHeadSkipSegment('HUBY905161', 10)
    self._SetHeadSkipSegment('ZGXJ549061', 10)
    self._SetHeadSkipSegment('JXXT256235', 10)
    self._SetHeadSkipSegment('HBHF409555', 10)
    self._SetHeadSkipSegment('DLTI422338', 10)
    self._SetHeadSkipSegment('EDJX218751', 10)
    self._SetHeadSkipSegment('TIQM459983', 10)
    self._SetHeadSkipSegment('XOVV214319', 10)
    self._SetHeadSkipSegment('XMWN505894', 10)
    self._SetHeadSkipSegment('TRAG739786', 10)
    self._SetHeadSkipSegment('AJUJ913860', 10)
    self._SetHeadSkipSegment('ZRDJ596186', 10)
    self._SetHeadSkipSegment('PHBH202466', 10)
    self._SetHeadSkipSegment('TIWS645015', 10)
    self._SetHeadSkipSegment('YPRE960726', 10)
    self._SetHeadSkipSegment('WTUD651271', 10)
    self._SetHeadSkipSegment('JPXR568150', 10)
    self._SetHeadSkipSegment('PNBC845744', 10)
    self._SetHeadSkipSegment('HFUJ379656', 10)
    self._SetHeadSkipSegment('VOCJ161338', 10)
    self._SetHeadSkipSegment('FKLV213508', 10)
    self._SetHeadSkipSegment('OAJO550354', 10)
    self._SetHeadSkipSegment('XAXF401282', 10)
    self._SetHeadSkipSegment('JUUO150145', 10)
    self._SetHeadSkipSegment('CJTC517281', 10)
    self._SetHeadSkipSegment('DJAD189046', 10)
    self._SetHeadSkipSegment('CMMY121111', 10)
    self._SetHeadSkipSegment('JLZC421162', 10)
    self._SetHeadSkipSegment('GQMM416565', 10)
    self._SetHeadSkipSegment('OUZM116346', 10)
    self._SetHeadSkipSegment('AAIH448137', 10)
    self._SetHeadSkipSegment('EZSL528350', 10)
    self._SetHeadSkipSegment('DZMY442960', 10)
    self._SetHeadSkipSegment('XMVZ510528', 10)
    self._SetHeadSkipSegment('ZTEL486977', 10)
    self._SetHeadSkipSegment('ZSRF218492', 10)
    self._SetHeadSkipSegment('PANH244687', 10)
    self._SetHeadSkipSegment('SFJO526973 ', 10)
    self._SetHeadSkipSegment('OOZI837026', 10)
    self._SetHeadSkipSegment('RECY965255 ', 10)
    self._SetHeadSkipSegment('ZVIA209228', 10)
    self._SetHeadSkipSegment('CORU898084', 10)
    self._SetHeadSkipSegment(' GCCK004417', 10)
    self._SetHeadSkipSegment('VUGU219372', 10)
    self._SetHeadSkipSegment('DBHP781626', 10)
    self._SetHeadSkipSegment('FTSI586271', 10)
    self._SetHeadSkipSegment('LOVP840167', 10)
    self._SetHeadSkipSegment('OLIA079052', 10)
    self._SetHeadSkipSegment('VSLR848434', 10)
    self._SetHeadSkipSegment('TTAK776080', 10)
    self._SetHeadSkipSegment('OOJH728667', 10)
    self._SetHeadSkipSegment('ILTJ275627', 10)
    self._SetHeadSkipSegment('KZZP313997', 10)
    self._SetHeadSkipSegment('LXAA235766', 10)
    self._SetHeadSkipSegment('PRZV311589', 10)
    self._SetHeadSkipSegment('EIAK837880', 10)
    self._SetHeadSkipSegment('OOFD995127', 10)
    self._SetHeadSkipSegment('SSLV396064', 10)
    self._SetHeadSkipSegment('LTNM921984', 10)
    self._SetHeadSkipSegment('PIBK683322', 10)
    self._SetHeadSkipSegment('LAIN634420', 10)
    self._SetHeadSkipSegment('PGQF534903', 10)
    self._SetHeadSkipSegment('MFSV860422', 10)
    self._SetHeadSkipSegment('EMTQ315958', 10)
    self._SetHeadSkipSegment('OEXL662989', 10)
    self._SetHeadSkipSegment('KHCO774640', 10)
    self._SetHeadSkipSegment('JPYW173793', 10)
    self._SetHeadSkipSegment('VPTM330250', 10)
    self._SetHeadSkipSegment('QHWR119183', 10)
    self._SetHeadSkipSegment('TCPN971463', 10)
    self._SetHeadSkipSegment('WVXD640371', 10)
    self._SetHeadSkipSegment('TNCE143448', 10)
    self._SetHeadSkipSegment('TNCE143448', 10)
    self._SetHeadSkipSegment('BMHT227183', 10)
    self._SetHeadSkipSegment('NWUO219263', 10)
    self._SetHeadSkipSegment('GKFR484746', 10)
    self._SetHeadSkipSegment('TCJM887887', 10)
    self._SetHeadSkipSegment('MXTP589145', 10)
    self._SetHeadSkipSegment('TICC150952', 10)
    self._SetHeadSkipSegment('GDXR057616', 10)
    self._SetHeadSkipSegment('VUAY490263', 10)
    self._SetHeadSkipSegment('OJEK572260', 10)
    self._SetHeadSkipSegment('UEED601514', 10)
    self._SetHeadSkipSegment('BFKM363923', 10)
    self._SetHeadSkipSegment('ZTSC892055', 10)
    self._SetHeadSkipSegment('OKTS328033', 10)
    self._SetHeadSkipSegment('BSRG076203', 10)
    self._SetHeadSkipSegment('OFRR377529', 10)
    self._SetHeadSkipSegment('IJOD440416', 10)
    self._SetHeadSkipSegment('RVIS948051', 10)
    self._SetHeadSkipSegment('LPUY187131', 10)
    self._SetHeadSkipSegment('BHZN782628', 10)
    self._SetHeadSkipSegment('EDPU432615', 10)
    self._SetHeadSkipSegment('NUJA011207', 10)
    self._SetHeadSkipSegment('JRMU688452', 10)
    self._SetHeadSkipSegment('XWBY038459', 10)
    self._SetHeadSkipSegment('BNFX633329', 10)
    self._SetHeadSkipSegment('GRMS732173', 10)
    self._SetHeadSkipSegment('BJZE827566', 10)
    self._SetHeadSkipSegment('KLSE399881', 10)
    self._SetHeadSkipSegment('WUJG044221', 10)
    self._SetHeadSkipSegment('JZML261087', 10)
    self._SetHeadSkipSegment('ADCL243777', 10)
    self._SetHeadSkipSegment('ZPVD486913', 10)
    self._SetHeadSkipSegment('VUUJ389291', 10)
    self._SetHeadSkipSegment('MWNO305228', 10)
    self._SetHeadSkipSegment('UJRK328457', 10)
    self._SetHeadSkipSegment('SEXF512942', 10)
    self._SetHeadSkipSegment('EQMG236647', 10)
    self._SetHeadSkipSegment('FDVE843682', 10)
    self._SetHeadSkipSegment('RWLZ143152', 10)
    self._SetHeadSkipSegment('BVVH921381', 10)
    self._SetHeadSkipSegment('AKRM403873', 10)
    self._SetHeadSkipSegment('IEZQ875140', 10)
    self._SetHeadSkipSegment('EMDE818668', 10)
    self._SetHeadSkipSegment('MWIJ939898', 10)
    self._SetHeadSkipSegment('EMWJ355563', 10)
    self._SetHeadSkipSegment('LTLL207183', 10)
    self._SetHeadSkipSegment('MIIX162049', 10)
    self._SetHeadSkipSegment('DBOG174770', 10)
    self._SetHeadSkipSegment('GAZZ043056', 10)
    self._SetHeadSkipSegment('IYID091583', 10)
    self._SetHeadSkipSegment('QFOB067979', 10)
    self._SetHeadSkipSegment('TRMI028044', 10)
    self._SetHeadSkipSegment('RNMW643630', 10)
    self._SetHeadSkipSegment('LLQO577626', 10)
    self._SetHeadSkipSegment('SUDQ118299', 10)
    self._SetHeadSkipSegment('QAGM625539', 10)
    self._SetHeadSkipSegment('RZPN801932', 10)
    self._SetHeadSkipSegment('FWVQ562188', 10)
    self._SetHeadSkipSegment('NJCW770907', 10)
    self._SetHeadSkipSegment('VEMY837982', 10)
    self._SetHeadSkipSegment('DCSJ406670', 10)
    self._SetHeadSkipSegment('RFEQ602646', 10)
    self._SetHeadSkipSegment('HFUR184196', 10)
    self._SetHeadSkipSegment('IKPH928727', 10)
    self._SetHeadSkipSegment('UHTT296187', 10)
    self._SetHeadSkipSegment('KQHS314734', 10)
    self._SetHeadSkipSegment('SSRT533772', 10)
    self._SetHeadSkipSegment('VZUR500698', 10)
    self._SetHeadSkipSegment('IPNR997983', 10)
    self._SetHeadSkipSegment('DJJP301502', 10)
    self._SetHeadSkipSegment('EDZG147890', 10)
    self._SetHeadSkipSegment('QNJR271714', 10)
    self._SetHeadSkipSegment('PSVF031865', 10)
    self._SetHeadSkipSegment('QXHD821581', 10)
    self._SetHeadSkipSegment('DQLN914993', 10)
    self._SetHeadSkipSegment('EVCZ627899', 10)
    self._SetHeadSkipSegment('EZHM205439', 10)
    self._SetHeadSkipSegment('MNJM343404', 10)
    self._SetHeadSkipSegment('PQIH799242', 10)
    self._SetHeadSkipSegment('CQKV333320', 10)
    self._SetHeadSkipSegment('IOQP861388', 10)
    self._SetHeadSkipSegment('AVXO920498', 10)
    self._SetHeadSkipSegment('NKUF361841', 10)
    self._SetHeadSkipSegment('TUGA357850', 10)
    self._SetHeadSkipSegment('VECP375992', 10)
    self._SetHeadSkipSegment('DBEG154007', 10)
    self._SetHeadSkipSegment('NYVN135837', 10)
    self._SetHeadSkipSegment('AXDR835895', 10)
    self._SetHeadSkipSegment('DFPI793326', 10)
    self._SetHeadSkipSegment('LNRG430321', 10)
    self._SetHeadSkipSegment('CJTB621542', 10)
    self._SetHeadSkipSegment('KXRA121032', 10)
    self._SetHeadSkipSegment('STSK726207 ', 10)
    self._SetHeadSkipSegment('FWAH928229', 10)
    self._SetHeadSkipSegment('MJDK924401', 10)
    self._SetHeadSkipSegment('VWLC633210', 10)
    self._SetHeadSkipSegment('RVQB865647', 10)
    self._SetHeadSkipSegment('EIMD104330', 10)
    self._SetHeadSkipSegment('VEKF891454', 10)
    self._SetHeadSkipSegment('MLFN970295', 10)
    self._SetHeadSkipSegment('IUHG252931', 10)
    self._SetHeadSkipSegment('BOZQ211384', 10)
    self._SetHeadSkipSegment('ZHTS121045', 10)
    self._SetHeadSkipSegment('SUJO510298', 10)
    self._SetHeadSkipSegment('BUIP096206', 10)
    self._SetHeadSkipSegment('POYH157941', 10)
    self._SetHeadSkipSegment('AVBR886580', 10)
    self._SetHeadSkipSegment('CKKM224806', 10)
    self._SetHeadSkipSegment('WMZF136929', 10)
    self._SetHeadSkipSegment('EGSX095921', 10)
    self._SetHeadSkipSegment('JZNC201750', 10)
    self._SetHeadSkipSegment('NMRB142831', 10)
    self._SetHeadSkipSegment('YJFO843025', 10)
    self._SetHeadSkipSegment('VQNJ120527', 10)
    self._SetHeadSkipSegment('MBPI987587', 10)
    self._SetHeadSkipSegment('PEKM631483', 10)
    self._SetHeadSkipSegment('SQIP918411', 10)
    self._SetHeadSkipSegment('MWMM976165', 10)
    self._SetHeadSkipSegment('KLTM370872', 10)
    self._SetHeadSkipSegment('AGEP514155', 10)
    self._SetHeadSkipSegment('XOCS182301', 10)
    self._SetHeadSkipSegment('MCCZ138350', 10)
    self._SetHeadSkipSegment('RWDF025141', 10)
    self._SetHeadSkipSegment('PZTQ055080', 10)
    self._SetHeadSkipSegment('UAUZ376371', 10)
    self._SetHeadSkipSegment('YXPR069907', 10)
    self._SetHeadSkipSegment('QRDH760699', 10)
    self._SetHeadSkipSegment('CSQF502747', 10)
    self._SetHeadSkipSegment('CLJS276644', 10)
    self._SetHeadSkipSegment('LSVG514742', 10)
    self._SetHeadSkipSegment('IYYB026937', 10)
    self._SetHeadSkipSegment('YYLM675219', 10)
    self._SetHeadSkipSegment('LDDZ452890', 10)
    self._SetHeadSkipSegment('WZKF776874', 10)
    self._SetHeadSkipSegment('YLAY268917', 10)
    self._SetHeadSkipSegment('OKDF827005', 10)
    self._SetHeadSkipSegment('SQDK173424', 10)
    self._SetHeadSkipSegment('UKYK922541', 10)
    self._SetHeadSkipSegment('NMAE968486', 10)
    self._SetHeadSkipSegment('ZMZU855272', 10)
    self._SetHeadSkipSegment('NEBA076239', 10)
    self._SetHeadSkipSegment('YYCH194078', 10)
    self._SetHeadSkipSegment('FRRY066289', 10)
    self._SetHeadSkipSegment('CTNG953742', 10)
    self._SetHeadSkipSegment('NOOT979572', 10)
    self._SetHeadSkipSegment('WZMU807758', 10)
    self._SetHeadSkipSegment('YOPK615468', 10)
    self._SetHeadSkipSegment('GHXM057423', 10)
    self._SetHeadSkipSegment('MKPR406318', 10)
    self._SetHeadSkipSegment('GDJT641839', 10)
    self._SetHeadSkipSegment('ENXC022189', 10)
    self._SetHeadSkipSegment('ZCFY038101', 10)
    self._SetHeadSkipSegment('OFJS560705', 10)
    self._SetHeadSkipSegment('BFTD407202', 10)
    self._SetHeadSkipSegment('UTUG334399', 10)
    self._SetHeadSkipSegment('XPXT647874', 10)
    self._SetHeadSkipSegment('GZWO214641', 10)
    self._SetHeadSkipSegment('ZOQA804592', 10)
    self._SetHeadSkipSegment('OVUW196708', 10)
    self._SetHeadSkipSegment('SSVA238696', 10)
    self._SetHeadSkipSegment('QHHI710184', 10)
    self._SetHeadSkipSegment('CJVM546572', 10)
    self._SetHeadSkipSegment('MBHO560437', 10)
    self._SetHeadSkipSegment('GQAC758485', 10)
    self._SetHeadSkipSegment('MNCH785363', 10)
    self._SetHeadSkipSegment('ETBF189836', 10)
    self._SetHeadSkipSegment('EYFG484671', 10)
    self._SetHeadSkipSegment('MJGT370316', 10)
    self._SetHeadSkipSegment('EQDD546001', 10)
    self._SetHeadSkipSegment('DAKN015324', 10)
    self._SetHeadSkipSegment('TPPR414931', 10)
    self._SetHeadSkipSegment('JCLX466950', 10)
    self._SetHeadSkipSegment('GMWP176546', 10)
    self._SetHeadSkipSegment('SZJP333487', 10)
    self._SetHeadSkipSegment('RUZZ842310', 10)

    # 临时10秒
    self._SetHeadSkipSegment('NMMF145697', 10)
    self._SetHeadSkipSegment('KOUH619146', 10)
    self._SetHeadSkipSegment('BZLJ078810', 10)
    self._SetHeadSkipSegment('PFGK766441', 10)
    self._SetHeadSkipSegment('RHNW291682', 10)
    self._SetHeadSkipSegment('KYCM226161', 10)
    self._SetHeadSkipSegment('MGCO435029', 10)
    self._SetHeadSkipSegment('EHNK141840', 10)
    self._SetHeadSkipSegment('JXPQ321233', 10)
    self._SetHeadSkipSegment('RPPA086686', 10)
    self._SetHeadSkipSegment('EKVE535183', 10)
    self._SetHeadSkipSegment('FBHY865061', 10)
    self._SetHeadSkipSegment('GTJU496775', 10)
    self._SetHeadSkipSegment('COKE299330', 10)
  #}

  def _SetHeadSkipSegment(self, sCmsCode, nDur):
  #{
    self.m_dictSkipSegment['head'][sCmsCode] = nDur
    #if self.m_dictSkipSegment['head'].has_key(sCmsCode):
    #{
    #  nDurO = self.m_dictSkipSegment['head'][sCmsCode]
    #  self.m_dictSkipSegment['head'][sCmsCode] = nDurO + nDur
    #}
    #else:
    #{
    #  self.m_dictSkipSegment['head'][sCmsCode] = nDur
    #}
  #}

  def GetHeadSkipDur(self, sCmsCode):
  #{
    if self.m_dictSkipSegment['head'].has_key(sCmsCode):
    # {
      return self.m_dictSkipSegment['head'][sCmsCode]
    # }
    return 0
  #}
#}

#-------------------------------------------------------#
if __name__ == '__main__':
  ms = CM3u8Spec()
  nDur = ms.GetHeadSkipDur('test')
  print nDur
  #print sData

