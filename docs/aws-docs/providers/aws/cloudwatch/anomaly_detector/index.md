---
title: anomaly_detector
hide_title: false
hide_table_of_contents: false
keywords:
  - anomaly_detector
  - cloudwatch
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>anomaly_detector</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anomaly_detector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>anomaly_detector</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudwatch.anomaly_detector</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>metric_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>stat</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>metric_math_anomaly_detector</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>dimensions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>namespace</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>single_metric_anomaly_detector</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
metric_name,
stat,
configuration,
metric_math_anomaly_detector,
dimensions,
id,
namespace,
single_metric_anomaly_detector
FROM aws.cloudwatch.anomaly_detector
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
