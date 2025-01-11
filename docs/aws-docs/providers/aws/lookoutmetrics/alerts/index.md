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

Creates, updates, deletes or gets an <code>alert</code> resource or lists <code>alerts</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::LookoutMetrics::Alert</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lookoutmetrics.alerts" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="alert_name" /></td><td><code>string</code></td><td>The name of the alert. If not provided, a name is generated automatically.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>ARN assigned to the alert.</td></tr>
<tr><td><CopyableCode code="alert_description" /></td><td><code>string</code></td><td>A description for the alert.</td></tr>
<tr><td><CopyableCode code="anomaly_detector_arn" /></td><td><code>string</code></td><td>The Amazon resource name (ARN) of the Anomaly Detector to alert.</td></tr>
<tr><td><CopyableCode code="alert_sensitivity_threshold" /></td><td><code>integer</code></td><td>A number between 0 and 100 (inclusive) that tunes the sensitivity of the alert.</td></tr>
<tr><td><CopyableCode code="action" /></td><td><code>object</code></td><td>The action to be taken by the alert when an anomaly is detected.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html"><code>AWS::LookoutMetrics::Alert</code></a>.

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
    <td><CopyableCode code="AnomalyDetectorArn, AlertSensitivityThreshold, Action, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>alerts</code> in a region.
```sql
SELECT
region,
alert_name,
arn,
alert_description,
anomaly_detector_arn,
alert_sensitivity_threshold,
action
FROM aws.lookoutmetrics.alerts
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>alert</code>.
```sql
SELECT
region,
alert_name,
arn,
alert_description,
anomaly_detector_arn,
alert_sensitivity_threshold,
action
FROM aws.lookoutmetrics.alerts
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
lookoutmetrics:DescribeAlert
```

### Delete
```json
lookoutmetrics:DeleteAlert
```

### List
```json
lookoutmetrics:ListAlerts
```
