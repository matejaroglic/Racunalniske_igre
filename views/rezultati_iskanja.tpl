%rebase('osnova.tpl')


<div class="row">
 <div class="col s5">
  <table class="striped">
            <thead>
                <tr>
                    <th>Rezultati iskanja:</th>
				</tr>
            </thead>
			<tbody>
			
		%for el in rezultati:
                <tr>
                    <td>
			 <a href="/igra/{{el['id']}}/">
                       
                        {{el['ime']}} 
                        </a>
                    </td>
                </tr>
                %end		
			      
               
            </tbody>
        </table>
	</div>  
</div> 