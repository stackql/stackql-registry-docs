---
title: product_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - product_secrets
  - deployment_admin
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
<tr><td><b>Name</b></td><td><code>product_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.deployment_admin.product_secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties of product secret. |
| `type` | `string` | Type of Resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `packageId, secretName, subscriptionId` | Returns the specific product secret. |
| `list` | `SELECT` | `packageId, subscriptionId` | Returns an array of product secrets. |
| `_list` | `EXEC` | `packageId, subscriptionId` | Returns an array of product secrets. |
| `set` | `EXEC` | `packageId, secretName, subscriptionId` | Imports a product secret. |
| `validate` | `EXEC` | `packageId, secretName, subscriptionId` | Validates a product secret. |
