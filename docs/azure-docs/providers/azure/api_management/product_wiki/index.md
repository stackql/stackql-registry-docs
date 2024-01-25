---
title: product_wiki
hide_title: false
hide_table_of_contents: false
keywords:
  - product_wiki
  - api_management
  - azure    
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
<tr><td><b>Name</b></td><td><code>product_wiki</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.product_wiki</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `productId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the Wiki for a Product specified by its identifier. |
| `create_or_update` | `INSERT` | `productId, resourceGroupName, serviceName, subscriptionId` | Creates a new Wiki for a Product or updates an existing one. |
| `delete` | `DELETE` | `If-Match, productId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified Wiki from a Product. |
| `update` | `EXEC` | `If-Match, productId, resourceGroupName, serviceName, subscriptionId` | Updates the details of the Wiki for a Product specified by its identifier. |
