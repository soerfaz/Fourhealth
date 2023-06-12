class AppBar extends HTMLElement {
    connectedCallback() {
      this.render();
    }
    render() {
      this.innerHTML = `
      <nav class="navbar navbar-expand-lg navbar-dark py-3"  style="background-color: #146C94;">
        <div class="container">
            <a class="navbar-brand" href="#">
                <img src="./static/img/faviconfourhealth.png" alt="" width="30" class="d-inline-block align-text-top me-2">
                Fourhealth
              </a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
              <li class="nav-item mx-3">
                <a class="nav-link" aria-current="page" href="/">Beranda</a>
              </li>
              <li class="nav-item mx-3">
                <a class="nav-link active" href="/cek_penyakit">Cek Penyakit</a>
              </li>
              <li class="nav-item mx-3">
                <a class="nav-link" href="/about">About-Us</a>
              </li>
            </ul>
           
          </div>
        </div>
      </nav>`;
    }
  }
  customElements.define("app-bar", AppBar);