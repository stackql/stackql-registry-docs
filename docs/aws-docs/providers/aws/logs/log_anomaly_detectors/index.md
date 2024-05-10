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


Used to retrieve a list of <code>log_anomaly_detectors</code> in a region or to create or delete a <code>log_anomaly_detectors</code> resource, use <code>log_anomaly_detector</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_anomaly_detectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Logs::LogAnomalyDetector resource specifies a CloudWatch Logs LogAnomalyDetector.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.log_anomaly_detectors" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
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
anomaly_detector_arn
FROM aws.logs.log_anomaly_detectors
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{}
>>>
--required properties only
INSERT INTO aws.logs.log_anomaly_detectors (
 ,
 region
)
SELECT 
{{ . }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AccountId": "{{ AccountId }}",
 "KmsKeyId": "{{ KmsKeyId }}",
 "DetectorName": "{{ DetectorName }}",
 "LogGroupArnList": [
  "{{ LogGroupArnList[0] }}"
 ],
 "EvaluationFrequency": "{{ EvaluationFrequency }}",
 "FilterPattern": "{{ FilterPattern }}",
 "AnomalyVisibilityTime": null
}
>>>
--all properties
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
 {{ .AccountId }},
 {{ .KmsKeyId }},
 {{ .DetectorName }},
 {{ .LogGroupArnList }},
 {{ .EvaluationFrequency }},
 {{ .FilterPattern }},
 {{ .AnomalyVisibilityTime }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
logs:DeleteLogAnomalyDetector
```

### List
```json
logs:ListLogAnomalyDetectors
```

