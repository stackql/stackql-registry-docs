---
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
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
<tr><td><b>Name</b></td><td><code>configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.postgresql_hsc.configurations</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, configurationName, resourceGroupName, subscriptionId` | Gets information of a configuration for coordinator and nodes. |
| `list_by_cluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | List all the configurations of a cluster. |
| `list_by_server` | `SELECT` | `clusterName, resourceGroupName, serverName, subscriptionId` | List all the configurations of a server in cluster. |
| `_list_by_cluster` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | List all the configurations of a cluster. |
| `_list_by_server` | `EXEC` | `clusterName, resourceGroupName, serverName, subscriptionId` | List all the configurations of a server in cluster. |
