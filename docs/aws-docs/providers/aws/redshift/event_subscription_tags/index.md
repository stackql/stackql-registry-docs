---
title: event_subscription_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - event_subscription_tags
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

Expands all tag keys and values for <code>event_subscriptions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_subscription_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The `AWS::Redshift::EventSubscription` resource creates an Amazon Redshift Event Subscription.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.event_subscription_tags" /></td></tr>
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
Expands tags for all <code>event_subscriptions</code> in a region.
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
tag_key,
tag_value
FROM aws.redshift.event_subscription_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>event_subscription_tags</code> resource, see <a href="/providers/aws/redshift/event_subscriptions/#permissions"><code>event_subscriptions</code></a>


