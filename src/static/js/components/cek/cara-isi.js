class CaraIsi extends HTMLElement {
    connectedCallback() {
      this.render();
    }
    render() {
      this.innerHTML = `
      <article id="cara-isi" class="card">
        <h3 class="text-center">Cara Pengisian Gejala</h3>
        <ul class="list-group">
          <li class="list-group-item">1. Buka halaman input gejala penyakit.</li>
          <li class="list-group-item">2. Pada form, Anda akan melihat input box dengan label "Masukkan Gejala".</li>
          <li class="list-group-item">3. Klik pada input box untuk membuka pilihan gejala penyakit.</li>
          <li class="list-group-item">4. Anda dapat memilih satu atau lebih gejala penyakit dengan cara:
            <ul>
              <li>Klik pada gejala yang ingin Anda pilih.</li>
              <li>Jika ingin memilih lebih dari satu gejala, lakukan hal yang sama seperti cara pertama otomatis akan
                menambahkan gejala.</li>
              <li>Gejala yang sudah dipilih akan ditampilkan pada input box.</li>
            </ul>
          </li>
          <li class="list-group-item">5. Jika ingin mengubah atau menghapus pilihan gejala, Anda dapat membuka input box
            lagi dan mengklik atau mengklik ulang gejala yang ingin diubah atau dihapus.</li>
          <li class="list-group-item">6. Setelah selesai mengisi form atau halaman lainnya, klik tombol "Cek" atau
            untuk mengirimkan data yang Anda isi.</li>
        </ul>
        <h6 class="text-justify mt-2 text-danger">*Pastikan untuk mengikuti petunjuk dan instruksi yang diberikan pada
          halaman input gejala penyakit yang sebenarnya.</h4>
      </article>`;
    }
}
customElements.define('cara-isi', CaraIsi)