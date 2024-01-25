---
title: alert_rule_recommendations
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_rule_recommendations
  - alerts_management
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
<tr><td><b>Name</b></td><td><code>alert_rule_recommendations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.alerts_management.alert_rule_recommendations</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_resource` | `SELECT` | `resourceUri` | Retrieve alert rule recommendations for a resource. |
| `list_by_target_type` | `SELECT` | `subscriptionId, targetType` | Retrieve alert rule recommendations for a target type. |
| `_list_by_resource` | `EXEC` | `resourceUri` | Retrieve alert rule recommendations for a resource. |
| `_list_by_target_type` | `EXEC` | `subscriptionId, targetType` | Retrieve alert rule recommendations for a target type. |
