---
title: flow_log_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_log_tags
  - ec2
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

Expands all tag keys and values for <code>flow_logs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_log_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a VPC flow log, which enables you to capture IP traffic for a specific network interface, subnet, or VPC.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.flow_log_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The Flow Log ID</td></tr>
<tr><td><CopyableCode code="deliver_cross_account_role" /></td><td><code>string</code></td><td>The ARN of the IAM role that allows Amazon EC2 to publish flow logs across accounts.</td></tr>
<tr><td><CopyableCode code="deliver_logs_permission_arn" /></td><td><code>string</code></td><td>The ARN for the IAM role that permits Amazon EC2 to publish flow logs to a CloudWatch Logs log group in your account. If you specify LogDestinationType as s3 or kinesis-data-firehose, do not specify DeliverLogsPermissionArn or LogGroupName.</td></tr>
<tr><td><CopyableCode code="log_destination" /></td><td><code>string</code></td><td>Specifies the destination to which the flow log data is to be published. Flow log data can be published to a CloudWatch Logs log group, an Amazon S3 bucket, or a Kinesis Firehose stream. The value specified for this parameter depends on the value specified for LogDestinationType.</td></tr>
<tr><td><CopyableCode code="log_destination_type" /></td><td><code>string</code></td><td>Specifies the type of destination to which the flow log data is to be published. Flow log data can be published to CloudWatch Logs or Amazon S3.</td></tr>
<tr><td><CopyableCode code="log_format" /></td><td><code>string</code></td><td>The fields to include in the flow log record, in the order in which they should appear.</td></tr>
<tr><td><CopyableCode code="log_group_name" /></td><td><code>string</code></td><td>The name of a new or existing CloudWatch Logs log group where Amazon EC2 publishes your flow logs. If you specify LogDestinationType as s3 or kinesis-data-firehose, do not specify DeliverLogsPermissionArn or LogGroupName.</td></tr>
<tr><td><CopyableCode code="max_aggregation_interval" /></td><td><code>integer</code></td><td>The maximum interval of time during which a flow of packets is captured and aggregated into a flow log record. You can specify 60 seconds (1 minute) or 600 seconds (10 minutes).</td></tr>
<tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td>The ID of the subnet, network interface, or VPC for which you want to create a flow log.</td></tr>
<tr><td><CopyableCode code="resource_type" /></td><td><code>string</code></td><td>The type of resource for which to create the flow log. For example, if you specified a VPC ID for the ResourceId property, specify VPC for this property.</td></tr>
<tr><td><CopyableCode code="traffic_type" /></td><td><code>string</code></td><td>The type of traffic to log. You can log traffic that the resource accepts or rejects, or all traffic.</td></tr>
<tr><td><CopyableCode code="destination_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>flow_logs</code> in a region.
```sql
SELECT
region,
id,
deliver_cross_account_role,
deliver_logs_permission_arn,
log_destination,
log_destination_type,
log_format,
log_group_name,
max_aggregation_interval,
resource_id,
resource_type,
traffic_type,
destination_options,
tag_key,
tag_value
FROM aws.ec2.flow_log_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>flow_log_tags</code> resource, see <a href="/providers/aws/ec2/flow_logs/#permissions"><code>flow_logs</code></a>

