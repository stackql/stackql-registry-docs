---
title: sync_groups_hub_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_groups_hub_schemas
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
<tr><td><b>Name</b></td><td><code>sync_groups_hub_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.sync_groups_hub_schemas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `lastUpdateTime` | `string` | Last update time of the database schema. |
| `tables` | `array` | List of tables in the database full schema. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` |
| `_list` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` |
