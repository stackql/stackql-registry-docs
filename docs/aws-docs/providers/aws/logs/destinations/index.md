---
title: destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - destinations
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
Retrieves a list of <code>destinations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>destinations</td></tr>
<tr><td><b>Id</b></td><td><code>aws.logs.destinations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DestinationName</code></td><td><code>string</code></td><td>The name of the destination resource</td></tr>
<tr><td><code>DestinationPolicy</code></td><td><code>string</code></td><td>An IAM policy document that governs which AWS accounts can create subscription filters against this destination.</td></tr>
<tr><td><code>RoleArn</code></td><td><code>string</code></td><td>The ARN of an IAM role that permits CloudWatch Logs to send data to the specified AWS resource</td></tr>
<tr><td><code>TargetArn</code></td><td><code>string</code></td><td>The ARN of the physical target where the log events are delivered (for example, a Kinesis stream)</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.logs.destinations
WHERE region = 'us-east-1'
</pre>
