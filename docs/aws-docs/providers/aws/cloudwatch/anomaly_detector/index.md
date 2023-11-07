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
null
<tr><td><b>Id</b></td><td><code>aws.cloudwatch.anomaly_detector</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>MetricName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Stat</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Configuration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>MetricMathAnomalyDetector</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Dimensions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Namespace</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SingleMetricAnomalyDetector</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.cloudwatch.anomaly_detector
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Id&gt;'
</pre>
