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
Retrieves a list of <code>event_subscriptions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>event_subscriptions</td></tr>
<tr><td><b>Id</b></td><td><code>aws.redshift.event_subscriptions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>SubscriptionName</code></td><td><code>string</code></td><td>The name of the Amazon Redshift event notification subscription</td></tr>
<tr><td><code>SnsTopicArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications.</td></tr>
<tr><td><code>SourceType</code></td><td><code>string</code></td><td>The type of source that will be generating the events.</td></tr>
<tr><td><code>SourceIds</code></td><td><code>array</code></td><td>A list of one or more identifiers of Amazon Redshift source objects.</td></tr>
<tr><td><code>EventCategories</code></td><td><code>array</code></td><td>Specifies the Amazon Redshift event categories to be published by the event notification subscription.</td></tr>
<tr><td><code>Severity</code></td><td><code>string</code></td><td>Specifies the Amazon Redshift event severity to be published by the event notification subscription.</td></tr>
<tr><td><code>Enabled</code></td><td><code>boolean</code></td><td>A boolean value; set to true to activate the subscription, and set to false to create the subscription but not activate it.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>CustomerAwsId</code></td><td><code>string</code></td><td>The AWS account associated with the Amazon Redshift event notification subscription.</td></tr>
<tr><td><code>CustSubscriptionId</code></td><td><code>string</code></td><td>The name of the Amazon Redshift event notification subscription.</td></tr>
<tr><td><code>Status</code></td><td><code>string</code></td><td>The status of the Amazon Redshift event notification subscription.</td></tr>
<tr><td><code>SubscriptionCreationTime</code></td><td><code>string</code></td><td>The date and time the Amazon Redshift event notification subscription was created.</td></tr>
<tr><td><code>SourceIdsList</code></td><td><code>array</code></td><td>A list of the sources that publish events to the Amazon Redshift event notification subscription.</td></tr>
<tr><td><code>EventCategoriesList</code></td><td><code>array</code></td><td>The list of Amazon Redshift event categories specified in the event notification subscription.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.redshift.event_subscriptions
WHERE region = 'us-east-1'
</pre>
