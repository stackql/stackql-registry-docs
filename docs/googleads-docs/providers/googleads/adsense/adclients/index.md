---
title: adclients
hide_title: false
hide_table_of_contents: false
keywords:
  - adclients
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
<tr><td><b>Name</b></td><td><code>adclients</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adsense.adclients</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the ad client. Format: accounts/&#123;account&#125;/adclients/&#123;adclient&#125; |
| `productCode` | `string` | Output only. Reporting product code of the ad client. For example, "AFC" for AdSense for Content. Corresponds to the `PRODUCT_CODE` dimension, and present only if the ad client supports reporting. |
| `reportingDimensionId` | `string` | Output only. Unique ID of the ad client as used in the `AD_CLIENT_ID` reporting dimension. Present only if the ad client supports reporting. |
| `state` | `string` | Output only. State of the ad client. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_adclients_get` | `SELECT` | `accountsId, adclientsId` | Gets the ad client from the given resource name. |
| `accounts_adclients_list` | `SELECT` | `accountsId` | Lists all the ad clients available in an account. |
