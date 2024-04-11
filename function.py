import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import pickle

def display_category_info(category_type):
    if category_type == "Accessories":
        st.subheader("Kategori Accessories")
        accessories_info = [
            "- Kategori Accessories merujuk pada berbagai jenis produk tambahan yang dirancang untuk melengkapi atau memperindah barang atau pakaian tertentu. ",
            "- Accessories ini termasuk perhiasan (seperti kalung, gelang, anting-anting), kacamata, topi, syal, dasi, selendang, ikat pinggang, dan tas tangan. ",
            "- Fashion accessories sering digunakan untuk menambahkan sentuhan gaya atau warna pada pakaian, serta untuk mempersonalisasi penampilan seseorang."
            ]
        st.markdown("\n".join(accessories_info))
    elif category_type == "Clothing":
        st.subheader("Kategori Clothing")
        clothing_info = [
            "- Kategori Clothing merujuk pada berbagai jenis pakaian yang dirancang untuk dikenakan oleh individu sebagai sarana penutup tubuh atau untuk tujuan tertentu, seperti gaya, perlindungan, atau kenyamanan.",
            "- Berikut adalah beberapa contoh kategori pakaian yang umum : ",
            "  1. Atasan (Tops): Ini mencakup berbagai jenis pakaian yang dikenakan di bagian atas tubuh, seperti kemeja, kaos, blouse, tank top, sweater, jaket, blazer, dan tunik.",
            "  2. Bawahan (Bottoms): Termasuk pakaian yang dikenakan di bagian bawah tubuh, seperti celana, rok, celana panjang, celana pendek, celana jeans, celana kulot, dan celana olahraga.",
            "  3. Pakaian Formal (Formalwear): Termasuk pakaian yang dipakai untuk acara-acara resmi atau formal, seperti jas pria, gaun malam, gaun pesta, gaun pengantin, dan setelan formal."
            ]
        st.markdown("\n".join(clothing_info))
    elif category_type == "Footwear":
        st.subheader("Kategori Footwear")
        footwear_info = [
            "- Kategori Footwear merujuk pada bebagai jenis alas kaki yang memiliki desain, fungsi, dan penggunaan yang unik. Pilihan footwear biasanya dipengarui oleh aktivitas sehari-hari dan gaya hidup.",
            "- Berikut adalah beberapa contoh kategori footwear yang umum digunakan :",
            "  1. **Sepatu Casual (Casual Shoes)**: Sepatu casual mencakup berbagai jenis sepatu yang dirancang untuk digunakan sehari-hari dalam situasi santai, seperti sneakers, sepatu slip-on, sepatu kanvas, dan sepatu boat.",
            "  2. **Sepatu Formal (Formal Shoes)**: Sepatu formal adalah sepatu yang dirancang untuk digunakan dalam situasi formal atau resmi, seperti acara bisnis, pesta, atau acara formal lainnya.",
            "  3. **Sepatu Olahraga (Athletic Shoes)**: Sepatu olahraga dirancang khusus untuk digunakan saat berolahraga atau aktivitas fisik. Ini mencakup sepatu lari, sepatu basket, sepatu tenis, sepatu futsal, sepatu hiking, dan sepatu golf, yang masing-masing dirancang dengan fitur-fitur yang sesuai untuk jenis olahraga tertentu.",
            "  4. **Sandals dan Flip-flops**: Sandal dan flip-flops adalah jenis alas kaki yang terbuka di bagian atas, sering kali digunakan di lingkungan yang lebih santai atau dalam cuaca hangat. Mereka nyaman dan mudah dipakai, dan sering kali menjadi pilihan untuk kegiatan sehari-hari di musim panas.",
            "  5. **Boots**: Boots adalah sepatu yang menutupi sebagian besar kaki dan pergelangan kaki. Ada berbagai jenis boots, termasuk sepatu bot, sepatu hiking, sepatu kowboy, sepatu kerja, dan sepatu musim dingin. Mereka sering kali dirancang untuk memberikan perlindungan tambahan terhadap cuaca eksternal atau lingkungan yang kasar.",
            "  6. **Heels dan Wedges**: Heels dan wedges adalah sepatu yang memiliki tumit atau platform di bagian bawahnya, memberikan peningkatan tinggi dan estetika. Mereka sering dipakai dalam situasi formal atau acara-acara khusus seperti pesta, pertemuan, atau acara formal lainnya.",
            "  7. **Flat Shoes**: Flat shoes adalah sepatu yang tidak memiliki tumit atau memiliki tumit yang sangat rendah."
            ]
        st.markdown("\n".join(footwear_info))
    elif category_type == "Outerwear":
        st.subheader("Kategori Outerwear")
        outerwear_info = [
            "- Kategori Outerwear (Pakaian Luar) dirancang untuk memberikan perlindungan dari elemen-elemen luar seperti cuaca dingin, angin, hujan, atau salju, sambil juga menambahkan dimensi gaya dan mode.",
            "- Berikut adalah beberapa contoh kategori outerwear yang umum digunakan :",
            "  1. **Coat**: Pakaian luar yang panjangnya mencapai pinggul atau di bawah pinggul, seringkali dengan kancing atau resleting di bagian depan. Ada berbagai jenis mantel, termasuk mantel panjang, mantel pendek, mantel wol, mantel parka, dan mantel hujan.",
            "  2. **Jacket**: Jacket adalah pakaian luar yang lebih pendek daripada coat dan umumnya memiliki gaya yang lebih casual. Ada banyak jenis jaket, seperti jaket denim, jaket kulit, jaket bomber, jaket parka, jaket puffer, dan jaket olahraga.",
            "  3. **Blazer**: Blazer adalah pakaian luar yang sering dipakai dalam situasi formal atau semi-formal, seperti pertemuan bisnis, acara sosial, atau kantor. Biasanya lebih ringan daripada coat atau jacket, blazer memiliki potongan yang lebih ramping dan lebih struktural.",
            "  4. **Vest**: Vest adalah pakaian luar yang tidak memiliki lengan dan dikenakan di atas pakaian lain, seringkali sebagai lapisan tambahan untuk memberikan kehangatan ekstra. Ada vest casual seperti vest rajut atau vest bulu dan vest formal seperti vest smoking.",
            "  5. **Parka**: Parka adalah jenis jaket atau mantel yang panjangnya mencapai bagian paha atau lebih panjang, seringkali dengan kapuchon dan bahan yang tahan air atau tahan angin. Parka sering dipakai untuk melindungi dari cuaca dingin, basah, atau berangin."
            ]
        st.markdown("\n".join(outerwear_info))

