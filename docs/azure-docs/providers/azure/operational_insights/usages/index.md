---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - operational_insights
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
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.operational_insights.usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `object` | The name of a metric. |
| `currentValue` | `number` | The current value of the metric. |
| `limit` | `number` | The quota limit for the metric. |
| `nextResetTime` | `string` | The time that the metric's value will reset. |
| `quotaPeriod` | `string` | The quota period that determines the length of time between value resets. |
| `unit` | `string` | The units used for the metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Usages_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
