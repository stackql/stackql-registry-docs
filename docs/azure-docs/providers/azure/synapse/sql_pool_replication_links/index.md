---
title: sql_pool_replication_links
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_replication_links
  - synapse
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
<tr><td><b>Name</b></td><td><code>sql_pool_replication_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.sql_pool_replication_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Location of the workspace that contains this firewall rule. |
| `properties` | `object` | Represents the properties of a Sql pool replication link. |
| `type` | `string` | Type of resource this is. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Lists a Sql pool's replication links. |
| `_list` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Lists a Sql pool's replication links. |
| `get_by_name` | `EXEC` | `linkId, resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get SQL pool replication link by name. |
