%rebase('osnova.tpl')

 <table class="highlight">
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