---
title: online_deployments_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - online_deployments_skus
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
<tr><td><b>Name</b></td><td><code>online_deployments_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ml_services.online_deployments_skus</code></td></tr>
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
| `list` | `SELECT` | `deploymentName, endpointName, resourceGroupName, subscriptionId, workspaceName` |
| `_list` | `EXEC` | `deploymentName, endpointName, resourceGroupName, subscriptionId, workspaceName` |
