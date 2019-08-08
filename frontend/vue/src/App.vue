<template>
  <div class="container">
    <header class="title">
    <h2>Data viewer</h2>
    </header>
    <div class="content-one">
      <h3>Filter</h3>
      <label class="date-from" for="datefrom">From</label>
      <input type="date" id="datefrom" v-model="dateFrom">
      
      <label class="date-to" for="dateto">To</label>
      <input type="date" id="dateto" :min="dateFrom" v-model="dateTo">
    </div>    
    <div class="content-two">
      <label for="status" class="status">Status</label>
      <select id="status" v-model="status">
        <option selected value="">-- All --</option>
        <option value="2">Open</option>
        <option value="3">Pending</option>
        <option value="4">Resolved</option>
        <option value="5">Closed</option>
      </select>
      
      <label for="priority" class="priority">Priority</label>
      <select id="priority" v-model="priority">
        <option selected value="">-- All --</option>
        <option value="1">Low</option>
        <option value="2">Medium</option>
        <option value="3">High</option>
        <option value="4">Urgent</option>
      </select>
      
      <label for="type" class="type">Type</label>
      <select id="type" v-model="type">
        <option selected value="">-- All --</option>
        <option value="Question">Question</option>
        <option value="Incident">Incident</option>
        <option value="Problem">Problem</option>
        <option value="Feature Request">Feature Request</option>
        <option value="Refund">Refund</option>
      </select>

      <input type="number" placeholder="Ticket ID" v-model="id">
      <input type="number" placeholder="Agent ID" v-model="agent">
    </div>
    <div class="content-three">
      <div>
        <table class="table">
            <tr>
              <th style="width:16%">Date to Solve</th>
              <th style="width:8%">Ticket ID</th>
              <th style="width:8%">Status</th>
              <th style="width:8%">Priority</th>
              <th style="width:12%">Type</th>
              <th style="width:15%">Agent Name</th>
              <th style="width:12%">Agent ID</th>
            </tr>
            <tr class="table-item" v-for="item in filteredItems" :key="item.id">
              <td>{{ item.due_by }}</td>
              <td>{{ item.id }}</td>
              <td>{{ item.status }}</td>
              <td>{{ item.priority }}</td>
              <td>{{ item.type }}</td>
              <td>{{ item.name }}</td>
              <td>{{ item.responder_id }}</td>
            </tr>
            <tbody v-if="filteredItems.length < 9">
              <tr v-for="i in (9 - filteredItems.length)" :key="i.id">
                <td>&nbsp;</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            </tbody>
        </table>
      </div>
    </div>
  </div>  
</template>
<script>
export default {
  data() {
    return {
      id: '',
      agent: '',
      dateFrom: '',
      dateTo: '',
      items: [],
      status: '',
      priority: '',
      type: ''
    }
  },
  created() {
    this.$http.get('http://localhost:8000/users', { params: {order_type: 'desc'}})
        .then(response => {
          this.items = response.body;
        }, error => {
          this.error = error.body;          
        });
  },
  methods: {
  },
  computed: {
    filteredItems() {
      var result = this.items.filter((item) => item.due_by >= this.dateFrom);
      if (this.id) {
        result = this.items.filter((item) => item.id == this.id);
        console.log('one');
      }
      if (this.agent) {
        result = result.filter((item) => item.responder_id == this.agent);
        console.log('two');
      }
      if (this.dateTo) {
        result = result.filter((item) => item.due_by <= this.dateTo);
        console.log('three');
      }
      if (this.status) {
        result = result.filter((item) => item.status == this.status);
        console.log('four');        
        }
      if (this.priority) {
        result = result.filter((item) => item.priority == this.priority);
        console.log('five');        
        }
      if (this.type) {
        result = result.filter((item) => item.type == this.type);
        console.log('six');        
        }
      return result;
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

/* ========> Application desing with CSS Grid <========*/

.container{
	width: 100%;
  height: 100%;
  display: grid;
  padding: 0px 40px;
  /* 1 columna */
  grid-template-columns: 100%;
  /* 4 filas */
  grid-template-rows: auto auto auto 1fr;
}

.title {
  grid-column: 1 / 2;
  grid-row: 1 / 2;
}

.content-one {
  margin-top: 1%;
  grid-column: 1 / 2;
  grid-row: 2 / 3;
}

.content-two {
  margin-top: 1%;
  grid-column: 1 / 2;
  grid-row: 3 / 4;
}

.content-three {
  height: 100%;
  margin-top: 1%;
  grid-column: 1 / 2;
  grid-row: 4 / 5;
}

/* ========> Styles for the content 1 - 3 <========*/

.title {
  padding: 10px 0px;
}

.container input, .container select {
  display: inline;
  width: 130px;
  height: 30px;
  padding-left: 6px;
  margin: 10px 0px;
  color: #555;
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 4px;
  outline: none;
}

.content-two .priority, .content-two .type, .content-two input, .content-one .date-to {
  margin-left: 3%;
}

.content-three div {
  overflow-y: scroll;
  height: 350px;
}

.content-three .table {
  width: 100%;
  text-align: left;
  border-collapse: collapse;
}

.table td, .table th {
  border-bottom: 1px solid #dddddd;
  padding: 8px;
}

.table tr:nth-child(even) {
  background-color: #f2f2f2;
}

.table tr:hover {
  background-color: #f9f9f9;
}

/* ========> Styles for the scrollbar <========*/

::-webkit-scrollbar {
      width: 10px;
}

::-webkit-scrollbar-track {
      background-color: #f8f8f8;
} 

::-webkit-scrollbar-thumb {
      background-color: #ddd;
} 

/* ::-webkit-scrollbar-button {
      background-color: navy;
}
*/

/* ========> Remove the arrows from the date fields  <========*/

input[type=date]::-webkit-inner-spin-button, 
input[type=date]::-webkit-outer-spin-button { 
  -webkit-appearance: none; 
  margin: 0;
}
input[type=input] { -moz-appearance:textfield; }
</style>
