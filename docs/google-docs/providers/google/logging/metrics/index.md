---
title: metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics
  - logging
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.logging.metrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The client-assigned metric identifier. Examples: "error_count", "nginx/requests".Metric identifiers are limited to 100 characters and can include only the following characters: A-Z, a-z, 0-9, and the special characters _-.,+!*',()%/. The forward-slash character (/) denotes a hierarchy of name pieces, and it cannot be the first character of the name.This field is the [METRIC_ID] part of a metric resource name in the format "projects/PROJECT_ID/metrics/METRIC_ID". Example: If the resource name of a metric is "projects/my-project/metrics/nginx%2Frequests", this field's value is "nginx/requests". |
| `description` | `string` | Optional. A description of this metric, which is used in documentation. The maximum length of the description is 8000 characters. |
| `labelExtractors` | `object` | Optional. A map from a label key string to an extractor expression which is used to extract data from a log entry field and assign as the label value. Each label key specified in the LabelDescriptor must have an associated extractor expression in this map. The syntax of the extractor expression is the same as for the value_extractor field.The extracted value is converted to the type defined in the label descriptor. If the either the extraction or the type conversion fails, the label will have a default value. The default value for a string label is an empty string, for an integer label its 0, and for a boolean label its false.Note that there are upper bounds on the maximum number of labels and the number of active time series that are allowed in a project. |
| `filter` | `string` | Required. An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced_filters) which is used to match log entries. Example: "resource.type=gae_app AND severity&gt;=ERROR" The maximum length of the filter is 20000 characters. |
| `metricDescriptor` | `object` | Defines a metric type and its schema. Once a metric descriptor is created, deleting or altering it stops data collection and makes the metric type's existing data unusable. |
| `version` | `string` | Deprecated. The API version that created or updated this metric. The v2 format is used by default and cannot be changed. |
| `disabled` | `boolean` | Optional. If set to True, then this metric is disabled and it does not generate any points. |
| `updateTime` | `string` | Output only. The last update timestamp of the metric.This field may not be present for older metrics. |
| `bucketOptions` | `object` | BucketOptions describes the bucket boundaries used to create a histogram for the distribution. The buckets can be in a linear sequence, an exponential sequence, or each bucket can be specified explicitly. BucketOptions does not include the number of values in each bucket.A bucket has an inclusive lower bound and exclusive upper bound for the values that are counted for that bucket. The upper bound of a bucket must be strictly greater than the lower bound. The sequence of N buckets for a distribution consists of an underflow bucket (number 0), zero or more finite buckets (number 1 through N - 2) and an overflow bucket (number N - 1). The buckets are contiguous: the lower bound of bucket i (i &gt; 0) is the same as the upper bound of bucket i - 1. The buckets span the whole range of finite values: lower bound of the underflow bucket is -infinity and the upper bound of the overflow bucket is +infinity. The finite buckets are so-called because both bounds are finite. |
| `valueExtractor` | `string` | Optional. A value_extractor is required when using a distribution logs-based metric to extract the values to record from a log entry. Two functions are supported for value extraction: EXTRACT(field) or REGEXP_EXTRACT(field, regex). The argument are: 1. field: The name of the log entry field from which the value is to be extracted. 2. regex: A regular expression using the Google RE2 syntax (https://github.com/google/re2/wiki/Syntax) with a single capture group to extract data from the specified log entry field. The value of the field is converted to a string before applying the regex. It is an error to specify a regex that does not include exactly one capture group.The result of the extraction must be convertible to a double type, as the distribution always records double values. If either the extraction or the conversion to double fails, then those values are not recorded in the distribution.Example: REGEXP_EXTRACT(jsonPayload.request, ".*quantity=(\d+).*") |
| `createTime` | `string` | Output only. The creation timestamp of the metric.This field may not be present for older metrics. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_metrics_get` | `SELECT` | `metricsId, projectsId` | Gets a logs-based metric. |
| `projects_metrics_list` | `SELECT` | `projectsId` | Lists logs-based metrics. |
| `projects_metrics_create` | `INSERT` | `projectsId` | Creates a logs-based metric. |
| `projects_metrics_delete` | `DELETE` | `metricsId, projectsId` | Deletes a logs-based metric. |
| `projects_metrics_update` | `EXEC` | `metricsId, projectsId` | Creates or updates a logs-based metric. |
