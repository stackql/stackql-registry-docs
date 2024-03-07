---
title: delivery_destination
hide_title: false
hide_table_of_contents: false
keywords:
  - delivery_destination
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
Gets an individual <code>delivery_destination</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delivery_destination</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>delivery_destination</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.logs.delivery_destination</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of this delivery destination.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) that uniquely identifies this delivery destination.</td></tr>
<tr><td><code>destination_resource_arn</code></td><td><code>string</code></td><td>The ARN of the AWS resource that will receive the logs.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags that have been assigned to this delivery destination.</td></tr>
<tr><td><code>delivery_destination_type</code></td><td><code>string</code></td><td>Displays whether this delivery destination is CloudWatch Logs, Amazon S3, or Kinesis Data Firehose.</td></tr>
<tr><td><code>delivery_destination_policy</code></td><td><code>object</code></td><td>IAM policy that grants permissions to CloudWatch Logs to deliver logs cross-account to a specified destination in this account.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;The policy must be in JSON string format.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;Length Constraints: Maximum length of 51200</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>delivery_destination</code> resource, the following permissions are required:

### Read
<pre>
logs:GetDeliveryDestination,
logs:ListTagsForResource,
logs:GetDeliveryDestinationPolicy</pre>

### Update
<pre>
logs:PutDeliveryDestination,
logs:GetDeliveryDestination,
logs:ListTagsForResource,
logs:TagResource,
logs:UntagResource,
logs:DeleteDeliveryDestinationPolicy,
logs:PutDeliveryDestinationPolicy,
logs:GetDeliveryDestinationPolicy</pre>

### Delete
<pre>
logs:DeleteDeliveryDestination,
logs:DeleteDeliveryDestinationPolicy</pre>


## Example
```sql
SELECT
region,
name,
arn,
destination_resource_arn,
tags,
delivery_destination_type,
delivery_destination_policy
FROM awscc.logs.delivery_destination
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Name&gt;'
```
