---
title: event_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - event_subscriptions
  - rds
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


Used to retrieve a list of <code>event_subscriptions</code> in a region or to create or delete a <code>event_subscriptions</code> resource, use <code>event_subscription</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::RDS::EventSubscription resource allows you to receive notifications for Amazon Relational Database Service events through the Amazon Simple Notification Service (Amazon SNS). For more information, see Using Amazon RDS Event Notification in the Amazon RDS User Guide.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.event_subscriptions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="subscription_name" /></td><td><code>string</code></td><td>The name of the subscription.</td></tr>
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
subscription_name
FROM aws.rds.event_subscriptions
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>event_subscription</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- event_subscription.iql (required properties only)
INSERT INTO aws.rds.event_subscriptions (
 SnsTopicArn,
 region
)
SELECT 
'{{ SnsTopicArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- event_subscription.iql (all properties)
INSERT INTO aws.rds.event_subscriptions (
 Tags,
 SubscriptionName,
 Enabled,
 EventCategories,
 SnsTopicArn,
 SourceIds,
 SourceType,
 region
)
SELECT 
 '{{ Tags }}',
 '{{ SubscriptionName }}',
 '{{ Enabled }}',
 '{{ EventCategories }}',
 '{{ SnsTopicArn }}',
 '{{ SourceIds }}',
 '{{ SourceType }}',
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
  - name: event_subscription
    props:
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: SubscriptionName
        value: '{{ SubscriptionName }}'
      - name: Enabled
        value: '{{ Enabled }}'
      - name: EventCategories
        value:
          - '{{ EventCategories[0] }}'
      - name: SnsTopicArn
        value: '{{ SnsTopicArn }}'
      - name: SourceIds
        value:
          - '{{ SourceIds[0] }}'
      - name: SourceType
        value: '{{ SourceType }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.rds.event_subscriptions
WHERE data__Identifier = '<SubscriptionName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>event_subscriptions</code> resource, the following permissions are required:

### Create
```json
iam:CreateServiceLinkedRole,
rds:CreateEventSubscription,
rds:DescribeEventSubscriptions,
rds:ListTagsForResource,
rds:AddTagsToResource,
rds:RemoveTagsFromResource
```

### Delete
```json
rds:DeleteEventSubscription,
rds:DescribeEventSubscriptions
```

### List
```json
rds:DescribeEventSubscriptions
```

