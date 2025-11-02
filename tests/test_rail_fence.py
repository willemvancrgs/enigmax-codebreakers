from cryptotools.rail_fence import *

def test_split():
    assert split("THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG", 5) == {0: 'TBJRD', 1: 'HKRXUETYO', 2: 'ECOOMVHZG', 3: 'QIWFPOEA', 4: 'UNSL'}
    assert split("I LOVE CIPHER CHALLENGE 2025", 2) == {0: 'ILV IHRCALNE22', 1: ' OECPE HLEG 05'}

def test_compose():
    assert compose({0: 'I WISH I WAS A ', 1: 'LITTLE BIT TALLER'}) == 'I WISH I WAS A LITTLE BIT TALLER'
    assert compose({0: 'I WOULD ', 1: 'I WISH I HAD A GIRL WHO ', 2: 'CALL HER', 3: 'LOOKED GOOD '}, [1, 3, 0, 2]) == 'I WISH I HAD A GIRL WHO LOOKED GOOD I WOULD CALL HER'