---
title: alert_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_rules
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
<tr><td><b>Name</b></td><td><code>alert_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.alert_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `kind` | `string` | The kind of the alert rule |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AlertRules_Get` | `SELECT` | `resourceGroupName, ruleId, subscriptionId, workspaceName` | Gets the alert rule. |
| `AlertRules_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all alert rules. |
| `AlertRules_CreateOrUpdate` | `INSERT` | `resourceGroupName, ruleId, subscriptionId, workspaceName, data__kind` | Creates or updates the alert rule. |
| `AlertRules_Delete` | `DELETE` | `resourceGroupName, ruleId, subscriptionId, workspaceName` | Delete the alert rule. |
