---
title: inference_schedulers
hide_title: false
hide_table_of_contents: false
keywords:
  - inference_schedulers
  - lookoutequipment
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


Used to retrieve a list of <code>inference_schedulers</code> in a region or to create or delete a <code>inference_schedulers</code> resource, use <code>inference_scheduler</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inference_schedulers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for LookoutEquipment InferenceScheduler.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lookoutequipment.inference_schedulers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="inference_scheduler_name" /></td><td><code>string</code></td><td>The name of the inference scheduler being created.</td></tr>
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
inference_scheduler_name
FROM aws.lookoutequipment.inference_schedulers
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
{
 "DataInputConfiguration": {
  "InputTimeZoneOffset": "{{ InputTimeZoneOffset }}",
  "InferenceInputNameConfiguration": {
   "ComponentTimestampDelimiter": "{{ ComponentTimestampDelimiter }}",
   "TimestampFormat": "{{ TimestampFormat }}"
  },
  "S3InputConfiguration": {
   "Bucket": "{{ Bucket }}",
   "Prefix": "{{ Prefix }}"
  }
 },
 "DataOutputConfiguration": {
  "KmsKeyId": "{{ KmsKeyId }}",
  "S3OutputConfiguration": {
   "Bucket": null,
   "Prefix": null
  }
 },
 "DataUploadFrequency": "{{ DataUploadFrequency }}",
 "ModelName": "{{ ModelName }}",
 "RoleArn": "{{ RoleArn }}"
}
>>>
--required properties only
INSERT INTO aws.lookoutequipment.inference_schedulers (
 DataInputConfiguration,
 DataOutputConfiguration,
 DataUploadFrequency,
 ModelName,
 RoleArn,
 region
)
SELECT 
{{ .DataInputConfiguration }},
 {{ .DataOutputConfiguration }},
 {{ .DataUploadFrequency }},
 {{ .ModelName }},
 {{ .RoleArn }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DataDelayOffsetInMinutes": "{{ DataDelayOffsetInMinutes }}",
 "DataInputConfiguration": {
  "InputTimeZoneOffset": "{{ InputTimeZoneOffset }}",
  "InferenceInputNameConfiguration": {
   "ComponentTimestampDelimiter": "{{ ComponentTimestampDelimiter }}",
   "TimestampFormat": "{{ TimestampFormat }}"
  },
  "S3InputConfiguration": {
   "Bucket": "{{ Bucket }}",
   "Prefix": "{{ Prefix }}"
  }
 },
 "DataOutputConfiguration": {
  "KmsKeyId": "{{ KmsKeyId }}",
  "S3OutputConfiguration": {
   "Bucket": null,
   "Prefix": null
  }
 },
 "DataUploadFrequency": "{{ DataUploadFrequency }}",
 "InferenceSchedulerName": "{{ InferenceSchedulerName }}",
 "ModelName": "{{ ModelName }}",
 "RoleArn": "{{ RoleArn }}",
 "ServerSideKmsKeyId": "{{ ServerSideKmsKeyId }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.lookoutequipment.inference_schedulers (
 DataDelayOffsetInMinutes,
 DataInputConfiguration,
 DataOutputConfiguration,
 DataUploadFrequency,
 InferenceSchedulerName,
 ModelName,
 RoleArn,
 ServerSideKmsKeyId,
 Tags,
 region
)
SELECT 
 {{ .DataDelayOffsetInMinutes }},
 {{ .DataInputConfiguration }},
 {{ .DataOutputConfiguration }},
 {{ .DataUploadFrequency }},
 {{ .InferenceSchedulerName }},
 {{ .ModelName }},
 {{ .RoleArn }},
 {{ .ServerSideKmsKeyId }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.lookoutequipment.inference_schedulers
WHERE data__Identifier = '<InferenceSchedulerName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>inference_schedulers</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
lookoutequipment:CreateInferenceScheduler,
lookoutequipment:DescribeInferenceScheduler
```

### Delete
```json
lookoutequipment:DeleteInferenceScheduler,
lookoutequipment:StopInferenceScheduler,
lookoutequipment:DescribeInferenceScheduler
```

### List
```json
lookoutequipment:ListInferenceSchedulers
```

