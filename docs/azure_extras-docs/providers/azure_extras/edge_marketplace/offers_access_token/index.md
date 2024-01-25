---
title: offers_access_token
hide_title: false
hide_table_of_contents: false
keywords:
  - offers_access_token
  - edge_marketplace
  - azure_extras    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>offers_access_token</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.edge_marketplace.offers_access_token</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `accessToken` | `string` | The access token. |
| `diskId` | `string` | The disk id. |
| `status` | `string` | The access token creation status. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `offerId, resourceUri, data__requestId` |
