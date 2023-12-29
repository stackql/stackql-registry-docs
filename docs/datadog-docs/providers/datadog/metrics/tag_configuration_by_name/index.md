---
title: tag_configuration_by_name
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_configuration_by_name
  - metrics
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_configuration_by_name</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.metrics.tag_configuration_by_name</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The metric name for this resource. |
| `attributes` | `object` | Object containing the definition of a metric tag configuration attributes. |
| `type` | `string` | The metric tag configuration resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_tag_configuration_by_name` | `SELECT` | `metric_name, dd_site` |
| `_list_tag_configuration_by_name` | `EXEC` | `metric_name, dd_site` |
