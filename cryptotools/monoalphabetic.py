from string import ascii_uppercase
from base_cipher import cipher


class monoalphabetic_cipher(cipher):

    def solve(self, key:str):
        if len(key) != 26:
            raise ValueError("Not all letters of the alphabet are covered by this key")
        letters = []
        for letter in self.ciphertext:
            letters.append([letter, 0])
        for i in range(26):
            for letter in letters:
                if not letter[1] and letter[0] == ascii_uppercase[i]:
                    letter == [key[i], 1]
        result = ""
        for letter in letters:
            result = result + letter[0]
        return result
    
    def intelligent_solve(self):
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

cp = monoalphabetic_cipher("PZ ORFE XERSQDMMR, D PNHK FYVMVXDHR UVE LAFEMRH, AR DH F XVVO PFS, INK LFS IR DEFHLDIMR, FSO KEFQRM ERFMMZ OVRH SVK HNDK ADP. D ERFO ADH MRKKRE KV ZVN TDKA HVPR LVSLRES (KAFSJ ZVN UVE HRSODSX PR F LVYZ), HRRDSX KAFK DK ORPVSHKEFKRH F MVTSRHH DS ADH HYDEKH, INK D LFS FHHNER ZVN KAFK AR DSKRSOH VSMZ KAR IRHK UVE VNE RSORFQVNE. DK KVVJ KAR LVPIDSRO RUUVEKH VU PZHRMU FSO MVEO OREIZ KV LVSQDSLR ADP VU KAR EDXAKSRHH VU VNE YMFS, INK TADMR AR DH UNMMZ LVPPDKKRO KV VNE LFNHR, AR DH SVK RSKDERMZ FK RFHR TDKA VNE PRKAVOH. D AFQR LVSKDSNRO KV HVMDLDK HNYYVEK UVE ZVNE YEVYVHFM VS KADH HDOR VU KAR FKMFSKDL, FSO D FP LVSUDORSK KAFK PZ VTS HPFMM LVSKEDINKDVS LFS YMFZ FS DPYVEKFSK YFEK DS DKH HNLLRHH. D KENHK KAFK ZVNE XEVNY ERPFDSH LVSUDORSK KAFK DK LFS ORMDQRE VS DKH YEVPDHR. TDKA KAR HNYYVEK VU KAR IEDKDHA FSO FPREDLFS XVQRESPRSKH D KADSJ TR LVNMO INDMO HVPRKADSX RSKDERMZ SRT FSO RWKERPRMZ YVTREUNM, AVTRQRE KAR KENR YVKRSKDFM LFS VSMZ IR PRK DU TR LFS RSHNER KVKFM HRLERLZ, FSO D TDMM AFQR KV ERMZ VS ZVN KV YREHNFOR LAFEMRH SVK KV HYRFJ VU VNE ORHDXSH TDKA FSZVSR VNKHDOR VU VNE LDELMR. UVE ADH VTS YFEK, LAFEMRH DH LADRUMZ DSKRERHKRO DS KAR HNLLRHH VU ADH KVNE, FSO TADMR AR TDMM YMFZ FS DPYVEKFSK EVMR DS YREHNFODSX DSQRHKVEH KV GVDS VNE HLARPR FSO YVMDKDLDFSH KV HNYYVEK DK, DK DH DPYVEKFSK KAFK AR DH FMHV FIMR KV RSGVZ KAR UENDKH VU ADH ERFODSX YREUVEPFSLRH. AR DSQRHKH PNLA VU ADPHRMU DS KAVHR ERFODSXH FSO DH DSLMDSRO KV VQREKDER ADPHRMU. D KENHK KAFK ZVN FSO ZVNE UEDRSOH TDMM VUURE ADP KAR HNYYVEK KAFK D TVNMO VUURE DU D LVNMO IR KARER TDKA ADP. TDKAVNK KAFK HNYYVEK D URFE KAFK AR TDMM AFQR SV RSREXZ MRUK KV YEVPVKR VNE YEVGRLK. ZVNE UEDRSO, LAFEMRH IFIIFXR")
cp.intelligent_solve()