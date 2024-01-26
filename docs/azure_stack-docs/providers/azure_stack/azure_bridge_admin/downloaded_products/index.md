---
title: downloaded_products
hide_title: false
hide_table_of_contents: false
keywords:
  - downloaded_products
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
<tr><td><b>Name</b></td><td><code>downloaded_products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.azure_bridge_admin.downloaded_products</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Location of the resource |
| `properties` | `object` | Properties for aggregate usage. |
| `tags` | `object` | List of key value pairs. |
| `type` | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `activationName, productName, resourceGroupName, subscriptionId` | Get a downloaded product. |
| `list` | `SELECT` | `activationName, resourceGroupName, subscriptionId` | Get a list of downloaded products. |
| `create` | `INSERT` | `activationName, productName, resourceGroupName, subscriptionId` | Creates a downloaded product. |
| `delete` | `DELETE` | `activationName, productName, resourceGroupName, subscriptionId` | Delete a downloaded product. |
| `_list` | `EXEC` | `activationName, resourceGroupName, subscriptionId` | Get a list of downloaded products. |
