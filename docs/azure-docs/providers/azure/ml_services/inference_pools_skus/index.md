---
title: inference_pools_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - inference_pools_skus
  - ml_services
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
<tr><td><b>Name</b></td><td><code>inference_pools_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ml_services.inference_pools_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `capacity` | `object` | SKU capacity information |
| `resourceType` | `string` | The resource type name. |
| `sku` | `object` | SkuSetting fulfills the need for stripped down SKU info in ARM contract. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `inferencePoolName, resourceGroupName, subscriptionId, workspaceName` |
| `_list` | `EXEC` | `inferencePoolName, resourceGroupName, subscriptionId, workspaceName` |
