%rebase('osnova.tpl')

      <div class="row">
        <div class="col s12">
          <div class="card blue-grey darken-2">
            <div class="card-content white-text">
              <span class="card-title">{{podatki['ime']}}</span>
			  
<<<<<<< HEAD
			<div class="right-align">
			<html>
			<body>
			<img src="https://cdn2.iconfinder.com/data/icons/pack1-baco-flurry-icons-style/512/Game_Center.png" style="width:100px;height:100px;">
			</body>
			</html>
			 </div>
=======
			 <div class="right-align">
			<html>
			<body>
			<img src="https://cdn.pixabay.com/photo/2016/03/03/22/56/birds-1235201_640.jpg" style="width:100px;height:100px;">
			</body>
			</html>
			 </div>

>>>>>>> 7d0c47359bd1996773e69c95fef7a6f63440c20a
			  
              <p>
			  Leto izdaje : {{podatki['leto']}} <br>
			  Razvijalec: {{razvijalec['razvijalec']}} <br>
			  Založnik: {{podatki['zaloznik']}}<br>
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
      </div>


  
       <div class="row">
        <div class="col s12 m6">
          <div class="card blue-grey darken-1">
            <div class="card-content white-text">
              <span class="card-title">Komentiranje</span>
              <p><label class="active" for="komentar">Napisi komentar</label>
			  <input value="" id="komentar" type="text" class="validate">
      </p>
            </div>
            <div class="card-action">
              <a href="/dodajKomentar">Dodaj komentar</a>
            </div>
          </div>
        </div>
      </div>

  <div class="row">
    <div class="col s12"><p>Komentarji</p></div> 
  </div>
	
	%for komentar in komentarji:
 <div class="row">
		<div class="col s12 m4 l2"><p>{{komentar['dodal']}}</p></div>
		<div class="col s12 m4 l8"><p>{{komentar['komentar']}}</p></div>
		<div class="col s12 m4 l2"><p>{{komentar['datum']}}</p></div>
	%end
 </div>
 
<ul class="collection">

</ul>