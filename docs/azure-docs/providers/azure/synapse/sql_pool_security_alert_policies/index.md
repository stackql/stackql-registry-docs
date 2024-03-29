---
title: sql_pool_security_alert_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_security_alert_policies
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
<tr><td><b>Name</b></td><td><code>sql_pool_security_alert_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.sql_pool_security_alert_policies</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, securityAlertPolicyName, sqlPoolName, subscriptionId, workspaceName` | Get a Sql pool's security alert policy. |
| `list` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get a list of Sql pool's security alert policies. |
| `create_or_update` | `INSERT` | `resourceGroupName, securityAlertPolicyName, sqlPoolName, subscriptionId, workspaceName` | Create or update a Sql pool's security alert policy. |
| `_list` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get a list of Sql pool's security alert policies. |
