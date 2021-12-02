from brownie import chain, Contract
from cachetools.func import ttl_cache

if chain.id == 1:
    feeds = {
        "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599": Contract("0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c"),  # wbtc
        "0x514910771AF9Ca656af840dff83E8264EcF986CA": Contract("0x2c1d072e956AFFC0D435Cb7AC38EF18d24d9127c"),  # link
        "0x584bC13c7D411c00c01A62e8019472dE68768430": Contract("0xBFC189aC214E6A4a35EBC281ad15669619b75534"),  # hegic
        "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9": Contract("0x547a514d5e3769680Ce22B2361c10Ea13619e8a9"),  # aave
        "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2": Contract("0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419"),  # weth
        "0xc00e94Cb662C3520282E6f5717214004A7f26888": Contract("0xdbd020CAeF83eFd542f4De03e3cF0C28A4428bd5"),  # comp
        "0xdB25f211AB05b1c97D595516F45794528a807ad8": Contract("0xb49f677943BC038e9857d61E7d053CaA2C1734C1"),  # eurs
        "0xC581b735A1688071A1746c968e0798D642EDE491": Contract("0xb49f677943BC038e9857d61E7d053CaA2C1734C1"),  # eurt
        "0xD71eCFF9342A5Ced620049e616c5035F1dB98620": Contract("0xb49f677943BC038e9857d61E7d053CaA2C1734C1"),  # seur
        "0x5555f75e3d5278082200Fb451D1b6bA946D8e13b": Contract("0xBcE206caE7f0ec07b545EddE332A47C2F75bbeb3"),  # ibjpy
        "0xFAFdF0C4c1CB09d430Bf88c75D88BB46DAe09967": Contract("0x77F9710E7d0A19669A13c055F62cd80d313dF022"),  # ibaud
        "0x69681f8fde45345C3870BCD5eaf4A05a60E7D227": Contract("0x5c0Ab2d9b5a7ed9f470386e82BB36A3613cDd4b5"),  # ibgbp
        "0x1CC481cE2BD2EC7Bf67d1Be64d4878b16078F309": Contract("0x449d117117838fFA61263B61dA6301AA2a88B13A"),  # ibchf
        "0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e": Contract("0xA027702dbb89fbd58938e4324ac03B58d812b0E1"),  # yfi
        # NOTE: These coins don't have oracles but we can use the oracle for the base token
        "0x9AFb950948c2370975fb91a441F36FDC02737cD4": Contract("0x1A31D42149e82Eb99777f903C08A2E41A00085d3"),  # hfil
        "0x5CAF29fD8efbe4ED0cfc43A8a211B276E9889583": Contract("0x1A31D42149e82Eb99777f903C08A2E41A00085d3"),  # renfil
        "0x95dFDC8161832e4fF7816aC4B6367CE201538253": Contract("0x01435677fb11763550905594a16b645847c1d0f3"),  # ibKRW
        "0xfE18be6b3Bd88A2D2A7f928d00292E7a9963CfC6": Contract("0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c"),  # sbtc
        "0xEB4C2781e4ebA804CE9a9803C67d0893436bB27D": Contract("0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c"),  # renbtc
        "0x1C5db575E2Ff833E46a2E9864C22F4B22E0B37C2": Contract("0xd54B033D48d0475f19c5fccf7484E8A981848501"),  # renzec
        "0x459086F2376525BdCebA5bDDA135e4E9d3FeF5bf": Contract("0x9F0F69428F923D6c95B781F89E165C9b2df9789D"),  # renbch
        "0x3832d2F059E55934220881F831bE501D180671A7": Contract("0x2465CefD3b488BE410b941b1d4b2767088e2A028"),  # rendoge
        "0x9fcf418B971134625CdF38448B949C8640971671": Contract("0xb49f677943BC038e9857d61E7d053CaA2C1734C1"),  # eurn
        "0x945Facb997494CC2570096c74b5F66A3507330a1": Contract("0xF4030086522a5bEEa4988F8cA5B36dbC97BeE88c"),  # mbtc
    }
elif chain.id == 56:
    feeds = {
        "0xfCe146bF3146100cfe5dB4129cf6C82b0eF4Ad8c": Contract("0x264990fbd0A4796A3E3d8E37C4d5F87a3aCa5Ebf"),  # renbtc
        "0xA164B067193bd119933e5C1e7877421FCE53D3E5": Contract("0x43d80f616DAf0b0B42a928EeD32147dC59027D41"),  # renbch
        "0xDBf31dF14B66535aF65AaC99C32e9eA844e14501": Contract("0xE5dbFD9003bFf9dF5feB2f4F445Ca00fb121fb83"),  # renfil
        "0xc3fEd6eB39178A541D274e6Fc748d48f0Ca01CC3": Contract("0x3AB0A0d137D4F946fBB19eecc6e92E64660231C8"),  # rendoge
    }
elif chain.id == 137:
    feeds = {
        "0xDBf31dF14B66535aF65AaC99C32e9eA844e14501": Contract("0xc907E116054Ad103354f2D350FD2514433D57F6f"),  # renbtc
        "0xc3fEd6eB39178A541D274e6Fc748d48f0Ca01CC3": Contract("0x327d9822e9932996f55b39F557AEC838313da8b7"),  # renbch
        "0x31a0D1A199631D244761EEba67e8501296d2E383": Contract("0xBC08c639e579a391C4228F20d0C29d0690092DF0"),  # renzec
        "0xcE829A89d4A55a63418bcC43F00145adef0eDB8E": Contract("0xbaf9327b6564454F4a3364C33eFeEf032b4b4444"),  # rendoge
        "0x7c7DAAF2dB46fEFd067f002a69FD0BE14AeB159f": Contract("0x1248573D9B62AC86a3ca02aBC6Abe6d403Cd1034"),  # renluna
        "0x7BDF330f423Ea880FF95fC41A280fD5eCFD3D09f": Contract("0x73366Fe0AA0Ded304479862808e02506FE556a98"),  # eurt
    }
elif chain.id == 250:
    feeds = {
        "0xDBf31dF14B66535aF65AaC99C32e9eA844e14501": Contract("0x8e94C22142F4A64b99022ccDd994f4e9EC86E4B4"),  # renbtc
    }

@ttl_cache(ttl=600)
def get_price(asset, block=None):
    try:
        return feeds[asset].latestAnswer(block_identifier=block) / 1e8
    except (KeyError, ValueError):
        return None
