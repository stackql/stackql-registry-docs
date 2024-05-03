---
title: event_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - event_subscription
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

Gets or operates on an individual <code>event_subscription</code> resource, use <code>event_subscriptions</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The `AWS::Redshift::EventSubscription` resource creates an Amazon Redshift Event Subscription.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.event_subscription" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="subscription_name" /></td><td><code>string</code></td><td>The name of the Amazon Redshift event notification subscription</td></tr>
<tr><td><CopyableCode code="sns_topic_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications.</td></tr>
<tr><td><CopyableCode code="source_type" /></td><td><code>string</code></td><td>The type of source that will be generating the events.</td></tr>
<tr><td><CopyableCode code="source_ids" /></td><td><code>array</code></td><td>A list of one or more identifiers of Amazon Redshift source objects.</td></tr>
<tr><td><CopyableCode code="event_categories" /></td><td><code>array</code></td><td>Specifies the Amazon Redshift event categories to be published by the event notification subscription.</td></tr>
<tr><td><CopyableCode code="severity" /></td><td><code>string</code></td><td>Specifies the Amazon Redshift event severity to be published by the event notification subscription.</td></tr>
<tr><td><CopyableCode code="enabled" /></td><td><code>boolean</code></td><td>A boolean value; set to true to activate the subscription, and set to false to create the subscription but not activate it.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="customer_aws_id" /></td><td><code>string</code></td><td>The AWS account associated with the Amazon Redshift event notification subscription.</td></tr>
<tr><td><CopyableCode code="cust_subscription_id" /></td><td><code>string</code></td><td>The name of the Amazon Redshift event notification subscription.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the Amazon Redshift event notification subscription.</td></tr>
<tr><td><CopyableCode code="subscription_creation_time" /></td><td><code>string</code></td><td>The date and time the Amazon Redshift event notification subscription was created.</td></tr>
<tr><td><CopyableCode code="source_ids_list" /></td><td><code>array</code></td><td>A list of the sources that publish events to the Amazon Redshift event notification subscription.</td></tr>
<tr><td><CopyableCode code="event_categories_list" /></td><td><code>array</code></td><td>The list of Amazon Redshift event categories specified in the event notification subscription.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
subscription_name,
sns_topic_arn,
source_type,
source_ids,
event_categories,
severity,
enabled,
tags,
customer_aws_id,
cust_subscription_id,
status,
subscription_creation_time,
source_ids_list,
event_categories_list
FROM aws.redshift.event_subscription
WHERE data__Identifier = '<SubscriptionName>';
```

## Permissions

To operate on the <code>event_subscription</code> resource, the following permissions are required:

### Read
```json
redshift:DescribeEventSubscriptions,
redshift:DescribeTags
```

### Update
```json
redshift:ModifyEventSubscription,
redshift:CreateTags,
redshift:DescribeTags,
redshift:DescribeEventSubscriptions,
redshift:DeleteTags
```

### Delete
```json
redshift:DescribeEventSubscriptions,
redshift:DeleteEventSubscription,
redshift:DescribeTags,
redshift:DeleteTags
```

