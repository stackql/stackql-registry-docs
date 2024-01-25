---
title: managed_databases_inaccessible_by_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_databases_inaccessible_by_instance
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
<tr><td><b>Name</b></td><td><code>managed_databases_inaccessible_by_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_databases_inaccessible_by_instance</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Resource location. |
| `properties` | `object` | The managed database's properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` |
