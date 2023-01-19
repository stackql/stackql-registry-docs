---
title: custom_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_metrics
  - analytics
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.custom_metrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Custom metric ID. |
| `name` | `string` | Name of the custom metric. |
| `kind` | `string` | Kind value for a custom metric. Set to "analytics#customMetric". It is a read-only field. |
| `webPropertyId` | `string` | Property ID. |
| `updated` | `string` | Time the custom metric was last modified. |
| `min_value` | `string` | Min value of custom metric. |
| `selfLink` | `string` | Link for the custom metric |
| `index` | `integer` | Index of the custom metric. |
| `accountId` | `string` | Account ID. |
| `active` | `boolean` | Boolean indicating whether the custom metric is active. |
| `max_value` | `string` | Max value of custom metric. |
| `scope` | `string` | Scope of the custom metric: HIT or PRODUCT. |
| `parentLink` | `object` | Parent link for the custom metric. Points to the property to which the custom metric belongs. |
| `type` | `string` | Data type of custom metric. |
| `created` | `string` | Time the custom metric was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `management_customMetrics_get` | `SELECT` | `accountId, customMetricId, webPropertyId` | Get a custom metric to which the user has access. |
| `management_customMetrics_list` | `SELECT` | `accountId, webPropertyId` | Lists custom metrics to which the user has access. |
| `management_customMetrics_insert` | `EXEC` | `accountId, webPropertyId` | Create a new custom metric. |
| `management_customMetrics_patch` | `EXEC` | `accountId, customMetricId, webPropertyId` | Updates an existing custom metric. This method supports patch semantics. |
| `management_customMetrics_update` | `EXEC` | `accountId, customMetricId, webPropertyId` | Updates an existing custom metric. |
