import sys
import MeCab

from lib.Miku import Miku
from time import sleep

def convert_katakana(text):
    mecab = MeCab.Tagger("-Ochasen")
    mecab.parse('')
    node =(mecab.parseToNode(text))

    text_list=[]
    while node :
        #print(node.surface+"\t"+node.feature)
        kana=node.feature.split(",")[7]
        text_list.append(kana)
        node=node.next

    return (''.join(text_list))[1:-1]


def pray_miku(text):

    try:
        miku = Miku()
        letter_list= []

        text = convert_katakana(text)

        for i in range(len(text)):
            if text[i] in miku.LETTERS:
                letter = miku.LETTERS[text[i]]
                letter_list.append(letter)

        miku.set_letter_list(letter_list)

        pitch=60 #声の高さ
        velocity=80
        for i in range(len(letter_list)):
            miku.note_onoff(pitch,velocity,"on")
            sleep(.200)
            miku.note_onoff(pitch,velocity,"off")

    except Exception as e:
        print(e)

    finally:
        miku.quit()

if __name__=='__main__':
    pray_miku("お寿司食べたい。")
