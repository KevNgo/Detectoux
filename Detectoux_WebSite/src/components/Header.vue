<template>
  <header>
    <div class="logo">
      <img alt="Vue logo" src="../assets/logo_detectoux.png" />
    </div>
  </header>
</template>

<script>
export default {
  name: "logo",
  components: {},
};
</script>

<style scoped>
header {
  background-color: #516079;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.logo {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 5px;
}

img {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100px;
  height: 100px;
}
</style>