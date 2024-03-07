---
title: destination
hide_title: false
hide_table_of_contents: false
keywords:
  - destination
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
Gets an individual <code>destination</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>destination</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>destination</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.logs.destination</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>destination_name</code></td><td><code>string</code></td><td>The name of the destination resource</td></tr>
<tr><td><code>destination_policy</code></td><td><code>string</code></td><td>An IAM policy document that governs which AWS accounts can create subscription filters against this destination.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>The ARN of an IAM role that permits CloudWatch Logs to send data to the specified AWS resource</td></tr>
<tr><td><code>target_arn</code></td><td><code>string</code></td><td>The ARN of the physical target where the log events are delivered (for example, a Kinesis stream)</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>destination</code> resource, the following permissions are required:

### Read
<pre>
logs:DescribeDestinations</pre>

### Update
<pre>
logs:PutDestination,
logs:PutDestinationPolicy,
logs:DescribeDestinations,
iam:PassRole</pre>

### Delete
<pre>
logs:DeleteDestination</pre>


## Example
```sql
SELECT
region,
arn,
destination_name,
destination_policy,
role_arn,
target_arn
FROM awscc.logs.destination
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DestinationName&gt;'
```
