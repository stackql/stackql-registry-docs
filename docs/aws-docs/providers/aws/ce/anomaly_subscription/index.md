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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>anomaly_subscription</code> resource, use <code>anomaly_subscriptions</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anomaly_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Cost Anomaly Detection leverages advanced Machine Learning technologies to identify anomalous spend and root causes, so you can quickly take action. Create subscription to be notified</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ce.anomaly_subscription" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="subscription_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subscription_name" /></td><td><code>string</code></td><td>The name of the subscription.</td></tr>
<tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>The accountId</td></tr>
<tr><td><CopyableCode code="monitor_arn_list" /></td><td><code>array</code></td><td>A list of cost anomaly monitors.</td></tr>
<tr><td><CopyableCode code="subscribers" /></td><td><code>array</code></td><td>A list of subscriber</td></tr>
<tr><td><CopyableCode code="threshold" /></td><td><code>number</code></td><td>The dollar value that triggers a notification if the threshold is exceeded. </td></tr>
<tr><td><CopyableCode code="threshold_expression" /></td><td><code>string</code></td><td>An Expression object in JSON String format used to specify the anomalies that you want to generate alerts for.</td></tr>
<tr><td><CopyableCode code="frequency" /></td><td><code>string</code></td><td>The frequency at which anomaly reports are sent over email. </td></tr>
<tr><td><CopyableCode code="resource_tags" /></td><td><code>array</code></td><td>Tags to assign to subscription.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
WHERE region = 'us-east-1' AND data__Identifier = '<SubscriptionArn>';
```


## Permissions

To operate on the <code>anomaly_subscription</code> resource, the following permissions are required:

### Read
```json
ce:GetAnomalySubscriptions
```

### Update
```json
ce:UpdateAnomalySubscription
```

