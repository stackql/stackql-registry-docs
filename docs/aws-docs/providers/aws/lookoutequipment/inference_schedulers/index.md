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

Creates, updates, deletes or gets an <code>inference_scheduler</code> resource or lists <code>inference_schedulers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inference_schedulers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for LookoutEquipment InferenceScheduler.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lookoutequipment.inference_schedulers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="data_delay_offset_in_minutes" /></td><td><code>integer</code></td><td>A period of time (in minutes) by which inference on the data is delayed after the data starts.</td></tr>
<tr><td><CopyableCode code="data_input_configuration" /></td><td><code>object</code></td><td>Specifies configuration information for the input data for the inference scheduler, including delimiter, format, and dataset location.</td></tr>
<tr><td><CopyableCode code="data_output_configuration" /></td><td><code>object</code></td><td>Specifies configuration information for the output results for the inference scheduler, including the S3 location for the output.</td></tr>
<tr><td><CopyableCode code="data_upload_frequency" /></td><td><code>string</code></td><td>How often data is uploaded to the source S3 bucket for the input data.</td></tr>
<tr><td><CopyableCode code="inference_scheduler_name" /></td><td><code>string</code></td><td>The name of the inference scheduler being created.</td></tr>
<tr><td><CopyableCode code="model_name" /></td><td><code>string</code></td><td>The name of the previously trained ML model being used to create the inference scheduler.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of a role with permission to access the data source being used for the inference.</td></tr>
<tr><td><CopyableCode code="server_side_kms_key_id" /></td><td><code>string</code></td><td>Provides the identifier of the AWS KMS customer master key (CMK) used to encrypt inference scheduler data by Amazon Lookout for Equipment.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Any tags associated with the inference scheduler.</td></tr>
<tr><td><CopyableCode code="inference_scheduler_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the inference scheduler being created.</td></tr>
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
    <td><CopyableCode code="DataInputConfiguration, DataOutputConfiguration, DataUploadFrequency, ModelName, RoleArn, region" /></td>
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
List all <code>inference_schedulers</code> in a region.
```sql
SELECT
region,
inference_scheduler_name
FROM aws.lookoutequipment.inference_schedulers
WHERE region = 'us-east-1';
```
Gets all properties from an <code>inference_scheduler</code>.
```sql
SELECT
region,
data_delay_offset_in_minutes,
data_input_configuration,
data_output_configuration,
data_upload_frequency,
inference_scheduler_name,
model_name,
role_arn,
server_side_kms_key_id,
tags,
inference_scheduler_arn
FROM aws.lookoutequipment.inference_schedulers
WHERE region = 'us-east-1' AND data__Identifier = '<InferenceSchedulerName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>inference_scheduler</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.lookoutequipment.inference_schedulers (
 DataInputConfiguration,
 DataOutputConfiguration,
 DataUploadFrequency,
 ModelName,
 RoleArn,
 region
)
SELECT 
'{{ DataInputConfiguration }}',
 '{{ DataOutputConfiguration }}',
 '{{ DataUploadFrequency }}',
 '{{ ModelName }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ DataDelayOffsetInMinutes }}',
 '{{ DataInputConfiguration }}',
 '{{ DataOutputConfiguration }}',
 '{{ DataUploadFrequency }}',
 '{{ InferenceSchedulerName }}',
 '{{ ModelName }}',
 '{{ RoleArn }}',
 '{{ ServerSideKmsKeyId }}',
 '{{ Tags }}',
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
  - name: inference_scheduler
    props:
      - name: DataDelayOffsetInMinutes
        value: '{{ DataDelayOffsetInMinutes }}'
      - name: DataInputConfiguration
        value:
          InputTimeZoneOffset: '{{ InputTimeZoneOffset }}'
          InferenceInputNameConfiguration:
            ComponentTimestampDelimiter: '{{ ComponentTimestampDelimiter }}'
            TimestampFormat: '{{ TimestampFormat }}'
          S3InputConfiguration:
            Bucket: '{{ Bucket }}'
            Prefix: '{{ Prefix }}'
      - name: DataOutputConfiguration
        value:
          KmsKeyId: '{{ KmsKeyId }}'
          S3OutputConfiguration:
            Bucket: null
            Prefix: null
      - name: DataUploadFrequency
        value: '{{ DataUploadFrequency }}'
      - name: InferenceSchedulerName
        value: '{{ InferenceSchedulerName }}'
      - name: ModelName
        value: '{{ ModelName }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: ServerSideKmsKeyId
        value: '{{ ServerSideKmsKeyId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
lookoutequipment:DescribeInferenceScheduler
```

### Delete
```json
lookoutequipment:DeleteInferenceScheduler,
lookoutequipment:StopInferenceScheduler,
lookoutequipment:DescribeInferenceScheduler
```

### Update
```json
lookoutequipment:UpdateInferenceScheduler,
lookoutequipment:DescribeInferenceScheduler,
lookoutequipment:StopInferenceScheduler,
lookoutequipment:StartInferenceScheduler
```

### List
```json
lookoutequipment:ListInferenceSchedulers
```

