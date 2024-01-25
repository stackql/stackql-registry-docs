---
title: recoverable_managed_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - recoverable_managed_databases
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
<tr><td><b>Name</b></td><td><code>recoverable_managed_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.recoverable_managed_databases</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `managedInstanceName, recoverableDatabaseName, resourceGroupName, subscriptionId` | Gets a recoverable managed database. |
| `list_by_instance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of recoverable managed databases. |
| `_list_by_instance` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of recoverable managed databases. |
