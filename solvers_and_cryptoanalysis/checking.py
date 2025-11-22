import math
from string import ascii_uppercase
from typing import Iterable

PP_freq = {'A': 0.0774016898062627, 'B': 0.0168531760692496,
           'C': 0.025614686881730825, 'D': 0.04095553123241224,
           'E': 0.128536111235796, 'F': 0.022436373304237638,
           'G': 0.019002551628173565, 'H': 0.06243029635486622,
           'I': 0.07112447733056187, 'J': 0.0017505757564248202,
           'K': 0.006037242031772777, 'L': 0.04052738252669887,
           'M': 0.02706486798172772, 'N': 0.07024055742199234,
           'O': 0.07489322178448238, 'P': 0.0158052475838947,
           'Q': 0.0011394280071404155, 'R': 0.0607142487198699,
           'S': 0.06162579112558223, 'T': 0.08776530545302622,
           'U': 0.02814559818243969, 'V': 0.010562152344977366,
           'W': 0.02247262783173756, 'X': 0.0017816510657104679,
           'Y': 0.023442868043878337, 'Z': 0.0016763402953535508}
# Letter Frequency of Pride and Prejudice


def consecutive_freq(text: str, length: int = 4) -> dict[str, int]:
    chunk_freq = {}

    for i in range(len(text) - length + 1):
        chunk = text[i:i+length]
        if chunk in chunk_freq:
            chunk_freq[chunk] += 1
        else:
            chunk_freq[chunk] = 1  # Creates chunk val

    # Return sorted list
    chunk_freq: dict[str, int] = dict(sorted(chunk_freq.items(),
                                             key=lambda x: x[1],
                                             reverse=True))

    return chunk_freq


