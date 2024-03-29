---
title: deployments_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments_skus
  - cognitive_services
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
<tr><td><b>Name</b></td><td><code>deployments_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cognitive_services.deployments_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `capacity` | `object` | The capacity configuration. |
| `resourceType` | `string` | The resource type name. |
| `sku` | `object` | The resource model definition representing SKU |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `accountName, deploymentName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `accountName, deploymentName, resourceGroupName, subscriptionId` |
