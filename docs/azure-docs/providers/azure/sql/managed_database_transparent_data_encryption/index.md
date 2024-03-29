---
title: managed_database_transparent_data_encryption
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_transparent_data_encryption
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
<tr><td><b>Name</b></td><td><code>managed_database_transparent_data_encryption</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_database_transparent_data_encryption</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId, tdeName` | Gets a managed database's transparent data encryption. |
| `list_by_database` | `SELECT` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of managed database's transparent data encryptions. |
| `create_or_update` | `INSERT` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId, tdeName` | Updates a database's transparent data encryption configuration. |
| `_list_by_database` | `EXEC` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of managed database's transparent data encryptions. |
