---
title: promotions
hide_title: false
hide_table_of_contents: false
keywords:
  - promotions
  - paymentsresellersubscription
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>promotions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.paymentsresellersubscription.promotions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is empty, there are no subsequent pages. |
| `promotions` | `array` | The promotions for the specified partner. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `partners_promotions_list` | `SELECT` | `partnersId` | To retrieve the promotions, such as free trial, that can be used by the partner. It should be autenticated with a service account. |
| `partners_promotions_findEligible` | `EXEC` | `partnersId` | To find eligible promotions for the current user. The API requires user authorization via OAuth. The user is inferred from the authenticated OAuth credential. |
