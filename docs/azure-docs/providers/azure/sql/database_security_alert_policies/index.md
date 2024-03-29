---
title: database_security_alert_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - database_security_alert_policies
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
<tr><td><b>Name</b></td><td><code>database_security_alert_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.database_security_alert_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of a security alert policy. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databaseName, resourceGroupName, securityAlertPolicyName, serverName, subscriptionId` | Gets a database's security alert policy. |
| `list_by_database` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets a list of database's security alert policies. |
| `create_or_update` | `INSERT` | `databaseName, resourceGroupName, securityAlertPolicyName, serverName, subscriptionId` | Creates or updates a database's security alert policy. |
| `_list_by_database` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets a list of database's security alert policies. |
