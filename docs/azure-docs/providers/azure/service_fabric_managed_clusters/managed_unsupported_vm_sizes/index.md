---
title: managed_unsupported_vm_sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_unsupported_vm_sizes
  - service_fabric_managed_clusters
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
<tr><td><b>Name</b></td><td><code>managed_unsupported_vm_sizes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric_managed_clusters.managed_unsupported_vm_sizes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | VM Size id. |
| `name` | `string` | VM Size name. |
| `type` | `string` | VM Size type. |
| `properties` | `object` | VM Sizes properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `managedUnsupportedVMSizes_Get` | `SELECT` | `api-version, location, subscriptionId, vmSize` | Get unsupported vm size for Service Fabric Managed Clusters. |
| `managedUnsupportedVMSizes_List` | `SELECT` | `api-version, location, subscriptionId` | Get the lists of unsupported vm sizes for Service Fabric Managed Clusters. |
