# app.py
from flask import Flask, render_template, request
import psycopg2
import psycopg2.extras 
import os
from dotenv import load_dotenv
from queries import RENK_SORGUSU_ISKELETI, TEK_TEDARIKCILI_URUN_SIPARISLERI, ORTALAMA_USTU_FIYAT_SORGUSU,EN_COK_SİPARİS_VEREN
load_dotenv()
app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD")
    )
    return conn


def handle_data_explorer_request(request):
    allowed_tables = ['tedarikci', 'parca', 'musteri', 'katalog', 'siparis']
    selected_table = request.args.get('table_to_show')

    context = {
        "table_names": allowed_tables,
        "selected_table": selected_table,
        "data": None,
        "columns": None,
        "explorer_open": False 
    }

    if selected_table and selected_table in allowed_tables:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute(f"SELECT * FROM {selected_table};")
        data = cur.fetchall()
        cur.close()
        conn.close()
        
        if data:
            context["data"] = data
            context["columns"] = list(data[0].keys())

       
        context["explorer_open"] = True
    
    return context

@app.route('/')
def index():
    
    explorer_context = handle_data_explorer_request(request)

   
    return render_template('index.html', **explorer_context)


@app.route('/analiz/en-cok-siparis')
def analiz_en_cok_siparis():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(EN_COK_SİPARİS_VEREN)
    sonuclar = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('analiz_en_cok_siparis.html', sonuclar=sonuclar)


@app.route('/analiz/renk', methods=['GET', 'POST'])
def analiz_renk():
    conn = get_db_connection()
   
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT renk FROM Parca WHERE renk IS NOT NULL ORDER BY renk;")
    tum_renkler = cur.fetchall()
    cur.close()

    sonuclar = None
    secilen_renkler = []

     
    if request.method == 'POST':
        secilen_renkler = request.form.getlist('renkler')
        if secilen_renkler:
            
            cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            renkler_tuple = tuple(secilen_renkler)
            cur.execute(RENK_SORGUSU_ISKELETI, (renkler_tuple,))
            sonuclar = cur.fetchall()
            cur.close()

    conn.close()
    
    return render_template('analiz_renk.html', 
                           tum_renkler=tum_renkler, 
                           sonuclar=sonuclar, 
                           secilen_renkler=secilen_renkler)


    
@app.route('/analiz/tek-tedarikci')
def analiz_tek_tedarikci():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(TEK_TEDARIKCILI_URUN_SIPARISLERI)
    sonuclar = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('analiz_tek_tedarikci.html', sonuclar=sonuclar)


   

@app.route('/analiz/ortalama-fiyat')
def analiz_ortalama_fiyat():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(ORTALAMA_USTU_FIYAT_SORGUSU)
    sonuclar = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('analiz_ortalama_fiyat.html', sonuclar=sonuclar)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True) 
