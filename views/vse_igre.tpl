%rebase('osnova.tpl')

 <table class="highlight">
            <thead>
                <tr>
                    <th>Vse igre</th>
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