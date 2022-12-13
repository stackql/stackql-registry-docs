import React from 'react';
import {providers} from '../../../src/configs/providers'

const ProviderCards = () =>{
  return providers.map(provider =>{
    const name = provider.name
    return <article class="col col--4 margin-bottom--lg">
    <a class="card padding--lg cardContainer" href="/providers/aws/">
      <div class="row">
      <div class="col col--2 cardTitleCol"><img src={`/img/providers/${name}/${name}.png`} /></div>
      <div class="col col--10 cardTitleCol"><h2 class="text--truncate cardTitle" title={name.toUpperCase()}>{name.toUpperCase()}</h2></div>  
      </div>
      <div class="row">
      <div class="col col--12 cardTitleCol">
      <p class="text--truncate cardDescription">provider.description</p>
      </div>
      </div>
    </a>
  </article>
  })

}

export default ProviderCards