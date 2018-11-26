if __name__ == '__main__':

# Usage : python crabConfig.py (to create jobs)
#         ./multicrab -c status -d <work area> (to check job status)

    from CRABAPI.RawCommand import crabCommand
    from httplib import HTTPException

    from CRABClient.UserUtilities import config
    config = config()
    
    from multiprocessing import Process

    # Common configuration

    config.General.workArea     = 'crab_projects_ntuples_data'
    config.General.transferLogs = False
    config.JobType.pluginName   = 'Analysis' # PrivateMC
    config.JobType.psetName     = '/uscms_data/d3/aldas/ggntuple/CMSSW_9_4_9_cand2/src/ggAnalysis/ggNtuplizer/test/run_data2017_94X.py'
    #config.JobType.inputFiles   = ['Summer16_23Sep2016V4_MC_L2Relative_AK8PFchs.txt', 'Summer16_23Sep2016V4_MC_L3Absolute_AK8PFchs.txt', 'Summer16_23Sep2016V4_MC.db']
    #config.JobType.inputFiles   = ['Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt']
    config.JobType.sendExternalFolder = True
    config.Data.inputDBS        = 'global'    
    config.Data.splitting       = 'LumiBased' # EventBased, FileBased, LumiBased (1 lumi ~= 300 events)
    config.Data.lumiMask     = 'Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt'
    config.Data.totalUnits      = -1
    config.Data.publication     = False
    config.Site.storageSite     = 'T2_IN_TIFR'#'T3_US_FNALLPC' #'T2_CH_CERN'

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException, hte:
            print hte.headers

    # dataset dependent configuration

    config.General.requestName = 'data_ggntuples_F_Ele'
    config.Data.unitsPerJob    = 20
    #config.Data.inputDataset   = '/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD'
    #config.Data.inputDataset   = '/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD'
    #config.Data.inputDataset   = '/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD'
    #config.Data.inputDataset   = '/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD'
    #config.Data.inputDataset   = '/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD'
    #config.Data.inputDataset   = '/SingleElectron/Run2017B-31Mar2018-v1/MINIAOD'
    #config.Data.inputDataset   = '/SingleElectron/Run2017C-31Mar2018-v1/MINIAOD'
    #config.Data.inputDataset   = '/SingleElectron/Run2017D-31Mar2018-v1/MINIAOD'
    #config.Data.inputDataset   = '/SingleElectron/Run2017E-31Mar2018-v1/MINIAOD'
    config.Data.inputDataset   = '/SingleElectron/Run2017F-31Mar2018-v1/MINIAOD'
    

    config.Data.outLFNDirBase  = '/store/user/aldas/2017_gg/TTGamma'
    p = Process(target=submit, args=(config,))
    p.start()
    p.join()




