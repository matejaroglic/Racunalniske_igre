% rebase('osnova.tpl')
<div class="row">
    <div class="col s6">
        <table class="highlight">
            <thead>
                <tr>
                    <th>Letnik</th>
                </tr>
            </thead>
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
			%niz = "".join(igra[0].split())
                <tr>
                    <td>
			 <a href="/{{niz}}/vec">
                       
                        {{igra[0]}} 
                        </a>
                    </td>
                </tr>
                %end					
					
                
            
               
            </tbody>
        </table>
    </div>
</div>