---
title: metric_filter
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_filter
  - logs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>metric_filter</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metric_filter</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>metric_filter</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.logs.metric_filter</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>filter_name</code></td><td><code>string</code></td><td>A name for the metric filter.</td></tr>
<tr><td><code>filter_pattern</code></td><td><code>string</code></td><td>Pattern that Logs follows to interpret each entry in a log.</td></tr>
<tr><td><code>log_group_name</code></td><td><code>string</code></td><td>Existing log group that you want to associate with this filter.</td></tr>
<tr><td><code>metric_transformations</code></td><td><code>array</code></td><td>A collection of information that defines how metric data gets emitted.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>metric_filter</code> resource, the following permissions are required:

### Read
```json
logs:DescribeMetricFilters
```

### Update
```json
logs:PutMetricFilter,
logs:DescribeMetricFilters
```

### Delete
```json
logs:DeleteMetricFilter
```


## Example
```sql
SELECT
region,
filter_name,
filter_pattern,
log_group_name,
metric_transformations
FROM awscc.logs.metric_filter
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;LogGroupName&gt;'
AND data__Identifier = '&lt;FilterName&gt;'
```
