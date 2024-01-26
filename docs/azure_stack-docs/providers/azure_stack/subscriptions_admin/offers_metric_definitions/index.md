---
title: offers_metric_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - offers_metric_definitions
  - subscriptions_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>offers_metric_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.subscriptions_admin.offers_metric_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Metric definition name. |
| `metricAvailabilities` | `array` | List of metric definitions. |
| `primaryAggregationType` | `string` | The primary aggregation type for resource metric. |
| `unit` | `string` | The resource metric unit. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `offer, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `offer, resourceGroupName, subscriptionId` |
