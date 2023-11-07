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
null
<tr><td><b>Id</b></td><td><code>aws.iot.fleet_metric</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>MetricName</code></td><td><code>string</code></td><td>The name of the fleet metric</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The description of a fleet metric</td></tr>
<tr><td><code>QueryString</code></td><td><code>string</code></td><td>The Fleet Indexing query used by a fleet metric</td></tr>
<tr><td><code>Period</code></td><td><code>integer</code></td><td>The period of metric emission in seconds</td></tr>
<tr><td><code>AggregationField</code></td><td><code>string</code></td><td>The aggregation field to perform aggregation and metric emission</td></tr>
<tr><td><code>QueryVersion</code></td><td><code>string</code></td><td>The version of a Fleet Indexing query used by a fleet metric</td></tr>
<tr><td><code>IndexName</code></td><td><code>string</code></td><td>The index name of a fleet metric</td></tr>
<tr><td><code>Unit</code></td><td><code>string</code></td><td>The unit of data points emitted by a fleet metric</td></tr>
<tr><td><code>AggregationType</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>MetricArn</code></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of a fleet metric metric</td></tr>
<tr><td><code>CreationDate</code></td><td><code>number</code></td><td>The creation date of a fleet metric</td></tr>
<tr><td><code>LastModifiedDate</code></td><td><code>number</code></td><td>The last modified date of a fleet metric</td></tr>
<tr><td><code>Version</code></td><td><code>number</code></td><td>The version of a fleet metric</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iot.fleet_metric
WHERE region = 'us-east-1' AND data__Identifier = '&lt;MetricName&gt;'
</pre>
