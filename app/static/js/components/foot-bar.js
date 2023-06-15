class FootBar extends HTMLElement {
    connectedCallback() {
      this.render();
    }
    render() {
      this.innerHTML = `
      <footer id="footer" class="footer">
      <div class="container">
        <div class="row gy-3">
          <div class="col-lg-6 col-md-6 d-flex">
            <i class="bi bi-geo-alt icon"></i>
            <div>
              <h4>Address</h4>
              <p>
                No. 10 Ruko IKN <br />
                Nusantara - Indonesia<br />
              </p>
            </div>
          </div>

          <div class="col-lg-6 col-md-6 footer-links d-flex">
            <div>
              <h4>Hubungi Kami</h4>
              <div class="d-flex flex-column lh-lg">
                <a class="text-decoration-none text-white-50" href="mailto:bayyupwirawan@gmail.com"
                  >Bayyu Putra Wirawan</a
                >
                <a
                  class="text-decoration-none text-white-50"
                  href="mailto:jostampan123@gmail.com"
                  >George Isaiah Abiyoso</a
                >
                <a
                  class="text-decoration-none text-white-50"
                  href="mailto:soerfaz@gmail.com"
                  >Gesen Abiyoga Soerfaz</a
                >
                <a
                  class="text-decoration-none text-white-50"
                  href="mailto:farizi1906@gmail.com"
                  >Salman Al Farizi</a
                >
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="container">
        <div class="copyright">
          &copy; Copyright <strong><span>Fourhealth</span></strong
          >. All Rights Reserved
        </div>
      </div>
    </footer>`;
    }
}
customElements.define('foot-bar', FootBar);