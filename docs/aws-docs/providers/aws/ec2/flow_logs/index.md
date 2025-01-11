---
title: flow_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_logs
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

Creates, updates, deletes or gets a <code>flow_log</code> resource or lists <code>flow_logs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a VPC flow log, which enables you to capture IP traffic for a specific network interface, subnet, or VPC.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.flow_logs" /></td></tr>
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
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags to apply to the flow logs.</td></tr>
<tr><td><CopyableCode code="traffic_type" /></td><td><code>string</code></td><td>The type of traffic to log. You can log traffic that the resource accepts or rejects, or all traffic.</td></tr>
<tr><td><CopyableCode code="destination_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html"><code>AWS::EC2::FlowLog</code></a>.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="ResourceType, ResourceId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>flow_logs</code> in a region.
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
tags,
traffic_type,
destination_options
FROM aws.ec2.flow_logs
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>flow_log</code>.
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
tags,
traffic_type,
destination_options
FROM aws.ec2.flow_logs
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>flow_log</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.ec2.flow_logs (
 ResourceId,
 ResourceType,
 region
)
SELECT 
'{{ ResourceId }}',
 '{{ ResourceType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.flow_logs (
 DeliverCrossAccountRole,
 DeliverLogsPermissionArn,
 LogDestination,
 LogDestinationType,
 LogFormat,
 LogGroupName,
 MaxAggregationInterval,
 ResourceId,
 ResourceType,
 Tags,
 TrafficType,
 DestinationOptions,
 region
)
SELECT 
 '{{ DeliverCrossAccountRole }}',
 '{{ DeliverLogsPermissionArn }}',
 '{{ LogDestination }}',
 '{{ LogDestinationType }}',
 '{{ LogFormat }}',
 '{{ LogGroupName }}',
 '{{ MaxAggregationInterval }}',
 '{{ ResourceId }}',
 '{{ ResourceType }}',
 '{{ Tags }}',
 '{{ TrafficType }}',
 '{{ DestinationOptions }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: flow_log
    props:
      - name: DeliverCrossAccountRole
        value: '{{ DeliverCrossAccountRole }}'
      - name: DeliverLogsPermissionArn
        value: '{{ DeliverLogsPermissionArn }}'
      - name: LogDestination
        value: '{{ LogDestination }}'
      - name: LogDestinationType
        value: '{{ LogDestinationType }}'
      - name: LogFormat
        value: '{{ LogFormat }}'
      - name: LogGroupName
        value: '{{ LogGroupName }}'
      - name: MaxAggregationInterval
        value: '{{ MaxAggregationInterval }}'
      - name: ResourceId
        value: '{{ ResourceId }}'
      - name: ResourceType
        value: '{{ ResourceType }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: TrafficType
        value: '{{ TrafficType }}'
      - name: DestinationOptions
        value:
          FileFormat: '{{ FileFormat }}'
          HiveCompatiblePartitions: '{{ HiveCompatiblePartitions }}'
          PerHourPartition: '{{ PerHourPartition }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.flow_logs
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>flow_logs</code> resource, the following permissions are required:

### Create
```json
ec2:CreateFlowLogs,
ec2:DescribeFlowLogs,
ec2:CreateTags,
iam:PassRole,
logs:CreateLogDelivery,
s3:GetBucketPolicy,
s3:PutBucketPolicy
```

### Read
```json
ec2:DescribeFlowLogs
```

### Update
```json
ec2:CreateTags,
ec2:DeleteTags,
ec2:DescribeFlowLogs
```

### Delete
```json
ec2:DeleteFlowLogs,
ec2:DescribeFlowLogs,
logs:DeleteLogDelivery
```

### List
```json
ec2:DescribeFlowLogs
```
