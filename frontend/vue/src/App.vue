<template>
  <div class="contenedor">
    <header class="title">
    <h1>Using Freshdesk Developer</h1>
    </header>
    <div class="content-one">
      <label>id ticket</label>
      <input type="number" autofocus v-model="id">
      <button @click="getItem">Select One</button>
      <button @click="getItems">Select All</button>
      <div v-if="items.length > 0">
        <h4>Items</h4>
        <ul class="list">
          <li class="list-item" v-for="item in items" :key="item.id" @click="id = item.id">
            Subject: {{ item.subject }} - id: {{ item.id }} - Priority: {{ item.priority }}
          </li>
        </ul>
    </div>
    </div>
    <div class="content-two" v-if="item">
      <h4>Item</h4>
      <p>{{ item.subject }}</p>
      <p>{{ item.description }}</p>
    </div>
    <div class="content-two error" v-else>
      <p>{{ error.error }}</p>
    </div>
  </div>  
</template>
<script>
export default {
  data() {
    return {
      id: '',
      item: null,
      items: [],
      error: ''
    }
  },
  methods: {
    getItem() {
      this.item = '';
      this.$http.get('http://localhost:8000/user', { params: {id: this.id} })
        .then(response => {
          this.item = response.body;
        }, error => {
          this.error = error.body;
        });
    },
    getItems() {
      this.$http.get('http://localhost:8000/users')
        .then(response => {
          this.items = response.body;
        }, error => {
          this.error = error.body;          
        });
    }
  }
}
</script>
<style scoped>

/* =========> General Styles <========= */

body{
	background-color: #fff;
}

*{
  margin: 0;
	padding: 0;
	box-sizing: border-box;
}

/* ========> layout of the application with CSS Grid <========*/

.contenedor{
	width: 100%;
  height: auto;
  display: grid;
  /* 2 columna */
  grid-template-columns: 50% 50%;
  /* 2 filas */
  grid-template-rows: 70px 1fr;
}

.title {
  text-align: center;
  padding: 5px;
  margin: 10px;
  grid-column: 1 / 3;
  grid-row: 1 /2;
}

.content-one {
  grid-column: 1 / 2;
  grid-row: 2 / 3; 
  padding-left: 20px;
  padding-top: 20px;
}

.content-two {
  grid-column: 2 / 3;
  grid-row: 2 / 3;
  padding-left: 20px;
  padding-top: 20px;
}


/* ========> Styles for the content 1 <========*/

.content-one label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.content-one input {
  display: block;
  width: 60%;
  height: 30px;
  padding: 6px;
  margin-bottom: 20px;
  color: #555;
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 4px;
  outline: none;
}

.content-one button {
  display: block;
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
  border-radius: 4px;
  margin-bottom: 15px;
  padding: 6px;
  cursor: pointer;
  border: 1px solid transparent;
}
.content-one button:hover {
  background-color: #0663b4;
}

.list {
  margin-top: 10px;
}

.list-item {
  list-style-type: none;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  padding: 8px 10px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
  width: 75%;
  cursor: pointer;
}


/* ========> Styles for the content 2 <========*/

.content-two h4 {
  margin-bottom: 5px;
}

.content-two p {
  margin-bottom: 7px;
}

.error {
  color: red;
}


/* ========> Remove the arrows from the numeric fields  <========*/

input[type=number]::-webkit-inner-spin-button, 
input[type=number]::-webkit-outer-spin-button { 
  -webkit-appearance: none; 
  margin: 0;
}
input[type=number] { -moz-appearance:textfield; }
</style>
