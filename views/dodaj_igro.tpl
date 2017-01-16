%rebase('osnova.tpl')

      <div class="row">
        <div class="col s12 m6">
          <div class="card blue-grey darken-1">
            <div class="card-content white-text">
              <span class="card-title">Dodajanje igre</span>
			  <form action = '/igre/dodaj_igro/' method = 'POST'>
			  <label class="active" for="ime_igre">Ime igre:</label>
			<input value="" id="ime_igre" type="text" class="validate">
			<label class="active" for="leto">Leto:</label>
			<input value="" id="leto" type="text" class="validate">
			<label class="active" for="razvijalec">Razvijalec:</label>
			<input value="" id="razvijalec" type="text" class="validate">
			<label class="active" for="zaloznik">Založnik:</label>
			<input value="" id="zaloznik" type="text" class="validate">
			<label class="active" for="platforme">Platforme:</label>
			%for plat in platforme:
			<input type="checkbox" name="platforme" value="{{plat}}" checked>{{plat}}<br>
			%end
			<br>
			<label class="active" for="zalozniki">Zalozniki:</label>
			%for zaloznik in zalozniki:
			<input type="checkbox" name="zalozniki" value="{{zaloznik}}" checked>{{zaloznik}}<br>
			%end
			
			

            </div>
            <div class="card-action">
              </a><button type = 'submit'>Dodaj!</button>
			  </form>
            </div>
          </div>
        </div>
      </div>