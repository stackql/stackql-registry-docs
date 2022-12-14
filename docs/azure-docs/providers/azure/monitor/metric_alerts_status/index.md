---
title: metric_alerts_status
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_alerts_status
  - monitor
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
<tr><td><b>Name</b></td><td><code>metric_alerts_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.metric_alerts_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The alert rule arm id. |
| `name` | `string` | The status name. |
| `properties` | `object` | An alert status properties. |
| `type` | `string` | The extended resource type name. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `MetricAlertsStatus_List` | `SELECT` | `resourceGroupName, ruleName, subscriptionId` |
| `MetricAlertsStatus_ListByName` | `SELECT` | `resourceGroupName, ruleName, statusName, subscriptionId` |
