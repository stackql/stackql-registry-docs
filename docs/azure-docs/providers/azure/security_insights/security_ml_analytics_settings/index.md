---
title: security_ml_analytics_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - security_ml_analytics_settings
  - security_insights
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
<tr><td><b>Id</b></td><td><code>azure.security_insights.security_ml_analytics_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `kind` | `string` | The kind of security ML analytics settings |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SecurityMLAnalyticsSettings_Get` | `SELECT` | `resourceGroupName, settingsResourceName, subscriptionId, workspaceName` | Gets the Security ML Analytics Settings. |
| `SecurityMLAnalyticsSettings_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all Security ML Analytics Settings. |
| `SecurityMLAnalyticsSettings_CreateOrUpdate` | `INSERT` | `resourceGroupName, settingsResourceName, subscriptionId, workspaceName, data__kind` | Creates or updates the Security ML Analytics Settings. |
| `SecurityMLAnalyticsSettings_Delete` | `DELETE` | `resourceGroupName, settingsResourceName, subscriptionId, workspaceName` | Delete the Security ML Analytics Settings. |
