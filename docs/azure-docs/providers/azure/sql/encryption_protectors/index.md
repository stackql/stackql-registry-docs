---
title: encryption_protectors
hide_title: false
hide_table_of_contents: false
keywords:
  - encryption_protectors
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
<tr><td><b>Name</b></td><td><code>encryption_protectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.encryption_protectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Kind of encryption protector. This is metadata used for the Azure portal experience. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties for an encryption protector execution. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `encryptionProtectorName, resourceGroupName, serverName, subscriptionId` | Gets a server encryption protector. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of server encryption protectors |
| `create_or_update` | `INSERT` | `encryptionProtectorName, resourceGroupName, serverName, subscriptionId` | Updates an existing encryption protector. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Gets a list of server encryption protectors |
| `revalidate` | `EXEC` | `encryptionProtectorName, resourceGroupName, serverName, subscriptionId` | Revalidates an existing encryption protector. |
