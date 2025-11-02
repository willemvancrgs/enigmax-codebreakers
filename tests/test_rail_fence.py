from cryptotools.rail_fence import *

def test_encrypt():
    assert encrypt("THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG", 5) == {0: 'TBJRD', 1: 'HKRXUETYO', 2: 'ECOOMVHZG', 3: 'QIWFPOEA', 4: 'UNSL'}
    assert encrypt("I LOVE CIPHER CHALLENGE 2025", 2) == {0: 'ILV IHRCALNE22', 1: ' OECPE HLEG 05'}
    assert encrypt("I LOVE ENIGMAX", 4, 5) == {0: ' EX', 1: 'IL NA', 2: 'OEIM', 3: 'VG'}

def test_compose():
    assert compose({0: 'I WISH I WAS A ', 1: 'LITTLE BIT TALLER'}) == 'I WISH I WAS A LITTLE BIT TALLER'
    assert compose({0: 'I WOULD ', 1: 'I WISH I HAD A GIRL WHO ', 2: 'CALL HER', 3: 'LOOKED GOOD '}, [1, 3, 0, 2]) == 'I WISH I HAD A GIRL WHO LOOKED GOOD I WOULD CALL HER'

def test_decrypt():
    # Rail fence tests
    assert decrypt("TEUCBONOJMSVRHLZDGHQIKRWFXUPOETEAYOS", 2, 0) == "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOGS"
    assert decrypt("VDTIOHAOEN ' OCBUPE NL AINHVEATIRRD E  AE S  C E IN5CCAE ER OVOI2E RLTMAEVOVG0RY PE ICE EM2TLMILGLNRDRA ANUTLN E NXILIFA", 10, 14) == "I LOVE ENIGMAX 2025 AND I CERTAINLY CAN'T HEAR MULTIPLE VOICES TELLING ME ABOUT RAIL FENCE CIPHER OVER AND OVER AND OVER"

    # Redefence tests
    assert decrypt("NGA EE GEIMSNVRAE", 2, 0, [1, 0]) == "ENIGMAS NEVER AGE"
    assert decrypt("ho ats wrsny rX aihpn  gttAn iaisisnrrmhnflhXBpeoralEmcikooealCaC, r ogrsne.Cte io,npso sl i ts iadwi", 5, 1, [2, 0, 4, 3, 1]) == "Charlotte Emma Aitchison, known professionally as Charli XCX, is a British pop singer and songwriter."
    assert decrypt(" ROMM UBRNYUR YB'NM NRM O' ,IOEE UO EIUONMR MIYE' ,B1NEUU R", 10, 16, [6, 8, 5, 0, 9, 1, 4, 3, 2, 7]) == "I'M YOUR NUMBER ONE, I'M YOUR NUMBER ONE, I'M YOUR NUMBER 1"