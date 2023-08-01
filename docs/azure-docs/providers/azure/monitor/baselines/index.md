---
title: baselines
hide_title: false
hide_table_of_contents: false
keywords:
  - baselines
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
<tr><td><b>Name</b></td><td><code>baselines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.baselines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The metric baseline Id. |
| `name` | `string` | The name of the metric for which the baselines were retrieved. |
| `properties` | `object` | The response to a metric baselines query. |
| `type` | `string` | The resource type of the metric baseline resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Baselines_List` | `SELECT` | `resourceUri` |
