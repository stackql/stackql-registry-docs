---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - azure_bridge_admin
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
<tr><td><b>Id</b></td><td><code>azure_stack.azure_bridge_admin.products</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Location of the resource |
| `properties` | `object` | Properties for a product. |
| `tags` | `object` | List of key value pairs. |
| `type` | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `activationName, productName, resourceGroupName, subscriptionId` | Return product name. |
| `list` | `SELECT` | `activationName, resourceGroupName, subscriptionId` | Return product name. |
| `_list` | `EXEC` | `activationName, resourceGroupName, subscriptionId` | Return product name. |
| `download` | `EXEC` | `activationName, productName, resourceGroupName, subscriptionId` | Downloads a product from azure marketplace. |
