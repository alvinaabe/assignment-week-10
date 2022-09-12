 waktu impor
 permintaan impor
impor  os
dari  dotenv  impor  load_dotenv

load_dotenv

# TOKEN = "..." # Letakkan TOKEN Anda di sini
TOKEN  =  os . getenv ( 'TOKEN' ) # Letakkan TOKEN Anda di sini
# DEVICE_LABEL = "mesin" # Letakkan label perangkat Anda di sini
DEVICE_LABEL  =  os . getenv ( 'LABEL' )   # Letakkan label perangkat Anda di sini
# VARIABLE_LABEL_1 = "suhu" # Letakkan label variabel pertama Anda di sini
VARIABLE_LABEL_1  =  os . getenv ( 'VARIABLE' )   # Letakkan label variabel pertama Anda di sini
VARIABLE_LABEL_2  =  os . getenv ( 'VARIABLE2' ) # Letakkan label variabel kedua Anda di sini
VARIABLE_LABEL_3 =   os . getenv ( 'VARIABLE3' ) # Letakkan label variabel kedua Anda di sini



def  build_payload ( variabel_1 , keranjang1 , variabel_2 , keranjang2 , variabel_3 , keranjang3 ):
    # Membuat dua nilai acak untuk mengirim data
    nilai_1  =  keranjang1
    nilai_2  =  keranjang2
    nilai_3  =  keranjang3

    # Membuat koordinat gps acak
    # lat = random.randrange(34, 36, 1) + \
    # random.randrange(1, 1000, 1) / 1000.0
    # lng = random.randrange(-83, -87, -1) + \
    # random.randrange(1, 1000, 1) / 1000.0
    # payload = {variabel_1: nilai_1,
    # variabel_2: nilai_2,
    # variabel_3: {"nilai": 1, "konteks": {"lat": lat, "lng": lng}}}
    muatan  = { variabel_1 : nilai_1 ,
               variabel_2 : nilai_2 ,
               variabel_3 : nilai_3
    
    }

    mengembalikan  muatan

# def build_payload(variabel_1):
# # Membuat dua nilai acak untuk mengirim data
# nilai_1 = Suhu_1.get_data()
# # nilai_2 = random.randint(0, 85)

# # Membuat koordinat gps acak
# # lat = random.randrange(34, 36, 1) + \
# # random.randrange(1, 1000, 1) / 1000.0
# # lng = random.randrange(-83, -87, -1) + \
# # random.randrange(1, 1000, 1) / 1000.0
# # payload = {variabel_1: nilai_1,
# # variabel_2: nilai_2,
# # variabel_3: {"nilai": 1, "konteks": {"lat": lat, "lng": lng}}}
# payload = {'variabel': variabel_1,
# 'nilai':nilai_1}

# kembalikan muatan



def  post_request ( payload ):
    # Membuat header untuk permintaan HTTP
    coba :
        url  =  "http://industrial.api.ubidots.com/api/v1.6/devices/" +  DEVICE_LABEL  + "/" 
        headers  = { "X-Auth-Token" : TOKEN , "Content-Type" : "application/json" }

        # Membuat permintaan HTTP
        req  =  permintaan . posting ( url = url , header = header , json = payload )
        status  =  permintaan . Kode status
        waktu . tidur ( 1 )

        # Memproses hasil
        print ( req .status_code , req .json ( ) )
        jika  status  >=  400 :
            print ( "[ERROR] Tidak dapat mengirim data setelah 5 kali percobaan, silakan periksa \
                kredensial token Anda dan koneksi internet" )
            lulus

        print ( "permintaan [INFO] dibuat dengan benar, perangkat Anda diperbarui" )
        kembali  Benar
    kecuali :
        print ( "Tidak dapat mengirim ke ubidots" )
        lulus

# def post_request(payload):
# mencoba:
# api = ApiClient(token=TOKEN) # Ganti dengan Token Ubidots Anda di sini
# api.save_collection([payload])
# # api.save_collection(payload)
# print('dikirim ke ubidots')
# kecuali:
# print('masalah di ubidots')
# lulus




def  send_data ( keranjang1 , keranjang2 , keranjang3 ):
    muatan  =  build_payload (
         VARIABLE_LABEL_1 , VARIABLE_LABEL_2 , VARIABLE_LABEL_3 )

    # payload = build_payload(
    # VARIABLE_ID)

    print ( "[INFO] Mencoba mengirim data" )
    cetak ( muatan )
    post_request ( payload )
    print ( "[INFO] selesai" )


# jika __name__ == '__main__':
    #sementara (Benar):
    # utama()
    # waktu.tidur(1)
