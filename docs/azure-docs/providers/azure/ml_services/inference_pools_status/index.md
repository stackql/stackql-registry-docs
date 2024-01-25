---
title: inference_pools_status
hide_title: false
hide_table_of_contents: false
keywords:
  - inference_pools_status
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
<tr><td><b>Name</b></td><td><code>inference_pools_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ml_services.inference_pools_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `actualCapacity` | `integer` | Gets or sets the actual number of instances in the pool. |
| `groupCount` | `integer` | Gets or sets the actual number of groups in the pool. |
| `requestedCapacity` | `integer` | Gets or sets the requested number of instances for the pool. |
| `reservedCapacity` | `integer` | Gets or sets the number of instances in the pool reserved by the system. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `inferencePoolName, resourceGroupName, subscriptionId, workspaceName` |
