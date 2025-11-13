from string import ascii_uppercase
from base_cipher import Cipher

class monoalphabetic_cipher(Cipher):
    def solve(self, key: str) -> str:
        if len(key) != 26:
            raise ValueError("Not all letters of the alphabet are covered by this key")

        letters = [[letter, 0] for letter in self.ciphertext]

        for i in range(26):
            for letter in letters:
                if letter[1] == 0 and letter[0] == ascii_uppercase[i]:
                    letter[0], letter[1] = key[i], 1

        return "".join(letter[0] for letter in letters)
    
    def intelligent_solve(self):
        raise NotImplementedError("Unfinished, throws an error")
        #TODO attempt this method: https://ti89.com/cryptotut/mono_crack.htm
        # STEP 1
        e_character = max(self.frequencies, key=self.frequencies.get)
        step1_substituted = self.ciphertext.replace(e_character, "e")
        # STEP 2
        fragmented_txt = step1_substituted.split(" ")
        for word in fragmented_txt:
            if len(word) == 3:
                if word[2] == "e":
                    t_character = word[0]
                    h_character = word[1]
        step2_substituted = step1_substituted.replace(t_character, "t").replace(h_character, "h")
        # MY STEPS FOR NOW
        # 3: Find a and i
        fragmented_txt = step2_substituted.split(" ")
        counts = {}
        for word in fragmented_txt:
            if len(word) == 1:
                print(word)
                try:
                    counts.update({word: counts[word]+1})
                except:
                    counts.update({word:1})
        print(counts)
        a_character = max(counts, key=counts.get)
        i_character = min(counts, key=counts.get) 
        step3_substituted = step2_substituted.replace(a_character, "a").replace(i_character, "i")
        # 4: Try and find r through assuming the most frequent a_e word = r
        fragmented_txt = step3_substituted.split(" ")
        counts = {}
        for word in fragmented_txt:
            if len(word) == 3:
                if word[0] == "a" and word[2] == "e":
                    try:
                        counts.update({word: counts[word]+1})
                    except:
                        counts.update({word:1})
        r_character = max(counts, key=counts.get)[1]
        step4_substituted = step3_substituted.replace(r_character, "r")
        

def solve(ciphertext:str, key:str):
    """
    With a given key solves a monoalphabetic substitution
    """
    cipher = monoalphabetic_cipher(ciphertext)
    return cipher.substitute(key)

if __name__ == "__main__":
    cipher = monoalphabetic_cipher("IFQFUDN EREIF, K JDYF HRNNRZFE BRXU ZRUM ZKWJ IUFDW KQWFUFVW DQE JDYF OFFQ PRVW KPSUFVVFE ZKWJ BRXU FQFUIFWKG EFYFNRSPFQW DQE SURPRWKRQ RH WJF QRUWJ DPFUKGDQ WFNFIUDSJKG VBVWFP. K JDYF VSFQW PDQB BFDUV VWXEBKQI PDWJFPDWKGV DQE FQIKQFFUKQI, EKVGXVVKQI WJF GJDNNFQIFV KQYRNYFE KQ FNFGWUKGDN WUDQVPKVVKRQ DQE VWRUDIF RH KQHRUPDWKRQ ZKWJ PB HUKFQE DQE GRNNFDIXF GJDUNFV ZJFDWVWRQF. K ZDV EFNKIJWFE ZJFQ BRX DSSURDGJFE PF ZKWJ BRXU SURSRVDN DQE JDYF VSFQW PDQB JRXUV EKVGXVVKQI KW ZKWJ PB GNRVFVW GRQHKEDQWFV. OFBRQE RXU GRPPRQ KQWFUFVWV DV PFQ RH VGKFQGF, BRXU NFWWFU GRQYKQGFE PF WJDW ZF DNVR VJDUF D GRQGFUQ HRU JXPDQKWB DQE NKOFUWB, DQE K WJKQM K GDQ VFF JRZ RXU GRPSNFPFQWDUB VMKNNV GRXNE SURHKWDONB GRPOKQF WR WJF OFQFHKW RH HUFF PFQ FYFUBZJFUF. K DP UFNXGWDQW WR GRPPKW PB GRPPFQWV RQ BRXU KEFD WR SDSFU, FYFQ VFGXUFE ZKWJ WJKV GKSJFU, SDUWNB OFGDXVF PB RZQ UFVFDUGJ JDV VJRZQ LXVW JRZ KNNXVKYF WJDW VFGXUKWB GDQ OF. IKYFQ WJRVF GRQGFUQV K ZRXNE SUFHFU WR EKVGXVV PDWWFUV KQ SFUVRQ, OXW K DP WRR RNE HRU WJF UKIRXUV RH DQ RGFDQ GURVVKQI. HRUWXQDWFNB, PB EFDU HUKFQE PU GJDUNFV EKGMFQV KV SNDQQKQI WR YKVKW BRXU GRXQWUB VJRUWNB, DQE K DP JRSKQI WJDW K ZKNN OF DONF WR SFUVXDEF JKP WR DGW DV DQ KQWFUPFEKDUB. JF KV UFNXGWDQW WR IFW KQYRNYFE KQ DHHDKUV RH VWDWF, OXW WJF SUKPF PKQKVWFU, NRUE EFUOB JDV KQEKGDWFE JKV VXSSRUW HRU BRXU VXIIFVWKRQ, DQE SFUJDSV JKV IKHW HRU SFUVXDVKRQ ZKNN FQGRXUDIF PU EKGMFQV WR FQIDIF ZKWJ XV. K JRSF BRX ZKNN QRW PKQE PF FPSJDVKVKQI WJF QFFE HRU GRPSNFWF GRQHKEFQWKDNKWB GRQGFUQKQI WJKV NFWWFU. KH BRX JDYF EFGKEFE RQ UFHNFGWKRQ QRW WR WDMF WJKV PDWWFU HXUWJFU, WJFQ SNFDVF EFVWURB WJKV SDSFU DQE ZF ZKNN VSFDM QR PRUF RQ WJKV VXOLFGW. KH, JRZFYFU, BRX DUF KQWFUFVWFE KQ EFYFNRSKQI BRXU KEFD HXUWJFU ZKWJ XV WJFQ K ZRXNE VXIIFVW DSSNBKQI RQF RH WJF PRUF VFGXUF PREFUQ GKSJFUV WR BRXU UFSNB. K ZKNN HXUQKVJ BRX ZKWJ VXKWDONB EKVIXKVFE MFBV OB WFNFIUDP. ZKWJ PB YFUB OFVW ZKVJFV, GJDUNFV ODOODIF")
    print(cipher.solve("JYQADECFGHIXKLBMNOPZRSTUVW"))