def histogram_plot(df):
    fig, axes = plt.subplots(1, 2, figsize=(20, 6))

    category_names = {
        "Accessories" : "Accessories",
        "Clothing" : "Clothing",
        "Footwear" : "Footwear",
        "Outerwear" : "Outerwear"
    }

    for category, ax in zip(df['Category'].unique(), axes):
        category_df = df[df['Category'] == category]
        ax.hist(category_df['Age'], bins=30, alpha=0.6, label=category_names[category])
        
        ax.set_xlabel('Age')
        ax.set_ylabel('Frequency')
        ax.set_title('Distribusi Usia berdasarkan Kategori')
        ax.grid(True)
        ax.legend()
    st.pyplot(fig)
    st.markdown("**1. Interpretasi**")
    st.markdown("""
        - Sumbu X menunjukkan usia pengguna, dengan rentang usia dari 18 hingga 70 tahun.
        - Sumbu Y menunjukkan jumlah pelanggan pada setiap usia
        - Bentuk histogram menunjukkan bahwa data usia pelanggan tidak terdistribusi secara normal""")
    
    st.markdown("**2. Insight**")
    st.markdown("""
        - Mayoritas pelanggan berusia antara 20 hingga 50 tahun
        - Distribusi usia pelanggan tidak merata, dengan konsentrasi pengguna yang lebih tinggi di kelompok usia 25-50 tahun""")
    
    st.markdown("**3. Actionable**")
    st.markdown("""
        - Targetkan produk kepada pelanggan yang berusia antara 25 hingga 50 tahun
        - Gunakan strategi marketing yang sesuai dengan kelompok usia 25-50 tahun""")
    
