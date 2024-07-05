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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>subscription_filter</code> resource or lists <code>subscription_filters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscription_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::Logs::SubscriptionFilter</code> resource specifies a subscription filter and associates it with the specified log group. Subscription filters allow you to subscribe to a real-time stream of log events and have them delivered to a specific destination. Currently, the supported destinations are:<br />+ An Amazon Kinesis data stream belonging to the same account as the subscription filter, for same-account delivery.<br />+ A logical destination that belongs to a different account, for cross-account delivery.<br />+ An Amazon Kinesis Firehose delivery stream that belongs to the same account as the subscription filter, for same-account delivery.<br />+ An LAMlong function that belongs to the same account as the subscription filter, for same-account delivery.<br /><br />There can be as many as two subscription filters associated with a log group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.subscription_filters" /></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="DestinationArn, FilterPattern, LogGroupName, region" /></td>
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
Gets all <code>subscription_filters</code> in a region.
```sql
SELECT
region,
filter_name,
destination_arn,
filter_pattern,
log_group_name,
role_arn,
distribution
FROM aws.logs.subscription_filters
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>subscription_filter</code>.
```sql
SELECT
region,
filter_name,
destination_arn,
filter_pattern,
log_group_name,
role_arn,
distribution
FROM aws.logs.subscription_filters
WHERE region = 'us-east-1' AND data__Identifier = '<FilterName>|<LogGroupName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>subscription_filter</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.logs.subscription_filters (
 DestinationArn,
 FilterPattern,
 LogGroupName,
 region
)
SELECT 
'{{ DestinationArn }}',
 '{{ FilterPattern }}',
 '{{ LogGroupName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.logs.subscription_filters (
 FilterName,
 DestinationArn,
 FilterPattern,
 LogGroupName,
 RoleArn,
 Distribution,
 region
)
SELECT 
 '{{ FilterName }}',
 '{{ DestinationArn }}',
 '{{ FilterPattern }}',
 '{{ LogGroupName }}',
 '{{ RoleArn }}',
 '{{ Distribution }}',
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
  - name: subscription_filter
    props:
      - name: FilterName
        value: '{{ FilterName }}'
      - name: DestinationArn
        value: '{{ DestinationArn }}'
      - name: FilterPattern
        value: '{{ FilterPattern }}'
      - name: LogGroupName
        value: '{{ LogGroupName }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Distribution
        value: '{{ Distribution }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.logs.subscription_filters
WHERE data__Identifier = '<FilterName|LogGroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>subscription_filters</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
logs:PutSubscriptionFilter,
logs:DescribeSubscriptionFilters
```

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

### List
```json
logs:DescribeSubscriptionFilters
```

