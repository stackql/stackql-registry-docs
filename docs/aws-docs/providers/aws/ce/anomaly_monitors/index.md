---
title: anomaly_monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - anomaly_monitors
  - ce
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>anomaly_monitors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anomaly_monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.ce.anomaly_monitors</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>MonitorArn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>MonitorType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>MonitorName</code></td><td><code>string</code></td><td>The name of the monitor.</td></tr><tr><td><code>CreationDate</code></td><td><code>string</code></td><td>The date when the monitor was created. </td></tr><tr><td><code>LastEvaluatedDate</code></td><td><code>string</code></td><td>The date when the monitor last evaluated for anomalies.</td></tr><tr><td><code>LastUpdatedDate</code></td><td><code>string</code></td><td>The date when the monitor was last updated.</td></tr><tr><td><code>MonitorDimension</code></td><td><code>string</code></td><td>The dimensions to evaluate</td></tr><tr><td><code>MonitorSpecification</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DimensionalValueCount</code></td><td><code>integer</code></td><td>The value for evaluated dimensions.</td></tr><tr><td><code>ResourceTags</code></td><td><code>array</code></td><td>Tags to assign to monitor.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.ce.anomaly_monitors
WHERE region = 'us-east-1'
</pre>
