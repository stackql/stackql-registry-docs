---
title: anomaly_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - anomaly_subscriptions
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

Creates, updates, deletes or gets an <code>anomaly_subscription</code> resource or lists <code>anomaly_subscriptions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anomaly_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Cost Anomaly Detection leverages advanced Machine Learning technologies to identify anomalous spend and root causes, so you can quickly take action. Create subscription to be notified</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ce.anomaly_subscriptions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="subscription_arn" /></td><td><code>Subscription ARN</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="MonitorArnList, Subscribers, Frequency, SubscriptionName, region" /></td>
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
List all <code>anomaly_subscriptions</code> in a region.
```sql
SELECT
region,
subscription_arn
FROM aws.ce.anomaly_subscriptions
WHERE region = 'us-east-1';
```
Gets all properties from an <code>anomaly_subscription</code>.
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
FROM aws.ce.anomaly_subscriptions
WHERE region = 'us-east-1' AND data__Identifier = '<SubscriptionArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>anomaly_subscription</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ce.anomaly_subscriptions (
 SubscriptionName,
 MonitorArnList,
 Subscribers,
 Frequency,
 region
)
SELECT 
'{{ SubscriptionName }}',
 '{{ MonitorArnList }}',
 '{{ Subscribers }}',
 '{{ Frequency }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ce.anomaly_subscriptions (
 SubscriptionName,
 MonitorArnList,
 Subscribers,
 Threshold,
 ThresholdExpression,
 Frequency,
 ResourceTags,
 region
)
SELECT 
 '{{ SubscriptionName }}',
 '{{ MonitorArnList }}',
 '{{ Subscribers }}',
 '{{ Threshold }}',
 '{{ ThresholdExpression }}',
 '{{ Frequency }}',
 '{{ ResourceTags }}',
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
  - name: anomaly_subscription
    props:
      - name: SubscriptionName
        value: '{{ SubscriptionName }}'
      - name: MonitorArnList
        value:
          - '{{ MonitorArnList[0] }}'
      - name: Subscribers
        value:
          - Address: '{{ Address }}'
            Status: '{{ Status }}'
            Type: '{{ Type }}'
      - name: Threshold
        value: null
      - name: ThresholdExpression
        value: '{{ ThresholdExpression }}'
      - name: Frequency
        value: '{{ Frequency }}'
      - name: ResourceTags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ce.anomaly_subscriptions
WHERE data__Identifier = '<SubscriptionArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>anomaly_subscriptions</code> resource, the following permissions are required:

### Create
```json
ce:CreateAnomalySubscription,
ce:TagResource
```

### Read
```json
ce:GetAnomalySubscriptions
```

### Update
```json
ce:UpdateAnomalySubscription
```

### Delete
```json
ce:DeleteAnomalySubscription
```

### List
```json
ce:GetAnomalySubscriptions
```

