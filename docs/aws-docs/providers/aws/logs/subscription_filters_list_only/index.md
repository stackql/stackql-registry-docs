---
title: subscription_filters_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_filters_list_only
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>subscription_filters</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/subscription_filters/"><code>subscription_filters</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscription_filters_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::Logs::SubscriptionFilter</code> resource specifies a subscription filter and associates it with the specified log group. Subscription filters allow you to subscribe to a real-time stream of log events and have them delivered to a specific destination. Currently, the supported destinations are:<br />+ An Amazon Kinesis data stream belonging to the same account as the subscription filter, for same-account delivery.<br />+ A logical destination that belongs to a different account, for cross-account delivery.<br />+ An Amazon Kinesis Firehose delivery stream that belongs to the same account as the subscription filter, for same-account delivery.<br />+ An LAMlong function that belongs to the same account as the subscription filter, for same-account delivery.<br /><br />There can be as many as two subscription filters associated with a log group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.subscription_filters_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="filter_name" /></td><td><code>string</code></td><td>The name of the subscription filter.</td></tr>
<tr><td><CopyableCode code="destination_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the destination.</td></tr>
<tr><td><CopyableCode code="filter_pattern" /></td><td><code>string</code></td><td>The filtering expressions that restrict what gets delivered to the destination AWS resource. For more information about the filter pattern syntax, see &#91;Filter and Pattern Syntax&#93;(https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html).</td></tr>
<tr><td><CopyableCode code="log_group_name" /></td><td><code>string</code></td><td>The log group to associate with the subscription filter. All log events that are uploaded to this log group are filtered and delivered to the specified AWS resource if the filter pattern matches the log events.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The ARN of an IAM role that grants CWL permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.</td></tr>
<tr><td><CopyableCode code="distribution" /></td><td><code>string</code></td><td>The method used to distribute log data to the destination, which can be either random or grouped by log stream.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>subscription_filters</code> in a region.
```sql
SELECT
region,
filter_name,
log_group_name
FROM aws.logs.subscription_filters_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>subscription_filters_list_only</code> resource, see <a href="/providers/aws/logs/subscription_filters/#permissions"><code>subscription_filters</code></a>


