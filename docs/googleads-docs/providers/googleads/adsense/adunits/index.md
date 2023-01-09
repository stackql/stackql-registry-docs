---
title: adunits
hide_title: false
hide_table_of_contents: false
keywords:
  - adunits
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
<tr><td><b>Name</b></td><td><code>adunits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adsense.adunits</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the ad unit. Format: accounts/&#123;account&#125;/adclients/&#123;adclient&#125;/adunits/&#123;adunit&#125; |
| `reportingDimensionId` | `string` | Output only. Unique ID of the ad unit as used in the `AD_UNIT_ID` reporting dimension. |
| `state` | `string` | State of the ad unit. |
| `contentAdsSettings` | `object` | Settings specific to content ads (AFC). |
| `displayName` | `string` | Required. Display name of the ad unit, as provided when the ad unit was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_adclients_adunits_get` | `SELECT` | `accountsId, adclientsId, adunitsId` | Gets an ad unit from a specified account and ad client. |
| `accounts_adclients_adunits_list` | `SELECT` | `accountsId, adclientsId` | Lists all ad units under a specified account and ad client. |
| `accounts_adclients_adunits_create` | `INSERT` | `accountsId, adclientsId` | Creates an ad unit. This method can only be used by projects enabled for the [AdSense for Platforms](https://developers.google.com/adsense/platforms/) product. Note that ad units can only be created for ad clients with an "AFC" product code. For more info see the [AdClient resource](/adsense/management/reference/rest/v2/accounts.adclients). For now, this method can only be used to create `DISPLAY` ad units. See: https://support.google.com/adsense/answer/9183566 |
| `accounts_adclients_adunits_patch` | `EXEC` | `accountsId, adclientsId, adunitsId` | Updates an ad unit. This method can only be used by projects enabled for the [AdSense for Platforms](https://developers.google.com/adsense/platforms/) product. For now, this method can only be used to update `DISPLAY` ad units. See: https://support.google.com/adsense/answer/9183566 |
