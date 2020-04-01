git <template>
  <Principal>
    <div>
      <div
        class="Wrapper_wrapper__28JZg BlockContentHtml_wrapper__3bo2x Wrapper_wrapper-default-width__2PRux"
        style="background-image: url(&quot;undefined&quot;);"
      >
        <div class="Wrapper_container__3c3aY Wrapper_container-default-width__2lKTA">
          <div class="HtmlMarkup_html__3sUPP">
            <!-- <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">-->
            
            <div id="page-custom">
              <div class="container max-center">
                <div class="row">
                  <div class="col-md-12">
                    <h1 class="title-line-center">Faça sua Doação</h1>
                  </div>
                </div>

                <div class="row">
                  <div class="col-md-12">
                    <p
                      class="text-center"
                    >Clique para fazer uma doação</p>
                  </div>
                </div>
              </div>

              <div class="container">
                <div class="row">
                  <div class="col-md-3 col-sm-6 text-center container-lines">
                    <div class="container-lines">
                      
                      
                      <div
                        class="img-line"
                      >&nbsp;</div>
        
                      <h2>

                        <a class="title-lines" v-bind:style="{ 'background-image': 'url(' + doa1 + ')' }">
                          <span class="lines">Doar 5 R$</span>
                        </a>
                      </h2>
                    </div>
                  </div>
                  
                  <div class="col-md-3 col-sm-6 text-center">
                    <div class="container-lines">
                      <div
                        class="img-line"
                        style="background-image: url('@/assets/imgs/michelle.jpg')"
                      >&nbsp;</div>

                      <h2>
                        <a class="title-lines" v-bind:style="{ 'background-image': 'url(' + doa2 + ')' }">
                          <span class="lines">Doar 10 R$</span>
                        </a>
                      </h2>
                    </div>
                  </div>

                  <div class="col-md-3 col-sm-6 text-center container-lines">
                    <div class="container-lines">
                      <div
                        class="img-line"
                        style="background-image: url('@/assets/imgs/michelle.jpg')"
                      >&nbsp;</div>

                      <h2>
                        <a class="title-lines" v-bind:style="{ 'background-image': 'url(' + doa3 + ')' }">
                          <span class="lines">Doar 20R$</span>
                        </a>
                      </h2>
                    </div>
                  </div>

                  <div class="col-md-3 col-sm-6 text-center container-lines">
                    <div class="container-lines">
                      <div
                        class="img-line"
                        style="background-image: url('')"
                      >&nbsp;</div>

                      <h2>
                        <a class="title-lines" v-bind:style="{ 'background-image': 'url(' + doa4 + ')' }">
                          <span class="lines">Doar 50R$</span>
                        </a>
                      </h2>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </Principal>
</template>

<script>
/* eslint-disable */ 
import Principal from "../layouts/principal";

export default {
  name: "app",
  components: { Principal },
data() {
  return {
  doa1:require('../imgs/doar/doar20.svg'),
  doa2:require('../imgs/doar/doar50.svg'),
  doa3:require('../imgs/doar/doar100.svg'),
  doa4:require('../imgs/doar/doar200.svg')
  }
}}
</script>

<style scoped>
#page-custom h2 {
  font-weight: 300;
}
#page-custom .container-lines,
#page-custom .img-line {
  position: relative;
  height: 27.5rem;
  margin-bottom: 30px;
}
#page-custom .container-lines:hover {
  top: -1px;
  transition: all 3s ease;
}

#page-custom .img-line {
  background-position-x: center;
  background-repeat: no-repeat;
}
#page-custom .title-lines {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  margin: 0;
  background-color: rgba(0, 0, 0, 0.4);
  color: #fff;
  font-size: 1.375rem;
  text-transform: uppercase;
  font-weight: 600;
}
#page-custom .title-lines:hover {
  color: #fff;
}
#page-custom .lines {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