def age_histogram_plot(df):
    fig, ax = plt.subplots(figsize = (20, 5))

    sns.histplot(df['Age'], bins=30, kde=True, edgecolor='black', linewidth=1.2, alpha=0.6, ax=ax)

    plt.title('Distribusi Usia dengan Density Curve', fontsize=16)
    plt.xlabel('Age', fontsize=14)
    plt.ylabel('Density', fontsize=14)

    mean_age = df['Age'].mean()
    plt.axvline(x=mean_age, color='red', linestyle='--', label=f'Mean Age ({mean_age:.2f})')
    plt.legend()
    plt.show()
    st.pyplot(fig)
    st.markdown("**1. Interpretasi**")
    st.markdown("""
        - Sumbu X menunjukkan usia pengguna, dengan rentang usia dari 20 hingga 70 tahun.
        - Sumbu Y menunjukkan density, yang menunjukkan proporsi pengguna pada setiap usia""")
    
    st.markdown("**2. Insight**")
    st.markdown("""Mayoritas pelanggan berusia antara 30 hingga 50 tahun""")
    
    st.markdown("**3. Actionable**")
    st.markdown("""
        - Targetkan produk kepada pelanggan yang berusia antara 30 hingga 50 tahun
        - Gunakan strategi marketing yang sesuai dengan kelompok usia 30-50 tahun""")

def box_plot(df):
    fig, ax = plt.subplots(figsize = (20, 6))
    custom_palette = {"Male": "blue", "Female": "orange"}
    sns.boxplot(x='Gender', y='Purchase Amount (USD)', data=df, ax=ax, palette=custom_palette)
    plt.title('Jumlah Pembelian Berdasarkan Jenis Kelamin')
    plt.xlabel('Gender')
    plt.ylabel('Purchase Amount (USD)')
    plt.show()
    st.pyplot(fig)
    text = 'Terdapat batang vertikal untuk setiap kategori jenis kelamin. Tinggi setiap batang menunjukkan rata-rata jumlah pembelian untuk jenis kelamin tersebut. Dari diagram tersebut, tampak bahwa rata-rata jumlah pembelian untuk pria lebih tinggi daripada rata-rata jumlah pembelian untuk wanita.'
    st.markdown(text)

def scatter_plot(df):
    fig, ax= plt.subplots(figsize = (20, 6))
    plt.scatter(df['Age'], df['Review Rating'], alpha=0.5)
    plt.title('Age vs. Review Rating')
    plt.xlabel('Age')
    plt.ylabel('Review Rating')
    plt.show()
    st.pyplot(fig)
    st.markdown("**1. Interpretasi**")
    st.markdown("""
        - Sumbu X menunjukkan usia pengguna.
        - Sumbu Y menunjukkan review rating, dengan nilai 2.5 sebagai rating terendah dan 5 sebagai rating tertinggi.
        - Garis Regresi menunjukkan tren hubungan antara usia dan review rating""")
    
    st.markdown("**2. Insight**")
    st.markdown("""
        - Ada hubungan positif antara usia dan review rating.
        - Pelanggan yang lebih tua cenderung memberikan review rating yang lebih tinggi dibandingkan dengan pelanggan yang lebih muda""")
    
    st.markdown("**3. Actionable**")
    st.markdown("""
        - Targetkan produk kepada pelanggan yang lebih tua
        - Gunakan testimoni dari pengguna yang lebih tua di website atau marketing Perusahaan""")


def heatmap(df):
    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
    correlation_matrix = df[numerical_columns].corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='vlag', ax=ax)
    plt.title('Nilai Korelasi')
    plt.show()
    st.pyplot(fig)
    text = 'Tabel korelasi diatas menunjukkan bahwa terdapat hubungan yang signifikan antara beberapa variabel. Perusahaan dapat menggunakan informasi ini untuk membuat keputusan yang lebih baik tentang produk/layanan perusahaan, strategi marketing, dan program loyalitas pelanggan.'
    st.markdown(text)

