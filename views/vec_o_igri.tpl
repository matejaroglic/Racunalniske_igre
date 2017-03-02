%rebase('osnova.tpl')

	<html>
	<body>
          <div class="card blue-grey darken-2">
            <div class="card-content white-text">
              <span class="card-title">{{podatki['ime']}}</span>
			  
			<div class="row">
			<div class="col s5">
				<p>
				Leto izdaje : {{podatki['leto']}} <br>
				Razvijalec: {{razvijalec['razvijalec']}} <br>
				Založnik: {{podatki['zaloznik']}}<br>
				</p>
			</div>
			
			<div class="col s5">
				<div class="chip">Povprečna ocena: {{povpOcena}}</div>
				
				% if ocenil == 0 and up is not None:
				<form action = '/igra/{{id_igre}}/' method = 'POST'>
				<ul id="dropdown2" class="dropdown-content">
				<li style="text-align:center;"><button value = 1 name = 'izbira' type='submit' style="border:none;background-color: Transparent;padding-top:15px;" >1</button></li>
				<li style="text-align:center;"><button value = 2 name = 'izbira' type='submit' style="border:none;background-color: Transparent;padding-top:15px;" >2</button></li>
				<li style="text-align:center;"><button value = 3 name = 'izbira' type='submit' style="border:none;background-color: Transparent;padding-top:15px;" >3</button></li>
				<li style="text-align:center;"><button value = 4 name = 'izbira' type='submit' style="border:none;background-color: Transparent;padding-top:15px;" >4</button></li>
				<li style="text-align:center;"><button value = 5 name = 'izbira' type='submit' style="border:none;background-color: Transparent;padding-top:15px;" >5</button></li>
				</ul>
				<a class="btn dropdown-button" href="#!" data-activates="dropdown2">OCENI IGRO<i class="mdi-navigation-arrow-drop-down right"></i></a>
				</form>
				%end
			</div>  
				
			  
			<div class="col s2">
			<img src="https://cdn2.iconfinder.com/data/icons/pack1-baco-flurry-icons-style/512/Game_Center.png" style="width:100px;height:100px;">
			 </div>
			  

			  
			  <p>
			  Zvrst: <br>
			  %for el in zvrsti:
			<div class="chip">
				{{el['zvrst']}}
			</div>
			 %end 
			 <br>
			  Platforma: <br>
			 %for ele in platforme:
			<div class="chip">
				{{ele['platforma']}}
			</div>
			 %end 
			  </p>
			<div class="right-align">Dodal: {{podatki['uporabnik']}}</div>
            </div>
          </div>
        </div>
 



	%if up is not None:
       <div class="row">
        <div class="col s12 m6">
		<form action = '/igra/{{id_igre}}/' method = 'POST'>
          <div class="card blue-grey darken-1">
            <div class="card-content white-text">
              <span class="card-title">Komentiranje</span>
              <p><label class="active" for="komentar">Napisi komentar</label></p>
			  <input value="" name="komentar" type="text" class="validate">
            </div>
            <div class="card-action">
              <input type="submit" value="Dodaj komentar">
            </div>
          </div>
		  </form>
        </div>
      </div>
	 %end


  <div class="row">
    <div class="col s12"><p>Komentarji</p></div> 
  </div>
	
	%for komentar in komentarji:
 <div class="row">
		<div class="col s12 m4 l2"><p>{{komentar['dodal']}}</p></div>
		<div class="col s12 m4 l8"><p>{{komentar['komentar']}}</p></div>
		<div class="col s12 m4 l2"><p>{{komentar['datum']}}</p></div>
 </div>
	%end
 
<ul class="collection"></ul>
<a href="/">Začetna stran</a>
<br>
<br>
<br>
</body>
</html>