---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - postgresql_hsc
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
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.postgresql_hsc.servers</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, resourceGroupName, serverName, subscriptionId` | Gets information about a server in cluster. |
| `list_by_cluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Lists servers of a cluster. |
| `_list_by_cluster` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Lists servers of a cluster. |
