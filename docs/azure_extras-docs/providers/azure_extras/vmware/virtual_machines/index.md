---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
  - vmware
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.vmware.virtual_machines</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `VirtualMachines_Get` | `SELECT` | `clusterName, privateCloudName, resourceGroupName, subscriptionId, virtualMachineId` |
| `VirtualMachines_List` | `SELECT` | `clusterName, privateCloudName, resourceGroupName, subscriptionId` |
| `VirtualMachines_RestrictMovement` | `EXEC` | `clusterName, privateCloudName, resourceGroupName, subscriptionId, virtualMachineId` |
