---
title: sql_pool_transparent_data_encryptions
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_transparent_data_encryptions
  - synapse
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
<tr><td><b>Name</b></td><td><code>sql_pool_transparent_data_encryptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.sql_pool_transparent_data_encryptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Resource location. |
| `properties` | `object` | Represents the properties of a database transparent data encryption. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, transparentDataEncryptionName, workspaceName` | Get a SQL pool's transparent data encryption configuration. |
| `list` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get list of SQL pool's transparent data encryption configurations. |
| `create_or_update` | `INSERT` | `resourceGroupName, sqlPoolName, subscriptionId, transparentDataEncryptionName, workspaceName` | Creates or updates a Sql pool's transparent data encryption configuration. |
| `_list` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get list of SQL pool's transparent data encryption configurations. |
