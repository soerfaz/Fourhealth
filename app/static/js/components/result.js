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
            <h3 class="mb-5 text-center">Depending on what symptoms you entered, you obtained:</h3>
            <div class="row gx-4 gx-lg-5 align-items-center">
              <h4 class="fw-bolder">${_name}</h4>
              <p class="lead">${description}</p>
            </div>
            <h5 class="fw-bolder mb-3">Precaution</h5>
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