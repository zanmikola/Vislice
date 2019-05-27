% import model
% rebase ('base.tpl', title='Vislice')


  <h1>Vislice</h1>

  <blockquote>
    Vislice so najboljša igra za preganjanje dolgčasa (poleg tetrisa).
    <small>Študentje</small>
  </blockquote>

 <table>
  <tr>
   <td>

   <h2>{{igra.pravilni_del_gesla()}}</h2>

   Nepravlini ugibi: <b>{{igra.nepravilni_del_gesla()}} </b>

   </td>

   <td>
   <img src="/img/{{igra.stevilo_napacnih()}}.jpg" alt="obesanje" />
   </td>
   
  </tr>
 </table>


  % if stanje == model.ZMAGA:
  <h1> ZMAGA! </h1>
  
  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </from>

  % elif stanje == model.PORAZ:
  <h1> IZGUBILI STE! </h1>
  Pravilno geslo: <h4> {{igra.geslo}} </h4>
<form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </from>
  % else:

  <form action="/igra/" method="POST">
    Črka: <input type="text" name="crka">
    <button type="submit">Pošlji ugib</button>
  </form>
  % end
