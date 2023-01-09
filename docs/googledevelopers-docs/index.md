---
title: googledevelopers
hide_title: false
hide_table_of_contents: false
keywords:
  - googledevelopers
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
id: googledevelopers-doc
slug: /providers/googledevelopers

---
Developer APIs by Google.  
    
:::info Provider Summary

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>44</b></span><br />
<span>total methods:&nbsp;<b>1046</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>331</b></span><br />
<span>total selectable resources:&nbsp;<b>243</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation
```bash
REGISTRY PULL googledevelopers v23.01.00114;
```

## Authentication
```javascript

{
  "googledevelopers": {
    /**
      * Type of authentication to use, suported values include: service_account, interactive
      * @type String
      */
    "type": string, 
    /**
      * path to service account key file.
      * @type String
      */
    "credentialsfilepath": string, 
  }
}

```
### Example (Mac/Linux)
```bash

AUTH='{ "googledevelopers": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}'
stackql shell --auth="${AUTH}"

```
### Example (PowerShell)
```powershell

$Auth = "{ 'googledevelopers': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json' }}"
stackql.exe shell --auth=$Auth

```
## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/googledevelopers/abusiveexperiencereport/">abusiveexperiencereport</a><br />
<a href="/providers/googledevelopers/acceleratedmobilepageurl/">acceleratedmobilepageurl</a><br />
<a href="/providers/googledevelopers/androiddeviceprovisioning/">androiddeviceprovisioning</a><br />
<a href="/providers/googledevelopers/androidenterprise/">androidenterprise</a><br />
<a href="/providers/googledevelopers/androidmanagement/">androidmanagement</a><br />
<a href="/providers/googledevelopers/androidpublisher/">androidpublisher</a><br />
<a href="/providers/googledevelopers/area120tables/">area120tables</a><br />
<a href="/providers/googledevelopers/authorizedbuyersmarketplace/">authorizedbuyersmarketplace</a><br />
<a href="/providers/googledevelopers/blogger/">blogger</a><br />
<a href="/providers/googledevelopers/books/">books</a><br />
<a href="/providers/googledevelopers/civicinfo/">civicinfo</a><br />
<a href="/providers/googledevelopers/content/">content</a><br />
<a href="/providers/googledevelopers/customsearch/">customsearch</a><br />
<a href="/providers/googledevelopers/digitalassetlinks/">digitalassetlinks</a><br />
<a href="/providers/googledevelopers/discovery/">discovery</a><br />
<a href="/providers/googledevelopers/displayvideo/">displayvideo</a><br />
<a href="/providers/googledevelopers/domainsrdap/">domainsrdap</a><br />
<a href="/providers/googledevelopers/factchecktools/">factchecktools</a><br />
<a href="/providers/googledevelopers/fitness/">fitness</a><br />
<a href="/providers/googledevelopers/games/">games</a><br />
<a href="/providers/googledevelopers/gamesConfiguration/">gamesConfiguration</a><br />
<a href="/providers/googledevelopers/gamesManagement/">gamesManagement</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/googledevelopers/homegraph/">homegraph</a><br />
<a href="/providers/googledevelopers/indexing/">indexing</a><br />
<a href="/providers/googledevelopers/kgsearch/">kgsearch</a><br />
<a href="/providers/googledevelopers/manufacturers/">manufacturers</a><br />
<a href="/providers/googledevelopers/oauth2/">oauth2</a><br />
<a href="/providers/googledevelopers/pagespeedonline/">pagespeedonline</a><br />
<a href="/providers/googledevelopers/paymentsresellersubscription/">paymentsresellersubscription</a><br />
<a href="/providers/googledevelopers/people/">people</a><br />
<a href="/providers/googledevelopers/playcustomapp/">playcustomapp</a><br />
<a href="/providers/googledevelopers/playdeveloperreporting/">playdeveloperreporting</a><br />
<a href="/providers/googledevelopers/playintegrity/">playintegrity</a><br />
<a href="/providers/googledevelopers/poly/">poly</a><br />
<a href="/providers/googledevelopers/prod_tt_sasportal/">prod_tt_sasportal</a><br />
<a href="/providers/googledevelopers/safebrowsing/">safebrowsing</a><br />
<a href="/providers/googledevelopers/sasportal/">sasportal</a><br />
<a href="/providers/googledevelopers/searchconsole/">searchconsole</a><br />
<a href="/providers/googledevelopers/smartdevicemanagement/">smartdevicemanagement</a><br />
<a href="/providers/googledevelopers/streetviewpublish/">streetviewpublish</a><br />
<a href="/providers/googledevelopers/travelimpactmodel/">travelimpactmodel</a><br />
<a href="/providers/googledevelopers/verifiedaccess/">verifiedaccess</a><br />
<a href="/providers/googledevelopers/versionhistory/">versionhistory</a><br />
<a href="/providers/googledevelopers/webfonts/">webfonts</a><br />
</div>
</div>
