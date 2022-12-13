---
title: restorable_dropped_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - restorable_dropped_databases
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
<tr><td><b>Name</b></td><td><code>restorable_dropped_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.restorable_dropped_databases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `location` | `string` | Resource location. |
| `properties` | `object` | The restorable dropped database's properties. |
| `sku` | `object` | An ARM Resource SKU. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RestorableDroppedDatabases_Get` | `SELECT` | `resourceGroupName, restorableDroppedDatabaseId, serverName, subscriptionId` | Gets a restorable dropped database. |
| `RestorableDroppedDatabases_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of restorable dropped databases. |
