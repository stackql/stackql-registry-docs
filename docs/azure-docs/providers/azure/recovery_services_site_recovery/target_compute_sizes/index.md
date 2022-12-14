---
title: target_compute_sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - target_compute_sizes
  - recovery_services_site_recovery
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
<tr><td><b>Name</b></td><td><code>target_compute_sizes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.target_compute_sizes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The Id. |
| `name` | `string` | The name. |
| `properties` | `object` | Represents applicable recovery vm sizes properties. |
| `type` | `string` | The Type of the object. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `TargetComputeSizes_ListByReplicationProtectedItems` | `SELECT` | `api-version, fabricName, protectionContainerName, replicatedProtectedItemName, resourceGroupName, resourceName, subscriptionId` |
