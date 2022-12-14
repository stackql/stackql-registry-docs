---
title: workspace_managed_sql_server_dedicated_sql_minimal_tls_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_managed_sql_server_dedicated_sql_minimal_tls_settings
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
<tr><td><b>Name</b></td><td><code>workspace_managed_sql_server_dedicated_sql_minimal_tls_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.workspace_managed_sql_server_dedicated_sql_minimal_tls_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of a dedicated sql minimal tls settings. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkspaceManagedSqlServerDedicatedSQLMinimalTlsSettings_Get` | `SELECT` | `dedicatedSQLminimalTlsSettingsName, resourceGroupName, subscriptionId, workspaceName` | Get workspace managed sql server's minimal tls settings. |
| `WorkspaceManagedSqlServerDedicatedSQLMinimalTlsSettings_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | List workspace managed sql server's minimal tls settings. |
| `WorkspaceManagedSqlServerDedicatedSQLMinimalTlsSettings_Update` | `EXEC` | `dedicatedSQLminimalTlsSettingsName, resourceGroupName, subscriptionId, workspaceName` | Update workspace managed sql server's minimal tls settings. |
