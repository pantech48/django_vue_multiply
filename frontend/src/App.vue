<template>
  <div id="app">
    <h1>Multiply Two Numbers</h1>
    <form @submit.prevent="multiply">
      <input v-model.number="first" placeholder="Enter first number" required />
      <input v-model.number="second" placeholder="Enter second number" required />
      <button type="submit">Multiply</button>
    </form>
    <div v-if="result !== null">
      <h2>Result: {{ result }}</h2>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      first: null,   // Renamed from a to first
      second: null,  // Renamed from b to second
      result: null,
    };
  },
  methods: {
    async multiply() {
      try {
        const response = await fetch(
          `http://localhost:8000/multiply/?first=${this.first}&second=${this.second}`
        );
        const data = await response.json();
        if (data.result !== undefined) {
          this.result = data.result;
        } else {
          alert(data.error);
        }
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