def pie_chart_category(df):
    fig, ax = plt.subplots(figsize = (12,6))
    count = df.Category.value_counts()
    explode=(0,0,0,0.1)
    count.plot(kind='pie', explode=explode,colors = ['#fff98f', '#ff8fd6', '#8ffbff', '#8fffc1'], autopct='%.1f%%', ax=ax)
    plt.xlabel('Category',weight = 'bold', color = '#910018', fontsize = 14)
    plt.ylabel('Count',weight = 'bold', color = '#910018', fontsize = 14)
    plt.axis('equal')
    legend = plt.legend(labels=count.index, loc='best')
    legend.get_frame().set_facecolor('white')
    legend.get_frame().set_edgecolor('black')
    plt.show()
    st.pyplot(fig)
    st.markdown("**1. Interpretasi**")
    st.markdown("""
        - Kategori Clothing memiliki pangsa terbesar yaitu **45%**.
        - Kategori Accessories memiliki pangsa terbesar kedua, yaitu **31%**.
        - Kategori Footwear memiliki pangsa sebesar, yaitu **15%**.
        - Kategori Outerwear memiliki pangsa terkecil, yaitu **8%**""")
    
    st.markdown("**2. Insight**")
    st.markdown("""
        - Kategori Clothing dan Accessories merupakan kategori produk yang paling diminati.
        - Kategori Footwear memiliki pasar yang cukup signifikan, tetapi masih jauh dari Accessories dan Clothing.
        - Kategori Outerwear memiliki pangsa pasar yang kecil dan perlu meningkatkan strateginya untuk bersaing dengan kategori lain""")
    
    st.markdown("**3. Actionable**")
    st.markdown("""
        - **Accessories dan Clothing** : Mempertahankan pangsa pasar dan menjaga kualitas produk dan meningkatkan strategi marketing, serta menawarkan produk baru yang inovatif untuk memenuhi kebutuhan pelanggan yang terus berkembang
        - **Footwear** : Meningkatkan pangsa pasar dengan meningkatkan strategi marketing dan bersaing dengan Clothing dan Accessories, serta menawarkan produk yang lebih berfariatif dan menarik untuk menarik pelanggan baru.
        - **Outerwear** : Mengembangkan strategi baru untuk meningkatkan pangsa pasar, seperti menawarkan produk yang unik datau menargetkan market.""")

def stacked_bar_chart(df):
    fig, ax = plt.subplots(figsize = (20,6))
    pivot_table = df.pivot_table(index='Review Rating', columns='Category', aggfunc='size', fill_value=0)
    pivot_table.plot(kind='bar', stacked=True, colormap='crest', ax=ax)

    plt.ylabel('Review Rating')
    plt.title('Jumlah Orang dalam Penilaian Ulasan berdasarkan Kategori')
    plt.show()
    st.pyplot(fig)
    st.markdown("**1. Interpretasi**")
    st.markdown("""
       - Kategori Clothing memiliki jumlah ulasan terbanyak secara keseluruhan, lalu diikuti oleh Accessories, Footwear, dan Outerwear.
        - Untuk semua kategori, rating terendah (2.5) memiliki jumlah pengulas paling sedikit, sedangkan rating di kisaran 3.0 hingga 4.0 memiliki jumlah pengulas paling banyak.
        - Kategori Clothing memiliki distribusi ulasan yang paling beragam di antara semua kategori.
        - Kategori Footwear memiliki tren penurunan yang cukup tajam pada rating di bawah 4.0
        - Kategori Outerwear memiliki distribusi ulasan yang paling rendah di antara semua kategori.""")
    st.markdown("**2. Insight**")
    st.markdown("""
        - Kategori Clothing memiliki popularitas tinggi, ditunjukkan dengan jumlah ulasan terbanyak.
        - Kategori Clothing memiliki distribusi ulasan yang beragam, menunjukkan variasi preferensi pelanggan
        - Kategori Accessories memiliki popularitas yang cukup tinggi.
        - Kategori Accessories memiliki distribusi ulasan terkonsentrasi di rating 3.0 hinggi 4.0 yang menunjukkan mayoritas pelanggan puas
        - Kategori Footwear dan Outerwear memiliki popularitas yang lebih rendah dibandingkan dua kategori lainnya.""")
    
    st.markdown("**3. Actionable**")
    st.markdown("""
        - Pertahankan kualitas produk kategori accessories dan clothing.
        - Lakukan analisis mendalam untuk memahami penyebab tren penurunan rating.
        - Tawarkan promo atau diskon untuk menarik minta pelanggan.
        - Tanggapi ulasan negatif dengan solusi yang tepat.
        - Dorong pelanggan yang puas untuk memberikan ulasan positif.""")
    
