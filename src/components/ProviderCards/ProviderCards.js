import React from 'react';
import {providers, getProviderSiteUrl} from '@site/src/configs/providers'

const moveCurrentProviderToTop = (allProviders, currentProvider) => {
  const currentProviderIndex = allProviders.findIndex(provider => provider.name === currentProvider)
  if(currentProviderIndex > -1){
    const currentProvider = allProviders.splice(currentProviderIndex, 1)
    allProviders.unshift(currentProvider[0])
  }
  return allProviders
}

const ProviderCards = props => {  
  const { currentProvider } = props;

  const orderedProviders = moveCurrentProviderToTop(providers, currentProvider);

  return orderedProviders.map(provider =>{
    const {name, title} = provider
    return <article class="col col--4 margin-bottom--lg">
    <a class="card padding--lg cardContainer" href={getProviderSiteUrl(name)}>
      <div class="row">
      <div class="col col--2 cardTitleCol"><img src={`/img/providers/${name}/${name}.png`} /></div>
      <div class="col col--10 cardTitleCol"><h2 class="text--truncate cardTitle" title={title}>{title}</h2></div>  
      </div>
      <div class="row">
      <div class="col col--12 cardTitleCol">
      <p class="text--truncate cardDescription">{provider.description}</p>
      </div>
      </div>
    </a>
  </article>
  })

}

export default ProviderCards