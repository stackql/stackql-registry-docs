---
title: anomaly_detectors
hide_title: false
hide_table_of_contents: false
keywords:
  - anomaly_detectors
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
Retrieves a list of <code>anomaly_detectors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anomaly_detectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>anomaly_detectors</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudwatch.anomaly_detectors</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>MetricName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Stat</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>MetricMathAnomalyDetector</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Dimensions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Namespace</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SingleMetricAnomalyDetector</code></td><td><code>object</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.cloudwatch.anomaly_detectors<br/>WHERE region = 'us-east-1'
</pre>