def bar_chart_size(df):
    fig, ax = plt.subplots(figsize = (12,6))
    size = df['Size'].value_counts().sort_values(ascending= True)
    size.plot(kind='bar',color = sns.color_palette('inferno'), ax=ax)
    plt.xlabel('Size',weight = 'bold', color = '#910018', fontsize = 14)
    plt.ylabel('Count',weight = 'bold', color = '#910018', fontsize = 14)
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
    st.pyplot(fig)
    st.markdown("**1. Interpretasi**")
    st.markdown("""
        - Dari bar chart diatas menunjukkan distribusi data berdasarkan ukuran (size) yang dikategorikan menjadi 4 kategori : S, M, L, dan XL.
        - Tinggi bar menunjukkan jumlah data pada tiap kategori size.""")
    
    st.markdown("**2. Insight**")
    st.markdown("""
        - **Ukuran M** memiliki jumlah data pembelian paling banyak, hal ini menunjukkan bahwa size ini paling populer.
        - **Ukuran S dan L** memiliki jumlah data yang cukup signifikan, tetapi tidak sebanyak size M.
        - **Ukuran XL** memiliki jumlah data paling sedikit, menunjukkan size ini kurang populer""")
    
    st.markdown("**3. Actionable**")
    st.markdown("""
        - **Ukuran M** : Pastikan stok size M selalu tersedia untuk memenuhi permintaan, serta mempertimbangkan menawarkan variasi produk yang lebih banyak di size M.
        - **Ukuran S dan L** : Mempertahankan fokus pada size ini untuk memenuhi permintaan pelanggan, serta menawarkan variasi produk yang lebih banyak di size ini.
        - **Ukuran XL** : Melakukan riset untuk memahami mengapa size ini kurang populer, serta menawarkan promo atau diskon khusus untuk size ini untuk meningkatkan penjualan""")  

