% rebase('osnova.tpl')


<html>
<head>
<style>
body   {
<<<<<<< HEAD
	background-image: url("https://duelyst.com/img/game-action-bg.jpg");
=======
	background-image: url("https://pixabay.com/get/ef3db60c2af61c22d2524518a3484491e374e7d104b0154991f5c17fafebb5/cat-687322_1280.jpg");
>>>>>>> 7d0c47359bd1996773e69c95fef7a6f63440c20a
	}
</style>
</head>
</html>

	   <div class="card-panel teal lighten-2">
			 <div class="right-align">
			<html>
			<body>
			<img src="http://image.flaticon.com/teams/1-freepik.jpg" style="width:100px;height:100px;">
			</body>
			</html>
			 </div>
	   <h4 class="center-align">Računalniške igre</h4>
	   </div>


<div class="row">
    <div class="col s6">
        <table class="highlight">
      <div class="row">
        <div class="col s12">
			% if up_id is None:
			<form action = '/' method = 'POST'>
          <div class="card">
            <div class="card-content text">
			<i class="material-icons right">perm_identity</i> <span class="card-title">Log in</span>
              <p><label class="active" for="up_ime">Uporabniško ime</label>
			  <input value="" name="up_ime" type="text" class="validate">
			  <label class="active" for="geslo">Geslo</label>
			  <input value="" name="geslo" type="text" class="validate">
			  
      </p>
            </div>
            <div class="card-action">
              <button type = 'submit' name='gumb' value='vpis'>VPIS</button>
			  <button type = 'submit' name='gumb' value='registracija'>REGISTRACIJA</button>
			 % end
            </div>
          </div>
   	 </form>
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
	
    <div class="col s5">
        <table class="striped">
            <thead>
                <tr>
				     <th>
						<h4 class="center-align">Top 10</h4>
					</th>
				</tr>
            </thead>
			<tbody>
			

		%for igra in igre:
                <tr>
                    <td>
			 <a href="/igra/{{igra['id']}}/">
                        <span class="purple-text text-purple-2">
							<h6 class="center-align">{{igra['ime']}} </h6>
						</span>
					</a>
                    </td>
                </tr>
                %end	
               
            </tbody>
        </table>
    </div>
</div>