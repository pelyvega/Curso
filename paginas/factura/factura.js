const form = document.getElementById("product-form");
const tbody = document.getElementById("invoice-body");
const totalDisplay = document.getElementById("total");

let products = JSON.parse(localStorage.getItem("products")) || [];

function saveToStorage() {
  localStorage.setItem("products", JSON.stringify(products));
}

function renderProducts() {
  tbody.innerHTML = "";
  let total = 0;

  products.forEach((product, index) => {
    const subtotal = product.price * product.quantity;
    total += subtotal;

    const row = document.createElement("tr");

    row.innerHTML = `
      <td contenteditable="true" oninput="updateProduct(${index}, 'name', this.textContent)">${product.name}</td>
      <td contenteditable="true" oninput="updateProduct(${index}, 'price', this.textContent)">${product.price}</td>
      <td contenteditable="true" oninput="updateProduct(${index}, 'quantity', this.textContent)">${product.quantity}</td>
      <td>$${subtotal.toFixed(2)}</td>
      <td class="actions">
        <button class="delete" onclick="deleteProduct(${index})">Eliminar</button>
      </td>
    `;

    tbody.appendChild(row);
  });

  totalDisplay.textContent = total.toFixed(2);
}

form.addEventListener("submit", function (e) {
  e.preventDefault();
  const name = document.getElementById("product-name").value.trim();
  const price = parseFloat(document.getElementById("product-price").value);
  const quantity = parseInt(document.getElementById("product-quantity").value);

  if (!name || isNaN(price) || isNaN(quantity)) return;

  products.push({ name, price, quantity });
  saveToStorage();
  renderProducts();
  form.reset();
});

function deleteProduct(index) {
  products.splice(index, 1);
  saveToStorage();
  renderProducts();
}

function updateProduct(index, field, value) {
  if (field === 'price' || field === 'quantity') {
    value = parseFloat(value);
    if (isNaN(value)) return;
  }
  products[index][field] = field === 'name' ? value : +value;
  saveToStorage();
  renderProducts();
}

renderProducts();
