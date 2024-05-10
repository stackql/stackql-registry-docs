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


Used to retrieve a list of <code>event_subscriptions</code> in a region or to create or delete a <code>event_subscriptions</code> resource, use <code>event_subscription</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The `AWS::Redshift::EventSubscription` resource creates an Amazon Redshift Event Subscription.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.event_subscriptions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="subscription_name" /></td><td><code>string</code></td><td>The name of the Amazon Redshift event notification subscription</td></tr>
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
FROM aws.redshift.event_subscriptions
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
 "SubscriptionName": "{{ SubscriptionName }}"
}
>>>
--required properties only
INSERT INTO aws.redshift.event_subscriptions (
 SubscriptionName,
 region
)
SELECT 
{{ SubscriptionName }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "SubscriptionName": "{{ SubscriptionName }}",
 "SnsTopicArn": "{{ SnsTopicArn }}",
 "SourceType": "{{ SourceType }}",
 "SourceIds": [
  "{{ SourceIds[0] }}"
 ],
 "EventCategories": [
  "{{ EventCategories[0] }}"
 ],
 "Severity": "{{ Severity }}",
 "Enabled": "{{ Enabled }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.redshift.event_subscriptions (
 SubscriptionName,
 SnsTopicArn,
 SourceType,
 SourceIds,
 EventCategories,
 Severity,
 Enabled,
 Tags,
 region
)
SELECT 
 {{ SubscriptionName }},
 {{ SnsTopicArn }},
 {{ SourceType }},
 {{ SourceIds }},
 {{ EventCategories }},
 {{ Severity }},
 {{ Enabled }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.redshift.event_subscriptions
WHERE data__Identifier = '<SubscriptionName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>event_subscriptions</code> resource, the following permissions are required:

### Create
```json
redshift:CreateEventSubscription,
redshift:CreateTags,
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

### List
```json
redshift:DescribeTags,
redshift:DescribeEventSubscriptions
```

