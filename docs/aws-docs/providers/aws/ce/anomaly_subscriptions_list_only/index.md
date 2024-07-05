---
title: anomaly_subscriptions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - anomaly_subscriptions_list_only
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

Lists <code>anomaly_subscriptions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/anomaly_subscriptions/"><code>anomaly_subscriptions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anomaly_subscriptions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Cost Anomaly Detection leverages advanced Machine Learning technologies to identify anomalous spend and root causes, so you can quickly take action. Create subscription to be notified</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ce.anomaly_subscriptions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="subscription_arn" /></td><td><code>string</code></td><td>Subscription ARN</td></tr>
<tr><td><CopyableCode code="subscription_name" /></td><td><code>string</code></td><td>The name of the subscription.</td></tr>
<tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>The accountId</td></tr>
<tr><td><CopyableCode code="monitor_arn_list" /></td><td><code>array</code></td><td>A list of cost anomaly monitors.</td></tr>
<tr><td><CopyableCode code="subscribers" /></td><td><code>array</code></td><td>A list of subscriber</td></tr>
<tr><td><CopyableCode code="threshold" /></td><td><code>number</code></td><td>The dollar value that triggers a notification if the threshold is exceeded.</td></tr>
<tr><td><CopyableCode code="threshold_expression" /></td><td><code>string</code></td><td>An Expression object in JSON String format used to specify the anomalies that you want to generate alerts for.</td></tr>
<tr><td><CopyableCode code="frequency" /></td><td><code>string</code></td><td>The frequency at which anomaly reports are sent over email.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>anomaly_subscriptions</code> in a region.
```sql
SELECT
region,
subscription_arn
FROM aws.ce.anomaly_subscriptions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>anomaly_subscriptions_list_only</code> resource, see <a href="/providers/aws/ce/anomaly_subscriptions/#permissions"><code>anomaly_subscriptions</code></a>


