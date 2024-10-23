# TESTATAAN MODUULIN identityCheck2.py LUOKKIEN TOIMINTAA

import identityCheck2

testSsnOK = identityCheck2.NationalSSN('130728-478N')
testSsnShort = identityCheck2.NationalSSN('130728-78N')
testSsnLong = identityCheck2.NationalSSN('1300728-478N')

def test_checkSsnLenghtOk():
    assert testSsnOK.checkSsnLenghtOk() == True
    assert testSsnShort.checkSsnLenghtOk() == False
    assert testSsnLong.checkSsnLenghtOk() == False