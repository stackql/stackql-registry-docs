---
title: workload_networks_public_ip
hide_title: false
hide_table_of_contents: false
keywords:
  - workload_networks_public_ip
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
<tr><td><b>Name</b></td><td><code>workload_networks_public_ip</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.vmware.workload_networks_public_ip</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `privateCloudName, publicIPId, resourceGroupName, subscriptionId` |
| `list` | `SELECT` | `privateCloudName, resourceGroupName, subscriptionId` |
| `create` | `INSERT` | `privateCloudName, publicIPId, resourceGroupName, subscriptionId` |
| `delete` | `DELETE` | `privateCloudName, publicIPId, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId` |
