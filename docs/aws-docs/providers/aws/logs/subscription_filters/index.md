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


Used to retrieve a list of <code>subscription_filters</code> in a region or to create or delete a <code>subscription_filters</code> resource, use <code>subscription_filter</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscription_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::Logs::SubscriptionFilter`` resource specifies a subscription filter and associates it with the specified log group. Subscription filters allow you to subscribe to a real-time stream of log events and have them delivered to a specific destination. Currently, the supported destinations are:&lt;br&#x2F;&gt;  +  An Amazon Kinesis data stream belonging to the same account as the subscription filter, for same-account delivery.&lt;br&#x2F;&gt;  +  A logical destination that belongs to a different account, for cross-account delivery.&lt;br&#x2F;&gt;  +  An Amazon Kinesis Firehose delivery stream that belongs to the same account as the subscription filter, for same-account delivery.&lt;br&#x2F;&gt;  +  An LAMlong function that belongs to the same account as the subscription filter, for same-account delivery.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt; There can be as many as two subscription filters associated with a log group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.subscription_filters" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="filter_name" /></td><td><code>string</code></td><td>The name of the subscription filter.</td></tr>
<tr><td><CopyableCode code="log_group_name" /></td><td><code>string</code></td><td>The log group to associate with the subscription filter. All log events that are uploaded to this log group are filtered and delivered to the specified AWS resource if the filter pattern matches the log events.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
filter_name,
log_group_name
FROM aws.logs.subscription_filters
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "DestinationArn": "{{ DestinationArn }}",
 "FilterPattern": "{{ FilterPattern }}",
 "LogGroupName": "{{ LogGroupName }}"
}
>>>
--required properties only
INSERT INTO aws.logs.subscription_filters (
 DestinationArn,
 FilterPattern,
 LogGroupName,
 region
)
SELECT 
{{ .DestinationArn }},
 {{ .FilterPattern }},
 {{ .LogGroupName }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "FilterName": "{{ FilterName }}",
 "DestinationArn": "{{ DestinationArn }}",
 "FilterPattern": "{{ FilterPattern }}",
 "LogGroupName": "{{ LogGroupName }}",
 "RoleArn": "{{ RoleArn }}",
 "Distribution": "{{ Distribution }}"
}
>>>
--all properties
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
 {{ .FilterName }},
 {{ .DestinationArn }},
 {{ .FilterPattern }},
 {{ .LogGroupName }},
 {{ .RoleArn }},
 {{ .Distribution }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
logs:DeleteSubscriptionFilter
```

### List
```json
logs:DescribeSubscriptionFilters
```

