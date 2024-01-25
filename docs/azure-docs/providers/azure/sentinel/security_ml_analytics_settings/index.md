---
title: security_ml_analytics_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - security_ml_analytics_settings
  - sentinel
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
<tr><td><b>Name</b></td><td><code>security_ml_analytics_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sentinel.security_ml_analytics_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `kind` | `string` | The kind of security ML analytics settings |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, settingsResourceName, subscriptionId, workspaceName` | Gets the Security ML Analytics Settings. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all Security ML Analytics Settings. |
| `create_or_update` | `INSERT` | `resourceGroupName, settingsResourceName, subscriptionId, workspaceName, data__kind` | Creates or updates the Security ML Analytics Settings. |
| `delete` | `DELETE` | `resourceGroupName, settingsResourceName, subscriptionId, workspaceName` | Delete the Security ML Analytics Settings. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Gets all Security ML Analytics Settings. |
