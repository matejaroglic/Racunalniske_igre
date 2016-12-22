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
                <tr>
                    <td>
                       
                        {{igra[0]}} 
                        
                    </td>
                </tr>
                %end					
					
                
            
               
            </tbody>
        </table>
    </div>
</div>