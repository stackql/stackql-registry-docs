---
title: log_anomaly_detectors
hide_title: false
hide_table_of_contents: false
keywords:
  - log_anomaly_detectors
  - logs
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

Creates, updates, deletes or gets a <code>log_anomaly_detector</code> resource or lists <code>log_anomaly_detectors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_anomaly_detectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Logs::LogAnomalyDetector resource specifies a CloudWatch Logs LogAnomalyDetector.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.log_anomaly_detectors" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>Account ID for owner of detector</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.</td></tr>
<tr><td><CopyableCode code="detector_name" /></td><td><code>string</code></td><td>Name of detector</td></tr>
<tr><td><CopyableCode code="log_group_arn_list" /></td><td><code>array</code></td><td>List of Arns for the given log group</td></tr>
<tr><td><CopyableCode code="evaluation_frequency" /></td><td><code>string</code></td><td>How often log group is evaluated</td></tr>
<tr><td><CopyableCode code="filter_pattern" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="anomaly_detector_status" /></td><td><code>string</code></td><td>Current status of detector.</td></tr>
<tr><td><CopyableCode code="anomaly_visibility_time" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time_stamp" /></td><td><code>number</code></td><td>When detector was created.</td></tr>
<tr><td><CopyableCode code="last_modified_time_stamp" /></td><td><code>number</code></td><td>When detector was lsat modified.</td></tr>
<tr><td><CopyableCode code="anomaly_detector_arn" /></td><td><code>string</code></td><td>ARN of LogAnomalyDetector</td></tr>
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
    <td><CopyableCode code=", region" /></td>
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
List all <code>log_anomaly_detectors</code> in a region.
```sql
SELECT
region,
anomaly_detector_arn
FROM aws.logs.log_anomaly_detectors
WHERE region = 'us-east-1';
```
Gets all properties from a <code>log_anomaly_detector</code>.
```sql
SELECT
region,
account_id,
kms_key_id,
detector_name,
log_group_arn_list,
evaluation_frequency,
filter_pattern,
anomaly_detector_status,
anomaly_visibility_time,
creation_time_stamp,
last_modified_time_stamp,
anomaly_detector_arn
FROM aws.logs.log_anomaly_detectors
WHERE region = 'us-east-1' AND data__Identifier = '<AnomalyDetectorArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>log_anomaly_detector</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.logs.log_anomaly_detectors (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.logs.log_anomaly_detectors (
 AccountId,
 KmsKeyId,
 DetectorName,
 LogGroupArnList,
 EvaluationFrequency,
 FilterPattern,
 AnomalyVisibilityTime,
 region
)
SELECT 
 '{{ AccountId }}',
 '{{ KmsKeyId }}',
 '{{ DetectorName }}',
 '{{ LogGroupArnList }}',
 '{{ EvaluationFrequency }}',
 '{{ FilterPattern }}',
 '{{ AnomalyVisibilityTime }}',
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
  - name: log_anomaly_detector
    props:
      - name: AccountId
        value: '{{ AccountId }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: DetectorName
        value: '{{ DetectorName }}'
      - name: LogGroupArnList
        value:
          - '{{ LogGroupArnList[0] }}'
      - name: EvaluationFrequency
        value: '{{ EvaluationFrequency }}'
      - name: FilterPattern
        value: '{{ FilterPattern }}'
      - name: AnomalyVisibilityTime
        value: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.logs.log_anomaly_detectors
WHERE data__Identifier = '<AnomalyDetectorArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>log_anomaly_detectors</code> resource, the following permissions are required:

### Create
```json
logs:CreateLogAnomalyDetector
```

### Read
```json
logs:GetLogAnomalyDetector
```

### Update
```json
logs:UpdateLogAnomalyDetector
```

### Delete
```json
logs:DeleteLogAnomalyDetector
```

### List
```json
logs:ListLogAnomalyDetectors
```

