% rebase('osnova.tpl')



<div class="row">
    <div class="col s6">
        <table class="highlight">
            <thead>
                <tr>
                    <th>
					<a href="/login" class="waves-effect waves-light btn"> <i class="material-icons right">perm_identity</i>LOGIN </a>
					</th>
                </tr>
            </thead>
			 <div class="row">
        <div class="input-field col s4">
          <input  id="first_name" type="text" class="validate">
          <label for="first_name">Vnesi:</label>
        </div>
        <div class="input-field col s2">
<a href="/login" class="waves-effect waves-light btn"> <i class="material-icons right">search</i>Išči </a>
        </div>
      </div>
            <tbody>
                
            </tbody>
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