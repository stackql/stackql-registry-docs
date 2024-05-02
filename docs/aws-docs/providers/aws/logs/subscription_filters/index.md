---
title: subscription_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_filters
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
Retrieves a list of <code>subscription_filters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscription_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::Logs::SubscriptionFilter`` resource specifies a subscription filter and associates it with the specified log group. Subscription filters allow you to subscribe to a real-time stream of log events and have them delivered to a specific destination. Currently, the supported destinations are:&lt;br&#x2F;&gt;  +  An Amazon Kinesis data stream belonging to the same account as the subscription filter, for same-account delivery.&lt;br&#x2F;&gt;  +  A logical destination that belongs to a different account, for cross-account delivery.&lt;br&#x2F;&gt;  +  An Amazon Kinesis Firehose delivery stream that belongs to the same account as the subscription filter, for same-account delivery.&lt;br&#x2F;&gt;  +  An LAMlong function that belongs to the same account as the subscription filter, for same-account delivery.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; There can be as many as two subscription filters associated with a log group.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.logs.subscription_filters</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>filter_name</code></td><td><code>string</code></td><td>The name of the subscription filter.</td></tr>
<tr><td><code>log_group_name</code></td><td><code>string</code></td><td>The log group to associate with the subscription filter. All log events that are uploaded to this log group are filtered and delivered to the specified AWS resource if the filter pattern matches the log events.</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
filter_name,
log_group_name
FROM aws.logs.subscription_filters
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>subscription_filters</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
logs:PutSubscriptionFilter,
logs:DescribeSubscriptionFilters
```

### List
```json
logs:DescribeSubscriptionFilters
```

