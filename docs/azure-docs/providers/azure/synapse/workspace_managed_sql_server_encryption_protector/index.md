---
title: workspace_managed_sql_server_encryption_protector
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_managed_sql_server_encryption_protector
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
<tr><td><b>Name</b></td><td><code>workspace_managed_sql_server_encryption_protector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.workspace_managed_sql_server_encryption_protector</code></td></tr>
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
| `WorkspaceManagedSqlServerEncryptionProtector_Get` | `SELECT` | `encryptionProtectorName, resourceGroupName, subscriptionId, workspaceName` | Get workspace managed sql server's encryption protector. |
| `WorkspaceManagedSqlServerEncryptionProtector_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Get list of encryption protectors for workspace managed sql server. |
| `WorkspaceManagedSqlServerEncryptionProtector_CreateOrUpdate` | `INSERT` | `encryptionProtectorName, resourceGroupName, subscriptionId, workspaceName` | Updates workspace managed sql server's encryption protector. |
| `WorkspaceManagedSqlServerEncryptionProtector_Revalidate` | `EXEC` | `encryptionProtectorName, resourceGroupName, subscriptionId, workspaceName` | Revalidates workspace managed sql server's existing encryption protector. |
