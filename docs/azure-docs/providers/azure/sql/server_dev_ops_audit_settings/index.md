---
title: server_dev_ops_audit_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - server_dev_ops_audit_settings
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
<tr><td><b>Name</b></td><td><code>server_dev_ops_audit_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.server_dev_ops_audit_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of a server DevOps audit settings. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerDevOpsAuditSettings_Get` | `SELECT` | `devOpsAuditingSettingsName, resourceGroupName, serverName, subscriptionId` | Gets a server's DevOps audit settings. |
| `ServerDevOpsAuditSettings_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Lists DevOps audit settings of a server. |
| `ServerDevOpsAuditSettings_CreateOrUpdate` | `INSERT` | `devOpsAuditingSettingsName, resourceGroupName, serverName, subscriptionId` | Creates or updates a server's DevOps audit settings. |
