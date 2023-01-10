---
title: custom_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_metrics
  - analyticsadmin
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
<tr><td><b>Id</b></td><td><code>googleanalytics.analyticsadmin.custom_metrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name for this CustomMetric resource. Format: properties/&#123;property&#125;/customMetrics/&#123;customMetric&#125; |
| `description` | `string` | Optional. Description for this custom dimension. Max length of 150 characters. |
| `displayName` | `string` | Required. Display name for this custom metric as shown in the Analytics UI. Max length of 82 characters, alphanumeric plus space and underscore starting with a letter. Legacy system-generated display names may contain square brackets, but updates to this field will never permit square brackets. |
| `measurementUnit` | `string` | Required. The type for the custom metric's value. |
| `parameterName` | `string` | Required. Immutable. Tagging name for this custom metric. If this is an event-scoped metric, then this is the event parameter name. May only contain alphanumeric and underscore charactes, starting with a letter. Max length of 40 characters for event-scoped metrics. |
| `restrictedMetricType` | `array` | Optional. Types of restricted data that this metric may contain. Required for metrics with CURRENCY measurement unit. Must be empty for metrics with a non-CURRENCY measurement unit. |
| `scope` | `string` | Required. Immutable. The scope of this custom metric. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `properties_customMetrics_get` | `SELECT` | `customMetricsId, propertiesId` | Lookup for a single CustomMetric. |
| `properties_customMetrics_list` | `SELECT` | `propertiesId` | Lists CustomMetrics on a property. |
| `properties_customMetrics_create` | `INSERT` | `propertiesId` | Creates a CustomMetric. |
| `properties_customMetrics_archive` | `EXEC` | `customMetricsId, propertiesId` | Archives a CustomMetric on a property. |
| `properties_customMetrics_patch` | `EXEC` | `customMetricsId, propertiesId` | Updates a CustomMetric on a property. |
