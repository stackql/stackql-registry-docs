---
title: adclients_adcode
hide_title: false
hide_table_of_contents: false
keywords:
  - adclients_adcode
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
<tr><td><b>Name</b></td><td><code>adclients_adcode</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adsense.adclients_adcode</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `ampBody` | `string` | Output only. The AdSense code snippet to add to the body of an AMP page. |
| `ampHead` | `string` | Output only. The AdSense code snippet to add to the head of an AMP page. |
| `adCode` | `string` | Output only. The AdSense code snippet to add to the head of an HTML page. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `accounts_adclients_getAdcode` | `SELECT` | `accountsId, adclientsId` |
