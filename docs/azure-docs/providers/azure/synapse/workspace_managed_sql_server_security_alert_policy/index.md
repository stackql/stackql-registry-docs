---
title: workspace_managed_sql_server_security_alert_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_managed_sql_server_security_alert_policy
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
<tr><td><b>Name</b></td><td><code>workspace_managed_sql_server_security_alert_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.workspace_managed_sql_server_security_alert_policy</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkspaceManagedSqlServerSecurityAlertPolicy_Get` | `SELECT` | `resourceGroupName, securityAlertPolicyName, subscriptionId, workspaceName` | Get a workspace managed sql server's security alert policy. |
| `WorkspaceManagedSqlServerSecurityAlertPolicy_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Get workspace managed sql server's threat detection policies. |
| `WorkspaceManagedSqlServerSecurityAlertPolicy_CreateOrUpdate` | `INSERT` | `resourceGroupName, securityAlertPolicyName, subscriptionId, workspaceName` | Create or Update a workspace managed sql server's threat detection policy. |
