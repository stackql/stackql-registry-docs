---
title: server_security_alert_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - server_security_alert_policies
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
<tr><td><b>Name</b></td><td><code>server_security_alert_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.server_security_alert_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of a security alert policy. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, securityAlertPolicyName, serverName, subscriptionId` | Get a server's security alert policy. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Get the server's threat detection policies. |
| `create_or_update` | `INSERT` | `resourceGroupName, securityAlertPolicyName, serverName, subscriptionId` | Creates or updates a threat detection policy. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Get the server's threat detection policies. |
