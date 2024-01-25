---
title: transparent_data_encryptions
hide_title: false
hide_table_of_contents: false
keywords:
  - transparent_data_encryptions
  - sql
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
<tr><td><b>Name</b></td><td><code>transparent_data_encryptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.transparent_data_encryptions</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId, tdeName` | Gets a logical database's transparent data encryption. |
| `list_by_database` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets a list of the logical database's transparent data encryption. |
| `create_or_update` | `INSERT` | `databaseName, resourceGroupName, serverName, subscriptionId, tdeName` | Updates a logical database's transparent data encryption configuration. |
| `_list_by_database` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets a list of the logical database's transparent data encryption. |
