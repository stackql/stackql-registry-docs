---
title: adunits__ad_code
hide_title: false
hide_table_of_contents: false
keywords:
  - adunits__ad_code
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
<tr><td><b>Name</b></td><td><code>adunits__ad_code</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adsensehost.adunits__ad_code</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `adCode` | `string` | The ad code snippet. |
| `kind` | `string` | Kind this is, in this case adsensehost#adCode. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `accounts_adunits_getAdCode` | `SELECT` | `accountId, adClientId, adUnitId` |
