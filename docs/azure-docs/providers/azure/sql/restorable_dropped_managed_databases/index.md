---
title: restorable_dropped_managed_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - restorable_dropped_managed_databases
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
<tr><td><b>Name</b></td><td><code>restorable_dropped_managed_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.restorable_dropped_managed_databases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `location` | `string` | Resource location. |
| `properties` | `object` | The restorable dropped managed database's properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RestorableDroppedManagedDatabases_Get` | `SELECT` | `managedInstanceName, resourceGroupName, restorableDroppedDatabaseId, subscriptionId` | Gets a restorable dropped managed database. |
| `RestorableDroppedManagedDatabases_ListByInstance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of restorable dropped managed databases. |