def letter_freq_vector(text: str) -> dict[str, float]:
    text = text.upper()
    freq = {letter: 0 for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    total = 0

    for letter in text:
        if letter in freq:
            freq[letter] += 1
            total += 1

    if total == 0:
        return {letter: 0.0 for letter in freq}  # avoid division by zero

    return {k: v / total for k, v in freq.items()}


def shan_entropy(text: str) -> float:
    probs = letter_freq_vector(text)
    # iterate over probability values (floats) instead of dict keys
    return -sum(prob * math.log2(prob) for prob in probs.values() if prob > 0)


def cosine_angle(vector1: list[float], vector2: list[float]) -> float:
    # Dot product of both vectors
    dot = sum(a*b for a, b in zip(vector1, vector2))

    # Length of vector arrows using pythag
    norm1 = math.sqrt(sum(a*a for a in vector1))
    norm2 = math.sqrt(sum(b*b for b in vector2))

    # Cosine ratio of the vector's aligments
    angle_cosine = dot / (norm1 * norm2)

    # max and min used to prevent /0 crashes
    angle_cosine = max(-1, min(1, angle_cosine))
    angle_radians = math.acos(angle_cosine)  # Angle in radians
    angle_degrees = math.degrees(angle_radians)  # Angle in degrees

    return angle_degrees


def display_freq(freqs: dict[str, float]) -> None:
    for i in freqs:
        print(i, freqs[i])


def chisq(text: str, expected: dict[str, float]) -> tuple[str, float]:
    """
    Performs the chi-squared heuristic
    """
    value: float = 0
    alphabet = ascii_uppercase
    cleantext = text.upper().replace(" ", "")
    for letter in alphabet:
        nominalvalue: float = expected[letter]/100
        nominalvalue *= len(cleantext)

        value += ((cleantext.count(letter) - nominalvalue) ** 2)/(nominalvalue)
    return (text, value)


def chisqrank(solutions: Iterable[str],
              expected: dict[str, float] | None = None
              ) -> list[tuple[str, float]]:
    """
    Ranks proposed solutions with the chi-squared heuristic
    """
    ranking: list[tuple[str, float]] = []
    if expected is None:
        expected = {'E': 12.0, 'T': 9.10, 'A': 8.12,
                    'O': 7.68, 'I': 7.31, 'N': 6.95,
                    'S': 6.28, 'R': 6.02, 'H': 5.92,
                    'D': 4.32, 'L': 3.98, 'U': 2.88,
                    'C': 2.71, 'M': 2.61, 'F': 2.30,
                    'Y': 2.11, 'W': 2.09, 'G': 2.03,
                    'P': 1.82, 'B': 1.49, 'V': 1.11,
                    'K': 0.69, 'X': 0.17, 'Q': 0.11,
                    'J': 0.10, 'Z': 0.07}

    for solution in solutions:
        score = chisq(solution, expected)
        ranking.append(score)

    ranking = sorted(ranking, key=lambda x: x[1])
    return ranking


if __name__ == "__main__":
    # Testing
    """
    text = "I WISH I WISH WISH IS"

    text = text.replace(' ', '')

    display_freq(consecutive_freq(text, 4)) # Tetragram
    print("\n")
    print(shan_entropy(text),
          shan_entropy("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
          shan_entropy("AAAAAQAAAQAAA"), sep='\n')

    print(letter_freq_vector(text))
    """
    print(cosine_angle([1, 2, 3], [3, 2, 1]))
    import requests
    text = requests.get("https://www.gutenberg.org/cache/epub/1342/pg1342.txt").text  # Pride and Prejudice
    print(letter_freq_vector(text))

    text = """YLRPC CHGHS CHLYC UNJUG UJSZB CTJZB PWKGB EENGB CURGZ TJSLZ UECLR XIZSU IGBEP GKBDJ BGBDP JLCTU MCYLZ LSCRU BJZSL JGLJC JRLTL AUMLJ UNTLT JYTAC UILZC BIJYE BLBJG KLSLX GTDCI CJIJZ BUIRZ CTLMC HZLLG ZZKUU SZJIZ BCXDY LOLJJ JZULL AGDRL JEYBG JJLTG EECUC DAIZU ISGTJ BTSKJ IBTLE EBUIL AULSZ ZCGLX LPYZZ USLIG LTLMC HZLLT TSUXY UPDIL GIHRL PKBPG ALYTU ZCITJ YLLNP GICLJ UZBIR LTCTJ JLLDI LUNRJ TNTUU TAJIC NCLXH JCDBG JLITG JLCUE EARZC JBABG ALGJE PXXYS CLCII SJILT RJCLG LIMGB LGKFL USLGG JCLLJ CGJJZ LUAZB KBUGK PXITL NBMBG LZEBL JJLTL SLXGI YCTGI CLIUI JCRLJ ACJWJ BHTPP HBAGK BKDYJ CGLZP HRYGA PPBJD XUSBI RIJLU DIJTJ LLCGU ZPYRH JILLB EEGJI JTNPL LKLGZ XHCLR BJLGL JYLZU JZLTC GKJLJ EBTLJ LOJUJ AJZBC IZUJJ LTLZT AUCUA ZBTNH KBGSK JTIKB PGCXD ZCJIW JILTU MLLTJ NCTJJ LILYI LSCYT PCCHL MLLZL ZPGAD RLJKZ UISUM CSLZL GUALD GLTCJ RZTLI LCBLG EKBAG ZLIBG BJUIK BXURP EAUEK JJXBL GHCLD WGDCT INJUU GXXLI UIJCI KXZUX NAUTT ICALY CUCCG EUTJR CUYJS KJTZG LRYLZ UJMLT CLKXB TJEUZ LIRMC LBUGK CBTYD SZUJJ CTPBK BGKBP GUGEL NRZTJ CLIZB JLSUY TLHJC LXHIS SKLCJ IYURB ECAUJ ZBUBB PEKCY GAZUT LCTJJ ZCAGL IUJTJ BLCTA XZLXS AULCG DZBRU MLLZB KELIK JUXLE BYULJ ZXSUX LLAZJ JCTYT PCLUD XZALR ULTDG SZUJA LTKLI GRXLJ LCGSY NJUCD CIDLG CZPXJ IJZLE YBGJB LTEAU ELCEB ZPNLB HWGKZ UILYI ICPHZ JZLTC BLYEX UYXCG LZCYR PMCTL LLHZL GCDJP XBBZC JGLTY IILCE LSGIY BBBLY ZUILS ZUZSJ UNTLT JISZU XLXLJ GLJGK YUIBA JZCGS JCXKJ BPLKL JGAUZ TAZCU EYGBC ZUWSU TJIZB AZJAL UJZBT ZULJA GLLLJ DRILY ILSCJ UYBXG LXEYB GGICN LGAZP LJDRU IKZIC SUXDY LLCAI IGCTJ EUATD ULTNG UTTAC BZRZT JLLIL XIKCA ICRLI NBXRZ NBUTJ ZLDDC CJCGK NBIUJ SZBLT JEJAC JJCTJ JLTLT JOCLH RLXHZ BLWAR EZUUX LMLLJ JGBGS KNIDT LXUNJ UCUES ZBTJG LSZLU LLZGB JIJLZ KJYLT LCTAZ YIUJD IBLKR LDLTJ RGALP UJDBB PZKBA GXCLX SALKG WACLT JRCUA JDGLT HCTPZ ZCRRG LAJZU CCLDI ABIJE UJUZK XARSZ UJKLT IEBLC JUZCC UXZGB EYYEB ULXXG CZIYJ CLJAC GJTRL LJCGJ JZLUI ZBLUJ JZECS XJSCB ZBYUG BJYII LCILS EYBGJ ZLTLT SUHGK BTRBB BUEEA LXLRJ BJTUR LIMBA LBPGE UTJIO LJJTJ UUUWZ JDIUL CTGDB NIGLT JOUYC ZSZUE JGKTU GLEXZ BPTBJ LUDXY BGDMB PLKLY GAZCT URYIB LSR"""
    print(letter_freq_vector(text))
