meme_dict = {"CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "tanggapan terhadap lelucon",
            "SHEESH": "sedikit ketidaksetujuan",
            "CREEPY": "menakutkan, tidak menyenangkan",
            }
            
word = input('masukan sebuah kata:')
word = word.upper()

for i in range(5):
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('tidak ada kata tersebut dalam data')
