---
title: wait_statistics
hide_title: false
hide_table_of_contents: false
keywords:
  - wait_statistics
  - maria_db
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
<tr><td><b>Name</b></td><td><code>wait_statistics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.maria_db.wait_statistics</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serverName, subscriptionId, waitStatisticsId` | Retrieve wait statistics for specified identifier. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId, data__properties` | Retrieve wait statistics for specified aggregation window. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId, data__properties` | Retrieve wait statistics for specified aggregation window. |
