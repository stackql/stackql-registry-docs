---
title: workload_networks_dhcp
hide_title: false
hide_table_of_contents: false
keywords:
  - workload_networks_dhcp
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
<tr><td><b>Name</b></td><td><code>workload_networks_dhcp</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.vmware.workload_networks_dhcp</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `dhcpId, privateCloudName, resourceGroupName, subscriptionId` |
| `list` | `SELECT` | `privateCloudName, resourceGroupName, subscriptionId` |
| `create` | `INSERT` | `dhcpId, privateCloudName, resourceGroupName, subscriptionId` |
| `delete` | `DELETE` | `dhcpId, privateCloudName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId` |
| `update` | `EXEC` | `dhcpId, privateCloudName, resourceGroupName, subscriptionId` |
