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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>metrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.logging.metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The client-assigned metric identifier. Examples: "error_count", "nginx/requests".Metric identifiers are limited to 100 characters and can include only the following characters: A-Z, a-z, 0-9, and the special characters _-.,+!*',()%/. The forward-slash character (/) denotes a hierarchy of name pieces, and it cannot be the first character of the name.This field is the [METRIC_ID] part of a metric resource name in the format "projects/PROJECT_ID/metrics/METRIC_ID". Example: If the resource name of a metric is "projects/my-project/metrics/nginx%2Frequests", this field's value is "nginx/requests". |
| <CopyableCode code="description" /> | `string` | Optional. A description of this metric, which is used in documentation. The maximum length of the description is 8000 characters. |
| <CopyableCode code="bucketName" /> | `string` | Optional. The resource name of the Log Bucket that owns the Log Metric. Only Log Buckets in projects are supported. The bucket has to be in the same project as the metric.For example:projects/my-project/locations/global/buckets/my-bucketIf empty, then the Log Metric is considered a non-Bucket Log Metric. |
| <CopyableCode code="bucketOptions" /> | `object` | BucketOptions describes the bucket boundaries used to create a histogram for the distribution. The buckets can be in a linear sequence, an exponential sequence, or each bucket can be specified explicitly. BucketOptions does not include the number of values in each bucket.A bucket has an inclusive lower bound and exclusive upper bound for the values that are counted for that bucket. The upper bound of a bucket must be strictly greater than the lower bound. The sequence of N buckets for a distribution consists of an underflow bucket (number 0), zero or more finite buckets (number 1 through N - 2) and an overflow bucket (number N - 1). The buckets are contiguous: the lower bound of bucket i (i > 0) is the same as the upper bound of bucket i - 1. The buckets span the whole range of finite values: lower bound of the underflow bucket is -infinity and the upper bound of the overflow bucket is +infinity. The finite buckets are so-called because both bounds are finite. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of the metric.This field may not be present for older metrics. |
| <CopyableCode code="disabled" /> | `boolean` | Optional. If set to True, then this metric is disabled and it does not generate any points. |
| <CopyableCode code="filter" /> | `string` | Required. An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced_filters) which is used to match log entries. Example: "resource.type=gae_app AND severity>=ERROR" The maximum length of the filter is 20000 characters. |
| <CopyableCode code="labelExtractors" /> | `object` | Optional. A map from a label key string to an extractor expression which is used to extract data from a log entry field and assign as the label value. Each label key specified in the LabelDescriptor must have an associated extractor expression in this map. The syntax of the extractor expression is the same as for the value_extractor field.The extracted value is converted to the type defined in the label descriptor. If either the extraction or the type conversion fails, the label will have a default value. The default value for a string label is an empty string, for an integer label its 0, and for a boolean label its false.Note that there are upper bounds on the maximum number of labels and the number of active time series that are allowed in a project. |
| <CopyableCode code="metricDescriptor" /> | `object` | Defines a metric type and its schema. Once a metric descriptor is created, deleting or altering it stops data collection and makes the metric type's existing data unusable. |
| <CopyableCode code="resourceName" /> | `string` | Output only. The resource name of the metric: "projects/[PROJECT_ID]/metrics/[METRIC_ID]"  |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp of the metric.This field may not be present for older metrics. |
| <CopyableCode code="valueExtractor" /> | `string` | Optional. A value_extractor is required when using a distribution logs-based metric to extract the values to record from a log entry. Two functions are supported for value extraction: EXTRACT(field) or REGEXP_EXTRACT(field, regex). The arguments are: field: The name of the log entry field from which the value is to be extracted. regex: A regular expression using the Google RE2 syntax (https://github.com/google/re2/wiki/Syntax) with a single capture group to extract data from the specified log entry field. The value of the field is converted to a string before applying the regex. It is an error to specify a regex that does not include exactly one capture group.The result of the extraction must be convertible to a double type, as the distribution always records double values. If either the extraction or the conversion to double fails, then those values are not recorded in the distribution.Example: REGEXP_EXTRACT(jsonPayload.request, ".*quantity=(\d+).*") |
| <CopyableCode code="version" /> | `string` | Deprecated. The API version that created or updated this metric. The v2 format is used by default and cannot be changed. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_metrics_get" /> | `SELECT` | <CopyableCode code="metricsId, projectsId" /> | Gets a logs-based metric. |
| <CopyableCode code="projects_metrics_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists logs-based metrics. |
| <CopyableCode code="projects_metrics_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a logs-based metric. |
| <CopyableCode code="projects_metrics_delete" /> | `DELETE` | <CopyableCode code="metricsId, projectsId" /> | Deletes a logs-based metric. |
| <CopyableCode code="projects_metrics_update" /> | `REPLACE` | <CopyableCode code="metricsId, projectsId" /> | Creates or updates a logs-based metric. |

## `SELECT` examples

Lists logs-based metrics.

```sql
SELECT
name,
description,
bucketName,
bucketOptions,
createTime,
disabled,
filter,
labelExtractors,
metricDescriptor,
resourceName,
updateTime,
valueExtractor,
version
FROM google.logging.metrics
WHERE projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>metrics</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.logging.metrics (
projectsId,
name,
description,
filter,
bucketName,
disabled,
metricDescriptor,
valueExtractor,
labelExtractors,
bucketOptions,
version
)
SELECT 
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ filter }}',
'{{ bucketName }}',
true|false,
'{{ metricDescriptor }}',
'{{ valueExtractor }}',
'{{ labelExtractors }}',
'{{ bucketOptions }}',
'{{ version }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: description
      value: '{{ description }}'
    - name: filter
      value: '{{ filter }}'
    - name: bucketName
      value: '{{ bucketName }}'
    - name: disabled
      value: '{{ disabled }}'
    - name: metricDescriptor
      value:
        - name: name
          value: '{{ name }}'
        - name: type
          value: '{{ type }}'
        - name: labels
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: metricKind
          value: '{{ metricKind }}'
        - name: valueType
          value: '{{ valueType }}'
        - name: unit
          value: '{{ unit }}'
        - name: description
          value: '{{ description }}'
        - name: displayName
          value: '{{ displayName }}'
        - name: metadata
          value:
            - name: launchStage
              value: '{{ launchStage }}'
            - name: samplePeriod
              value: '{{ samplePeriod }}'
            - name: ingestDelay
              value: '{{ ingestDelay }}'
            - name: timeSeriesResourceHierarchyLevel
              value:
                - name: type
                  value: '{{ type }}'
                - name: enumDescriptions
                  value: '{{ enumDescriptions }}'
                - name: enum
                  value: '{{ enum }}'
        - name: launchStage
          value: '{{ launchStage }}'
        - name: monitoredResourceTypes
          value:
            - name: type
              value: '{{ type }}'
    - name: valueExtractor
      value: '{{ valueExtractor }}'
    - name: labelExtractors
      value: '{{ labelExtractors }}'
    - name: bucketOptions
      value:
        - name: linearBuckets
          value:
            - name: numFiniteBuckets
              value: '{{ numFiniteBuckets }}'
            - name: width
              value: '{{ width }}'
            - name: offset
              value: '{{ offset }}'
        - name: exponentialBuckets
          value:
            - name: numFiniteBuckets
              value: '{{ numFiniteBuckets }}'
            - name: growthFactor
              value: '{{ growthFactor }}'
            - name: scale
              value: '{{ scale }}'
        - name: explicitBuckets
          value:
            - name: bounds
              value:
                - name: type
                  value: '{{ type }}'
                - name: format
                  value: '{{ format }}'
    - name: version
      value: '{{ version }}'

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>metrics</code> resource.

```sql
/*+ update */
REPLACE google.logging.metrics
SET 
name = '{{ name }}',
description = '{{ description }}',
filter = '{{ filter }}',
bucketName = '{{ bucketName }}',
disabled = true|false,
metricDescriptor = '{{ metricDescriptor }}',
valueExtractor = '{{ valueExtractor }}',
labelExtractors = '{{ labelExtractors }}',
bucketOptions = '{{ bucketOptions }}',
version = '{{ version }}'
WHERE 
metricsId = '{{ metricsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>metrics</code> resource.

```sql
/*+ delete */
DELETE FROM google.logging.metrics
WHERE metricsId = '{{ metricsId }}'
AND projectsId = '{{ projectsId }}';
```
