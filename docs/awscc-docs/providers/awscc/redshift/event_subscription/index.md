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
Gets an individual <code>event_subscription</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>event_subscription</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.redshift.event_subscription</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>subscription_name</code></td><td><code>string</code></td><td>The name of the Amazon Redshift event notification subscription</td></tr>
<tr><td><code>sns_topic_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications.</td></tr>
<tr><td><code>source_type</code></td><td><code>string</code></td><td>The type of source that will be generating the events.</td></tr>
<tr><td><code>source_ids</code></td><td><code>array</code></td><td>A list of one or more identifiers of Amazon Redshift source objects.</td></tr>
<tr><td><code>event_categories</code></td><td><code>array</code></td><td>Specifies the Amazon Redshift event categories to be published by the event notification subscription.</td></tr>
<tr><td><code>severity</code></td><td><code>string</code></td><td>Specifies the Amazon Redshift event severity to be published by the event notification subscription.</td></tr>
<tr><td><code>enabled</code></td><td><code>boolean</code></td><td>A boolean value; set to true to activate the subscription, and set to false to create the subscription but not activate it.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>customer_aws_id</code></td><td><code>string</code></td><td>The AWS account associated with the Amazon Redshift event notification subscription.</td></tr>
<tr><td><code>cust_subscription_id</code></td><td><code>string</code></td><td>The name of the Amazon Redshift event notification subscription.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the Amazon Redshift event notification subscription.</td></tr>
<tr><td><code>subscription_creation_time</code></td><td><code>string</code></td><td>The date and time the Amazon Redshift event notification subscription was created.</td></tr>
<tr><td><code>source_ids_list</code></td><td><code>array</code></td><td>A list of the sources that publish events to the Amazon Redshift event notification subscription.</td></tr>
<tr><td><code>event_categories_list</code></td><td><code>array</code></td><td>The list of Amazon Redshift event categories specified in the event notification subscription.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>event_subscription</code> resource, the following permissions are required:

### Read
<pre>
redshift:DescribeEventSubscriptions,
redshift:DescribeTags</pre>

### Update
<pre>
redshift:ModifyEventSubscription,
redshift:CreateTags,
redshift:DescribeTags,
redshift:DescribeEventSubscriptions,
redshift:DeleteTags</pre>

### Delete
<pre>
redshift:DescribeEventSubscriptions,
redshift:DeleteEventSubscription,
redshift:DescribeTags,
redshift:DeleteTags</pre>


## Example
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
FROM awscc.redshift.event_subscription
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;SubscriptionName&gt;'
```
