<template>
  <div>
    <footer class="text-center py-1 bg-info">
      <div class="tb-container">
        <ul class="d-flex justify-content-center tb-social-links">
          <li>
            <a rel="noopener" href="https://facebook.com/" class="text-light">
              <img src="@/assets/imgs/face.png" alt="face" width="30">
            </a>
          </li>
          <li>
            <a rel="noopener" href="https://twitter.com/" class="text-light">
             <img src="@/assets/imgs/twitter.png" alt="twi" width="30">
            </a>
          </li>
          <li>
            <a rel="noopener" href="https://instagram.com/" class="text-light">
            <img src="@/assets/imgs/instagram.png" alt="twi" width="30">
            </a>
          </li>
        </ul>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: "app",
  components: {}
};
</script>

<style>
ul.tb-social-links a {
  text-decoration: none;
}

/* article {
  margin-bottom: 200px;
} */

.tb-social-links {
  list-style: none;
  text-align: center;
  margin-bottom: 0px;
}
ul {
  display: block;
  list-style-type: disc;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  padding-inline-start: 40px;
}

.tb-social-links a {
  margin-right: 50px;
}

div {
  display: block;
}

.tb-container {
  display: center;
  max-width: 1px;
  margin-right: 50;
  margin-left: auto;
  padding: 0 40px;
}

footer {
  /* position:absolute;
  bottom:0;
  width:100%; */
  width: 100%;
  position: fixed;
  bottom: 0;
  left: 0;
}
</style>