def bar_chart_subscription(df):
    fig, ax = plt.subplots(figsize = (20, 6))
    subscription_gender_counts = df.groupby(['Gender', 'Subscription Status']).size().unstack()
    subscription_gender_counts.plot(kind='bar', stacked=True, rot = 0, ax=ax)
    plt.title('Subscription Status by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.show()
    st.pyplot(fig)
    st.markdown("**1. Interpretasi**")
    st.markdown("""
        - Warna biru menunjukkan jumlah orang yang tidak berlangganan.
        - Warna oren menunjukkan jumlah orang yang berlangganan
        - Tinggi bar menunjukkan jumlah orang pada tiap kategoru Subscription Status""")
    
    st.markdown("**2. Insight**")
    st.markdown("""
        - Jumlah orang yang tidak berlangganan lebih banyak daripada jumlah orang yang berlangganan. Hal ini menunjukkan bahwa terdapat peluang untuk meningkatkan jumlah pelanggan yang berlangganan.
        - Persentase orang yang berlangganan cukup signifikan. Hal ini menunjukkan bahwa terdapat minat terhadap produk yang ditawarkan.""")
    st.markdown("**3. Actionable**")
    st.markdown("""
        - Permudah proses pendaftaran dan pembayaran untuk berlangganan.
        - Tingkatkan kualitas produk dan berikan nilai tambah bagi pelanggan.
        - Lakukan analisis data untuk memahami faktor yang mempengaruhi keputusan pelanggan untuk berlangganan.""")
    
def predict(df):
    # Dropdown untuk kolom "Age"
    age_option = st.selectbox('Input Age', [i for i in df['Age'].unique()])

    # Dropdown untuk kolom "Gender"
    gender_option = st.selectbox('Input Gender', [i for i in df['Gender'].unique()])

    # Dropdown untuk kolom "Item Purchased"
    item_option = st.selectbox('Input Item Purchased', [i for i in df['Item Purchased'].unique()])

    # Dropdown untuk kolom "Purchase Amount (USD)"
    purchase_amount_option = st.selectbox('Input Purchase Amount (USD)', [i for i in df['Purchase Amount (USD)'].unique()])

    # Dropdown untuk kolom "Location"
    location_option = st.selectbox('Input Location', [i for i in df['Location'].unique()])

    # Dropdown untuk kolom "Size"
    size_option = st.selectbox('Input Size', [i for i in df['Size'].unique()])

    # Dropdown untuk kolom "Color"
    color_option = st.selectbox('Input Color', [i for i in df['Color'].unique()])

    # Dropdown untuk kolom "Season"
    season_option = st.selectbox('Input Season', [i for i in df['Season'].unique()])

    # Dropdown untuk kolom "Review Rating"
    review_rating_option = st.selectbox('Input Review Rating', [i for i in df['Review Rating'].unique()])

    # Dropdown untuk kolom "Payment Method"
    payment_method_option = st.selectbox('Input Payment Method', [i for i in df['Payment Method'].unique()])

    # Dropdown untuk kolom "Shipping Type"
    shipping_type_option = st.selectbox('Input Shipping Type', [i for i in df['Shipping Type'].unique()])

    # Dropdown untuk kolom "Discount Applied"
    discount_applied_option = st.selectbox('Input Discount Applied', [i for i in df['Discount Applied'].unique()])

    # Dropdown untuk kolom "Promo Code Used"
    promo_code_option = st.selectbox('Input Promo Code Used', [i for i in df['Promo Code Used'].unique()])

    # Dropdown untuk kolom "Previous Purchases"
    previous_purchases_option = st.selectbox('Input Previous Purchases', [i for i in df['Previous Purchases'].unique()])

    # Dropdown untuk kolom "Frequency of Purchases"
    frequency_purchases_option = st.selectbox('Input Frequency of Purchases', [i for i in df['Frequency of Purchases'].unique()])

    # Dropdown untuk kolom "Age Category"
    age_category_option = st.selectbox('Input Age Category', [i for i in df['Age Category'].unique()])

    # Dropdown untuk kolom "Spending Category"
    spending_category_option = st.selectbox('Input Spending Category', [i for i in df['Spending Category'].unique()])

    data = pd.DataFrame({
        'Age': [df[df['Age'] == age_option].index[0]],
        'Gender': [df[df['Gender'] == gender_option].index[0]],
        'Item Purchased': [df[df['Item Purchased'] == item_option].index[0]],
        'Purchase Amount (USD)': [df[df['Purchase Amount (USD)'] == purchase_amount_option].index[0]],
        'Location': [df[df['Location'] == location_option].index[0]],
        'Size': [df[df['Size'] == size_option].index[0]],
        'Color': [df[df['Color'] == color_option].index[0]],
        'Season': [df[df['Season'] == season_option].index[0]],
        'Review Rating': [df[df['Review Rating'] == review_rating_option].index[0]],
        'Payment Method': [df[df['Payment Method'] == payment_method_option].index[0]],
        'Shipping Type': [df[df['Shipping Type'] == shipping_type_option].index[0]],
        'Discount Applied': [df[df['Discount Applied'] == discount_applied_option].index[0]],
        'Promo Code Used': [df[df['Promo Code Used'] == promo_code_option].index[0]],
        'Previous Purchases': [df[df['Previous Purchases'] == previous_purchases_option].index[0]],
        'Frequency of Purchases': [df[df['Frequency of Purchases'] == frequency_purchases_option].index[0]],
        'Age Category': [df[df['Age Category'] == age_category_option].index[0]],
        'Spending Category': [df[df['Spending Category'] == spending_category_option].index[0]]
    })  
    button = st.button('Predict')

    if button :
        with open ('knn.pkl','rb') as file:
            loaded_model = pickle.load(file)

        predicted = loaded_model.predict(data)

        if predicted[0] == 0:
            st.write('Accesories')
        elif predicted[0] == 1:
            st.write('Clothing')
        elif predicted[0] == 2:
            st.write('Footwear')
        elif predicted[0] == 3:
            st.write('Outerwear')
        else:
            st.write('Not Defined')
