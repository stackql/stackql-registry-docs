---
title: metric_namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_namespaces
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
<tr><td><b>Name</b></td><td><code>metric_namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.metric_namespaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the metric namespace. |
| `name` | `string` | The escaped name of the namespace. |
| `type` | `string` | The type of the namespace. |
| `classification` | `string` | Kind of namespace |
| `properties` | `object` | The fully qualified metric namespace name. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `MetricNamespaces_List` | `SELECT` | `resourceUri` |
