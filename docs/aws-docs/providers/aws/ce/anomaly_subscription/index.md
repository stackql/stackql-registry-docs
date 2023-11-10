---
title: anomaly_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - anomaly_subscription
  - ce
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>anomaly_subscription</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anomaly_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>anomaly_subscription</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ce.anomaly_subscription</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>subscription_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subscription_name</code></td><td><code>string</code></td><td>The name of the subscription.</td></tr>
<tr><td><code>account_id</code></td><td><code>string</code></td><td>The accountId</td></tr>
<tr><td><code>monitor_arn_list</code></td><td><code>array</code></td><td>A list of cost anomaly monitors.</td></tr>
<tr><td><code>subscribers</code></td><td><code>array</code></td><td>A list of subscriber</td></tr>
<tr><td><code>threshold</code></td><td><code>number</code></td><td>The dollar value that triggers a notification if the threshold is exceeded. </td></tr>
<tr><td><code>threshold_expression</code></td><td><code>string</code></td><td>An Expression object in JSON String format used to specify the anomalies that you want to generate alerts for.</td></tr>
<tr><td><code>frequency</code></td><td><code>string</code></td><td>The frequency at which anomaly reports are sent over email. </td></tr>
<tr><td><code>resource_tags</code></td><td><code>array</code></td><td>Tags to assign to subscription.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
subscription_arn,
subscription_name,
account_id,
monitor_arn_list,
subscribers,
threshold,
threshold_expression,
frequency,
resource_tags
FROM aws.ce.anomaly_subscription
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;SubscriptionArn&gt;'
```
