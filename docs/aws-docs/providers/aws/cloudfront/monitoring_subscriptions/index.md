---
title: monitoring_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - monitoring_subscriptions
  - cloudfront
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


Used to retrieve a list of <code>monitoring_subscriptions</code> in a region or to create or delete a <code>monitoring_subscriptions</code> resource, use <code>monitoring_subscription</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitoring_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CloudFront::MonitoringSubscription</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.monitoring_subscriptions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="distribution_id" /></td><td><code>string</code></td><td></td></tr>
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
distribution_id
FROM aws.cloudfront.monitoring_subscriptions
;
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>monitoring_subscription</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- monitoring_subscription.iql (required properties only)
INSERT INTO aws.cloudfront.monitoring_subscriptions (
 DistributionId,
 MonitoringSubscription,
 region
)
SELECT 
'{{ DistributionId }}',
 '{{ MonitoringSubscription }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- monitoring_subscription.iql (all properties)
INSERT INTO aws.cloudfront.monitoring_subscriptions (
 DistributionId,
 MonitoringSubscription,
 region
)
SELECT 
 '{{ DistributionId }}',
 '{{ MonitoringSubscription }}',
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
  - name: monitoring_subscription
    props:
      - name: DistributionId
        value: '{{ DistributionId }}'
      - name: MonitoringSubscription
        value:
          DistributionId: '{{ DistributionId }}'
          MonitoringSubscription: null

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cloudfront.monitoring_subscriptions
WHERE data__Identifier = '<DistributionId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>monitoring_subscriptions</code> resource, the following permissions are required:

### Create
```json
cloudfront:CreateMonitoringSubscription
```

### Delete
```json
cloudfront:DeleteMonitoringSubscription
```

