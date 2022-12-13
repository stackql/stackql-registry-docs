---
title: product_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - product_deployments
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
<tr><td><b>Name</b></td><td><code>product_deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.deployment_admin.product_deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `properties` | `object` | Product deployment resource properties |
| `type` | `string` | Type of Resource. |
| `eTag` | `string` | entity tag |
| `location` | `string` | Location of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ProductDeployments_Get` | `SELECT` | `productId, subscriptionId` |
| `ProductDeployments_List` | `SELECT` | `subscriptionId` |
