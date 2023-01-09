---
title: settlementtransactions
hide_title: false
hide_table_of_contents: false
keywords:
  - settlementtransactions
  - content
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
<tr><td><b>Name</b></td><td><code>settlementtransactions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.content.settlementtransactions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `resources` | `array` |  |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#settlementtransactionsListResponse`". |
| `nextPageToken` | `string` | The token for the retrieval of the next page of returns. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `merchantId, settlementId` |
