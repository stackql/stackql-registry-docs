---
title: product
hide_title: false
hide_table_of_contents: false
keywords:
  - product
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
<tr><td><b>Name</b></td><td><code>product</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.azure_stack.product</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `etag` | `string` | The entity tag used for optimistic concurrency when modifying the resource. |
| `properties` | `object` | Properties portion of the product resource. |
| `type` | `string` | Type of Resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `productName, registrationName, resourceGroup, subscriptionId` |
| `exec_get` | `EXEC` | `productName, registrationName, resourceGroup, subscriptionId` |
