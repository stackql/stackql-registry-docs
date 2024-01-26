---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
  - vmware
  - azure_isv    
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
<tr><td><b>Id</b></td><td><code>azure_isv.vmware.virtual_machines</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `clusterName, privateCloudName, resourceGroupName, subscriptionId, virtualMachineId` |
| `list` | `SELECT` | `clusterName, privateCloudName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `clusterName, privateCloudName, resourceGroupName, subscriptionId` |
| `restrict_movement` | `EXEC` | `clusterName, privateCloudName, resourceGroupName, subscriptionId, virtualMachineId` |
