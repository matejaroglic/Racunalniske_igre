% rebase('osnova.tpl')

<html>
<head>
<style>
body   {
	background-image: url("https://duelyst.com/img/game-action-bg.jpg");
	}
</style>
</head>
</html>

	<div class="card-panel teal lighten-2">  
	  <div class="row">
		<div class="col s1">
			<html>
			<body>
			<img src="http://image.flaticon.com/teams/1-freepik.jpg" style="width:100px;height:100px;">
			</body>
			</html>
		</div>
	    <div class="col s9">
			<h3 class="center-align">Računalniške igre</h3>
		</div>
		<div class="col s2">
			% if up_id is not None:
			<p style="color:powderblue;">ime Uprorabnika</p>
			
			
			%end
		 </div>
		</div>
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
			<input value="" name="geslo" type="password" class="validate">
			  
			</p>
			</div>
			<div class="card-action">
            <button type = 'submit' name='gumb' value='vpis'>VPIS</button>
			<button type = 'submit' name='gumb' value='registracija'>REGISTRACIJA</button>
			  
		% else: 
			 
			<a href="/dodaj_igro">
			<img src="https://s27.postimg.org/ksmj4ypfn/dodaj_Igro.jpg" alt="dodajIgro" >
			</a> 
		% end
            </div>
          </div>
   	 </form>
        </div>
      </div>

			 <div class="row">
		<p style="color:powderblue;">Išči igro po imenu, letu, uporabniku, založniku, razvijalcu, zvrsti ali platformi:</p>
        <div class="input-field col s12">
		  <form action="/iskanje/">
			<input name="iskanje" type="text" style="color:white" "class="validate">
			<label for="iskanje">Vnesi:</label>
			<button class="waves-effect waves-light btn"><i class="material-icons right">search</i>Išči</button>
			<a href="/vse_igre" class="waves-effect waves-light btn"> <i class="material-icons right">view_list</i>VSE IGRE</a>
		  </form>
		  % if up_id is not None:
		  <a class="waves-effect waves-light btn"><i class="material-icons right">perm_identity</i>ODJAVA</a>
		  %end
        </div>
		
      </div>

			
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
