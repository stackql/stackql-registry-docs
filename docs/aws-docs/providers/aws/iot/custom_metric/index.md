---
title: custom_metric
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_metric
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
Gets an individual <code>custom_metric</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_metric</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.custom_metric</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>MetricName</code></td><td><code>string</code></td><td>The name of the custom metric. This will be used in the metric report submitted from the device/thing. Shouldn't begin with aws: . Cannot be updated once defined.</td></tr><tr><td><code>DisplayName</code></td><td><code>string</code></td><td>Field represents a friendly name in the console for the custom metric; it doesn't have to be unique. Don't use this name as the metric identifier in the device metric report. Can be updated once defined.</td></tr><tr><td><code>MetricType</code></td><td><code>string</code></td><td>The type of the custom metric. Types include string-list, ip-address-list, number-list, and number.</td></tr><tr><td><code>MetricArn</code></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of the custom metric.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iot.custom_metric
WHERE region = 'us-east-1' AND data__Identifier = '{MetricName}'
</pre>
