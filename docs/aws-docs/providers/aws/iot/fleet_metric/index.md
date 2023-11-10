---
title: fleet_metric
hide_title: false
hide_table_of_contents: false
keywords:
  - fleet_metric
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>fleet_metric</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleet_metric</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>fleet_metric</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.fleet_metric</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>metric_name</code></td><td><code>string</code></td><td>The name of the fleet metric</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of a fleet metric</td></tr>
<tr><td><code>query_string</code></td><td><code>string</code></td><td>The Fleet Indexing query used by a fleet metric</td></tr>
<tr><td><code>period</code></td><td><code>integer</code></td><td>The period of metric emission in seconds</td></tr>
<tr><td><code>aggregation_field</code></td><td><code>string</code></td><td>The aggregation field to perform aggregation and metric emission</td></tr>
<tr><td><code>query_version</code></td><td><code>string</code></td><td>The version of a Fleet Indexing query used by a fleet metric</td></tr>
<tr><td><code>index_name</code></td><td><code>string</code></td><td>The index name of a fleet metric</td></tr>
<tr><td><code>unit</code></td><td><code>string</code></td><td>The unit of data points emitted by a fleet metric</td></tr>
<tr><td><code>aggregation_type</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>metric_arn</code></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of a fleet metric metric</td></tr>
<tr><td><code>creation_date</code></td><td><code>number</code></td><td>The creation date of a fleet metric</td></tr>
<tr><td><code>last_modified_date</code></td><td><code>number</code></td><td>The last modified date of a fleet metric</td></tr>
<tr><td><code>version</code></td><td><code>number</code></td><td>The version of a fleet metric</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
metric_name,
description,
query_string,
period,
aggregation_field,
query_version,
index_name,
unit,
aggregation_type,
metric_arn,
creation_date,
last_modified_date,
version,
tags
FROM aws.iot.fleet_metric
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;MetricName&gt;'
```
