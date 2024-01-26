---
title: volumes_replications
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes_replications
  - netapp
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
<tr><td><b>Name</b></td><td><code>volumes_replications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.netapp.volumes_replications</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | List all replications for a specified volume |
| `delete` | `DELETE` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Delete the replication connection on the destination volume, and send release to the source replication |
