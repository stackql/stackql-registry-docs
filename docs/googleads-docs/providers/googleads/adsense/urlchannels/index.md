---
title: urlchannels
hide_title: false
hide_table_of_contents: false
keywords:
  - urlchannels
  - adsense
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>urlchannels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adsense.urlchannels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the URL channel. Format: accounts/&#123;account&#125;/adclients/&#123;adclient&#125;/urlchannels/&#123;urlchannel&#125; |
| `reportingDimensionId` | `string` | Output only. Unique ID of the custom channel as used in the `URL_CHANNEL_ID` reporting dimension. |
| `uriPattern` | `string` | URI pattern of the channel. Does not include "http://" or "https://". Example: www.example.com/home |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_adclients_urlchannels_get` | `SELECT` | `accountsId, adclientsId, urlchannelsId` | Gets information about the selected url channel. |
| `accounts_adclients_urlchannels_list` | `SELECT` | `accountsId, adclientsId` | Lists active url channels. |
