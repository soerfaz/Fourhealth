class Article extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    const _name = this.hasAttribute("_name") ? this.getAttribute("_name") : "";
    const description = this.hasAttribute("description") ? this.getAttribute("description") : "";
    const precaution = this.hasAttribute("precaution") ? this.getAttribute("precaution") : "";

    console.log(_name)
    console.log(description)
    console.log(precaution)

   
    this.innerHTML = `
    <section class="card shadow result">
          <div class="card-body">
            <h1 class="mb-4">According by what you input, you got : </h1>
            <div class="row gx-4 gx-lg-5 align-items-center">
              <h1 class="display-5 fw-bolder">${_name}</h1>
              <p class="lead">${description}</p>
            </div>
            <h2 class="fw-bolder mb-4">Precaution</h2>
            <ul>
              ${precaution.split(",").map(function(precaution,index){
                return `
                  <li>
                    <p> ${precaution.charAt(0).toUpperCase() + precaution.slice(1)} </p>
                  </li>
                `
              }).join("")}
            </ul>
          </div>
    </section>


    `;
  }
}

customElements.define("article-card", Article);