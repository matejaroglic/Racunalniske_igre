% rebase('osnova.tpl')



<div class="row">
    <div class="col s6">
        <table class="highlight">
      <div class="row">
        <div class="col s12">
          <div class="card">
            <div class="card-content text">
			<i class="material-icons right">perm_identity</i> <span class="card-title">Log in</span>
              <p><label class="active" for="up_ime">Uporabniško ime</label>
			  <input value="" id="up_ime" type="text" class="validate">
			  <label class="active" for="geslo">Geslo</label>
			  <input value="" id="geslo" type="text" class="validate">
			  
      </p>
            </div>
            <div class="card-action">
              <a href="#">VPIS</a>
			  <a href="#">REGISTRACIJA</a>
            </div>
          </div>
        </div>
      </div>

			 <div class="row">
		Išči igro po imenu, letu, uporabniku, založniku, razvijalcu, zvrsti ali platformi:
        <div class="input-field col s6">
		  <form action="/iskanje/">
			<input name="iskanje" type="text" class="validate">
			<label for="iskanje">Vnesi:</label>
			<button class="waves-effect waves-light btn"><i class="material-icons right">search</i>Išči</button>
		  </form>
        </div>
		
      </div>
	  <br>
	  <br>
      <thead>
                <tr>
                    <th>
					<a href="/vse_igre" class="waves-effect waves-light btn"> <i class="material-icons right">view_list</i>VSE IGRE</a>
					</th>
                </tr>
      </thead>  
	  
        </table>
    </div>
	
    <div class="col s6">
        <table class="highlight">
            <thead>
                <tr>
                    <th>Top 10</th>
				</tr>
            </thead>
			<tbody>
			
		%for igra in igre:
                <tr>
                    <td>
			 <a href="/igra/{{igra['id']}}/">
                       
                        {{igra['ime']}} 
                        </a>
                    </td>
                </tr>
                %end		
			      
               
            </tbody>
        </table>
    </div>
</div>