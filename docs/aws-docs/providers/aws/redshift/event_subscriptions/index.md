---
title: event_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - event_subscriptions
  - redshift
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

Creates, updates, deletes or gets an <code>event_subscription</code> resource or lists <code>event_subscriptions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The `AWS::Redshift::EventSubscription` resource creates an Amazon Redshift Event Subscription.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.event_subscriptions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the Amazon Redshift event notification subscription.</td></tr>
<tr><td><CopyableCode code="cust_subscription_id" /></td><td><code>string</code></td><td>The name of the Amazon Redshift event notification subscription.</td></tr>
<tr><td><CopyableCode code="event_categories_list" /></td><td><code>array</code></td><td>The list of Amazon Redshift event categories specified in the event notification subscription.</td></tr>
<tr><td><CopyableCode code="source_type" /></td><td><code>string</code></td><td>The type of source that will be generating the events.</td></tr>
<tr><td><CopyableCode code="event_categories" /></td><td><code>array</code></td><td>Specifies the Amazon Redshift event categories to be published by the event notification subscription.</td></tr>
<tr><td><CopyableCode code="enabled" /></td><td><code>boolean</code></td><td>A boolean value; set to true to activate the subscription, and set to false to create the subscription but not activate it.</td></tr>
<tr><td><CopyableCode code="severity" /></td><td><code>string</code></td><td>Specifies the Amazon Redshift event severity to be published by the event notification subscription.</td></tr>
<tr><td><CopyableCode code="subscription_name" /></td><td><code>string</code></td><td>The name of the Amazon Redshift event notification subscription</td></tr>
<tr><td><CopyableCode code="source_ids" /></td><td><code>array</code></td><td>A list of one or more identifiers of Amazon Redshift source objects.</td></tr>
<tr><td><CopyableCode code="customer_aws_id" /></td><td><code>string</code></td><td>The AWS account associated with the Amazon Redshift event notification subscription.</td></tr>
<tr><td><CopyableCode code="source_ids_list" /></td><td><code>array</code></td><td>A list of the sources that publish events to the Amazon Redshift event notification subscription.</td></tr>
<tr><td><CopyableCode code="sns_topic_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications.</td></tr>
<tr><td><CopyableCode code="subscription_creation_time" /></td><td><code>string</code></td><td>The date and time the Amazon Redshift event notification subscription was created.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="SubscriptionName, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>event_subscriptions</code> in a region.
```sql
SELECT
region,
subscription_name
FROM aws.redshift.event_subscriptions
WHERE region = 'us-east-1';
```
Gets all properties from an <code>event_subscription</code>.
```sql
SELECT
region,
status,
cust_subscription_id,
event_categories_list,
source_type,
event_categories,
enabled,
severity,
subscription_name,
source_ids,
customer_aws_id,
source_ids_list,
sns_topic_arn,
subscription_creation_time,
tags
FROM aws.redshift.event_subscriptions
WHERE region = 'us-east-1' AND data__Identifier = '<SubscriptionName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>event_subscription</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.redshift.event_subscriptions (
 SubscriptionName,
 region
)
SELECT 
'{{ SubscriptionName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.redshift.event_subscriptions (
 SourceType,
 EventCategories,
 Enabled,
 Severity,
 SubscriptionName,
 SourceIds,
 SnsTopicArn,
 Tags,
 region
)
SELECT 
 '{{ SourceType }}',
 '{{ EventCategories }}',
 '{{ Enabled }}',
 '{{ Severity }}',
 '{{ SubscriptionName }}',
 '{{ SourceIds }}',
 '{{ SnsTopicArn }}',
 '{{ Tags }}',
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
      - name: SourceType
        value: '{{ SourceType }}'
      - name: EventCategories
        value:
          - '{{ EventCategories[0] }}'
      - name: Enabled
        value: '{{ Enabled }}'
      - name: Severity
        value: '{{ Severity }}'
      - name: SubscriptionName
        value: '{{ SubscriptionName }}'
      - name: SourceIds
        value:
          - '{{ SourceIds[0] }}'
      - name: SnsTopicArn
        value: '{{ SnsTopicArn }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.redshift.event_subscriptions
WHERE data__Identifier = '<SubscriptionName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>event_subscriptions</code> resource, the following permissions are required:

### Read
```json
redshift:DescribeEventSubscriptions,
redshift:DescribeTags
```

### Create
```json
redshift:CreateEventSubscription,
redshift:CreateTags,
redshift:DescribeTags,
redshift:DescribeEventSubscriptions
```

### Update
```json
redshift:ModifyEventSubscription,
redshift:CreateTags,
redshift:DescribeTags,
redshift:DescribeEventSubscriptions,
redshift:DeleteTags
```

### List
```json
redshift:DescribeTags,
redshift:DescribeEventSubscriptions
```

### Delete
```json
redshift:DescribeEventSubscriptions,
redshift:DeleteEventSubscription,
redshift:DescribeTags,
redshift:DeleteTags
```

