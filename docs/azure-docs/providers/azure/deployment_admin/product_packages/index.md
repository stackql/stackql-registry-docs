---
title: product_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - product_packages
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
<tr><td><b>Name</b></td><td><code>product_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.deployment_admin.product_packages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `type` | `string` | Type of Resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties for Product package. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ProductPackages_Get` | `SELECT` | `packageId, subscriptionId` | Retrieves the specific product package details. |
| `ProductPackages_List` | `SELECT` | `subscriptionId` | Returns an array of product packages. |
| `ProductPackages_Create` | `INSERT` | `packageId, subscriptionId` | Creates a new product package. |
| `ProductPackages_Delete` | `DELETE` | `packageId, subscriptionId` | Deletes a product package. |
