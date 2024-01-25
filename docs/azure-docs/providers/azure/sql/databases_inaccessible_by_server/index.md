---
title: databases_inaccessible_by_server
hide_title: false
hide_table_of_contents: false
keywords:
  - databases_inaccessible_by_server
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
<tr><td><b>Name</b></td><td><code>databases_inaccessible_by_server</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.databases_inaccessible_by_server</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Azure Active Directory identity configuration for a resource. |
| `kind` | `string` | Kind of database. This is metadata used for the Azure portal experience. |
| `location` | `string` | Resource location. |
| `managedBy` | `string` | Resource that manages the database. |
| `properties` | `object` | The database's properties. |
| `sku` | `object` | An ARM Resource SKU. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `resourceGroupName, serverName, subscriptionId` |
| `_list` | `EXEC` | `resourceGroupName, serverName, subscriptionId` |
