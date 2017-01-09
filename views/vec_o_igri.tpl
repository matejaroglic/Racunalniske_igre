%rebase('osnova.tpl')

      <div class="row">
        <div class="col s12">
          <div class="card blue-grey darken-2">
            <div class="card-content white-text">
              <span class="card-title">{{podatki['ime']}}</span>
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
    <div class="col s12"><p>Komentarji</p></div> <div class="right-align"><a class="waves-effect waves-light btn">Dodaj komentar</a></div>
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