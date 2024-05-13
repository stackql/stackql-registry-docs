---
title: inference_experiments
hide_title: false
hide_table_of_contents: false
keywords:
  - inference_experiments
  - sagemaker
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


Used to retrieve a list of <code>inference_experiments</code> in a region or to create or delete a <code>inference_experiments</code> resource, use <code>inference_experiment</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inference_experiments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::InferenceExperiment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.inference_experiments" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the inference experiment.</td></tr>
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
    <td><CopyableCode code="Name, Type, RoleArn, EndpointName, ModelVariants, region" /></td>
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
name
FROM aws.sagemaker.inference_experiments
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>inference_experiment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.inference_experiments (
 Name,
 Type,
 RoleArn,
 EndpointName,
 ModelVariants,
 region
)
SELECT 
'{{ Name }}',
 '{{ Type }}',
 '{{ RoleArn }}',
 '{{ EndpointName }}',
 '{{ ModelVariants }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.inference_experiments (
 Name,
 Type,
 Description,
 RoleArn,
 EndpointName,
 Schedule,
 KmsKey,
 DataStorageConfig,
 ModelVariants,
 ShadowModeConfig,
 Tags,
 StatusReason,
 DesiredState,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Type }}',
 '{{ Description }}',
 '{{ RoleArn }}',
 '{{ EndpointName }}',
 '{{ Schedule }}',
 '{{ KmsKey }}',
 '{{ DataStorageConfig }}',
 '{{ ModelVariants }}',
 '{{ ShadowModeConfig }}',
 '{{ Tags }}',
 '{{ StatusReason }}',
 '{{ DesiredState }}',
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
  - name: inference_experiment
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Type
        value: '{{ Type }}'
      - name: Description
        value: '{{ Description }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: EndpointName
        value: '{{ EndpointName }}'
      - name: Schedule
        value:
          StartTime: '{{ StartTime }}'
          EndTime: '{{ EndTime }}'
      - name: KmsKey
        value: '{{ KmsKey }}'
      - name: DataStorageConfig
        value:
          Destination: '{{ Destination }}'
          KmsKey: '{{ KmsKey }}'
          ContentType:
            CsvContentTypes:
              - '{{ CsvContentTypes[0] }}'
            JsonContentTypes:
              - '{{ JsonContentTypes[0] }}'
      - name: ModelVariants
        value:
          - ModelName: '{{ ModelName }}'
            VariantName: '{{ VariantName }}'
            InfrastructureConfig:
              InfrastructureType: '{{ InfrastructureType }}'
              RealTimeInferenceConfig:
                InstanceType: '{{ InstanceType }}'
                InstanceCount: '{{ InstanceCount }}'
      - name: ShadowModeConfig
        value:
          SourceModelVariantName: '{{ SourceModelVariantName }}'
          ShadowModelVariants:
            - ShadowModelVariantName: '{{ ShadowModelVariantName }}'
              SamplingPercentage: '{{ SamplingPercentage }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: StatusReason
        value: '{{ StatusReason }}'
      - name: DesiredState
        value: '{{ DesiredState }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.sagemaker.inference_experiments
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>inference_experiments</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateInferenceExperiment,
sagemaker:DescribeInferenceExperiment,
sagemaker:AddTags,
sagemaker:ListTags,
iam:PassRole
```

### Delete
```json
sagemaker:DeleteInferenceExperiment,
sagemaker:DescribeInferenceExperiment,
sagemaker:StopInferenceExperiment,
sagemaker:ListTags
```

### List
```json
sagemaker:ListInferenceExperiments
```

