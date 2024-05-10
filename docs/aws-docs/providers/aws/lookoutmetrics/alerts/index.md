---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - lookoutmetrics
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


Used to retrieve a list of <code>alerts</code> in a region or to create or delete a <code>alerts</code> resource, use <code>alert</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::LookoutMetrics::Alert</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lookoutmetrics.alerts" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>undefined</code></td><td>ARN assigned to the alert.</td></tr>
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
arn
FROM aws.lookoutmetrics.alerts
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>alert</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- alert.iql (required properties only)
INSERT INTO aws.lookoutmetrics.alerts (
 AnomalyDetectorArn,
 AlertSensitivityThreshold,
 Action,
 region
)
SELECT 
'{{ AnomalyDetectorArn }}',
 '{{ AlertSensitivityThreshold }}',
 '{{ Action }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- alert.iql (all properties)
INSERT INTO aws.lookoutmetrics.alerts (
 AlertName,
 AlertDescription,
 AnomalyDetectorArn,
 AlertSensitivityThreshold,
 Action,
 region
)
SELECT 
 '{{ AlertName }}',
 '{{ AlertDescription }}',
 '{{ AnomalyDetectorArn }}',
 '{{ AlertSensitivityThreshold }}',
 '{{ Action }}',
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
  - name: alert
    props:
      - name: AlertName
        value: '{{ AlertName }}'
      - name: AlertDescription
        value: '{{ AlertDescription }}'
      - name: AnomalyDetectorArn
        value: '{{ AnomalyDetectorArn }}'
      - name: AlertSensitivityThreshold
        value: '{{ AlertSensitivityThreshold }}'
      - name: Action
        value:
          SNSConfiguration:
            RoleArn: '{{ RoleArn }}'
            SnsTopicArn: null
          LambdaConfiguration:
            RoleArn: null
            LambdaArn: null

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.lookoutmetrics.alerts
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>alerts</code> resource, the following permissions are required:

### Create
```json
lookoutmetrics:CreateAlert,
iam:PassRole
```

### Delete
```json
lookoutmetrics:DeleteAlert
```

### List
```json
lookoutmetrics:ListAlerts
```

