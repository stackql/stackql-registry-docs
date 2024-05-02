---
title: subscription_filter
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_filter
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
Gets or operates on an individual <code>subscription_filter</code> resource, use <code>subscription_filters</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscription_filter</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::Logs::SubscriptionFilter`` resource specifies a subscription filter and associates it with the specified log group. Subscription filters allow you to subscribe to a real-time stream of log events and have them delivered to a specific destination. Currently, the supported destinations are:&lt;br&#x2F;&gt;  +  An Amazon Kinesis data stream belonging to the same account as the subscription filter, for same-account delivery.&lt;br&#x2F;&gt;  +  A logical destination that belongs to a different account, for cross-account delivery.&lt;br&#x2F;&gt;  +  An Amazon Kinesis Firehose delivery stream that belongs to the same account as the subscription filter, for same-account delivery.&lt;br&#x2F;&gt;  +  An LAMlong function that belongs to the same account as the subscription filter, for same-account delivery.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; There can be as many as two subscription filters associated with a log group.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.logs.subscription_filter</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>filter_name</code></td><td><code>string</code></td><td>The name of the subscription filter.</td></tr>
<tr><td><code>destination_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the destination.</td></tr>
<tr><td><code>filter_pattern</code></td><td><code>string</code></td><td>The filtering expressions that restrict what gets delivered to the destination AWS resource. For more information about the filter pattern syntax, see &#91;Filter and Pattern Syntax&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonCloudWatch&#x2F;latest&#x2F;logs&#x2F;FilterAndPatternSyntax.html).</td></tr>
<tr><td><code>log_group_name</code></td><td><code>string</code></td><td>The log group to associate with the subscription filter. All log events that are uploaded to this log group are filtered and delivered to the specified AWS resource if the filter pattern matches the log events.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>The ARN of an IAM role that grants CWL permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.</td></tr>
<tr><td><code>distribution</code></td><td><code>string</code></td><td>The method used to distribute log data to the destination, which can be either random or grouped by log stream.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
filter_name,
destination_arn,
filter_pattern,
log_group_name,
role_arn,
distribution
FROM aws.logs.subscription_filter
WHERE data__Identifier = '<FilterName>|<LogGroupName>';
```

## Permissions

To operate on the <code>subscription_filter</code> resource, the following permissions are required:

### Read
```json
logs:DescribeSubscriptionFilters
```

### Update
```json
iam:PassRole,
logs:PutSubscriptionFilter,
logs:DescribeSubscriptionFilters
```

### Delete
```json
logs:DeleteSubscriptionFilter
```

