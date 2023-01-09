---
title: adclients
hide_title: false
hide_table_of_contents: false
keywords:
  - adclients
  - adsensehost
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
<tr><td><b>Id</b></td><td><code>googleads.adsensehost.adclients</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier of this ad client. |
| `kind` | `string` | Kind of resource this is, in this case adsensehost#adClient. |
| `productCode` | `string` | This ad client's product code, which corresponds to the PRODUCT_CODE report dimension. |
| `supportsReporting` | `boolean` | Whether this ad client supports being reported on. |
| `arcOptIn` | `boolean` | Whether this ad client is opted in to ARC. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_adclients_get` | `SELECT` | `accountId, adClientId` | Get information about one of the ad clients in the specified publisher's AdSense account. |
| `accounts_adclients_list` | `SELECT` | `accountId` | List all hosted ad clients in the specified hosted account. |
| `get` | `SELECT` | `adClientId` | Get information about one of the ad clients in the Host AdSense account. |
| `list` | `SELECT` |  | List all host ad clients in this AdSense account. |
