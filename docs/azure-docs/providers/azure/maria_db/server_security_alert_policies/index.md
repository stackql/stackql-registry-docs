---
title: server_security_alert_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - server_security_alert_policies
  - maria_db
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
<tr><td><b>Name</b></td><td><code>server_security_alert_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.maria_db.server_security_alert_policies</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerSecurityAlertPolicies_Get` | `SELECT` | `resourceGroupName, securityAlertPolicyName, serverName, subscriptionId` | Get a server's security alert policy. |
| `ServerSecurityAlertPolicies_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Get the server's threat detection policies. |
| `ServerSecurityAlertPolicies_CreateOrUpdate` | `INSERT` | `resourceGroupName, securityAlertPolicyName, serverName, subscriptionId` | Creates or updates a threat detection policy. |
