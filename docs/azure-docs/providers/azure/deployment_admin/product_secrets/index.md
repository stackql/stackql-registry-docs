---
title: product_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - product_secrets
  - deployment_admin
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
<tr><td><b>Name</b></td><td><code>product_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.deployment_admin.product_secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `properties` | `object` | Properties of product secret. |
| `type` | `string` | Type of Resource. |
| `location` | `string` | Location of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ProductSecrets_GET` | `SELECT` | `packageId, secretName, subscriptionId` | Returns the specific product secret. |
| `ProductSecrets_List` | `SELECT` | `packageId, subscriptionId` | Returns an array of product secrets. |
| `ProductSecrets_Set` | `EXEC` | `packageId, secretName, subscriptionId` | Imports a product secret. |
| `ProductSecrets_Validate` | `EXEC` | `packageId, secretName, subscriptionId` | Validates a product secret. |
