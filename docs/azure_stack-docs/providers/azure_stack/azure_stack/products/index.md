---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - azure_stack
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.azure_stack.products</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | URI to the next page. |
| `value` | `array` | List of products. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `registrationName, resourceGroup, subscriptionId` | Returns a list of products. |
| `list_by_product_name` | `SELECT` | `productName, registrationName, resourceGroup, subscriptionId` | Returns a list of products. |
| `_list` | `EXEC` | `registrationName, resourceGroup, subscriptionId` | Returns a list of products. |
| `exec_get` | `EXEC` | `productName, registrationName, resourceGroup, subscriptionId` | Returns a list of products. |
| `upload_log` | `EXEC` | `productName, registrationName, resourceGroup, subscriptionId` | Returns the specified product. |
