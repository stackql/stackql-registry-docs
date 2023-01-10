---
title: products
hide_title: false
hide_table_of_contents: false
keywords:
  - products
  - azure_stack
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
<tr><td><b>Name</b></td><td><code>products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.azure_stack.products</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `properties` | `object` | Properties portion of the product resource. |
| `type` | `string` | Type of Resource. |
| `etag` | `string` | The entity tag used for optimistic concurrency when modifying the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Products_Get` | `SELECT` | `productName, registrationName, resourceGroup, subscriptionId` | Returns the specified product. |
| `Products_List` | `SELECT` | `registrationName, resourceGroup, subscriptionId` | Returns a list of products. |
| `Products_GetProduct` | `EXEC` | `productName, registrationName, resourceGroup, subscriptionId` | Returns the specified product. |
| `Products_GetProducts` | `EXEC` | `productName, registrationName, resourceGroup, subscriptionId` | Returns a list of products. |
| `Products_ListDetails` | `EXEC` | `productName, registrationName, resourceGroup, subscriptionId` | Returns the extended properties of a product. |
| `Products_ListProducts` | `EXEC` | `productName, registrationName, resourceGroup, subscriptionId` | Returns a list of products. |
| `Products_UploadLog` | `EXEC` | `productName, registrationName, resourceGroup, subscriptionId` | Returns the specified product. |
