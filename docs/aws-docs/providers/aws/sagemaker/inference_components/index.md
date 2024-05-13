---
title: inference_components
hide_title: false
hide_table_of_contents: false
keywords:
  - inference_components
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


Used to retrieve a list of <code>inference_components</code> in a region or to create or delete a <code>inference_components</code> resource, use <code>inference_component</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inference_components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::InferenceComponent</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.inference_components" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="inference_component_arn" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="EndpointName, VariantName, Specification, RuntimeConfig, region" /></td>
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
inference_component_arn
FROM aws.sagemaker.inference_components
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>inference_component</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.inference_components (
 EndpointName,
 VariantName,
 Specification,
 RuntimeConfig,
 region
)
SELECT 
'{{ EndpointName }}',
 '{{ VariantName }}',
 '{{ Specification }}',
 '{{ RuntimeConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.inference_components (
 InferenceComponentName,
 EndpointArn,
 EndpointName,
 VariantName,
 Specification,
 RuntimeConfig,
 Tags,
 region
)
SELECT 
 '{{ InferenceComponentName }}',
 '{{ EndpointArn }}',
 '{{ EndpointName }}',
 '{{ VariantName }}',
 '{{ Specification }}',
 '{{ RuntimeConfig }}',
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
  - name: inference_component
    props:
      - name: InferenceComponentName
        value: '{{ InferenceComponentName }}'
      - name: EndpointArn
        value: '{{ EndpointArn }}'
      - name: EndpointName
        value: '{{ EndpointName }}'
      - name: VariantName
        value: '{{ VariantName }}'
      - name: Specification
        value:
          ModelName: '{{ ModelName }}'
          Container:
            DeployedImage:
              SpecifiedImage: '{{ SpecifiedImage }}'
              ResolvedImage: null
              ResolutionTime: '{{ ResolutionTime }}'
            Image: null
            ArtifactUrl: '{{ ArtifactUrl }}'
            Environment: {}
          StartupParameters:
            ModelDataDownloadTimeoutInSeconds: '{{ ModelDataDownloadTimeoutInSeconds }}'
            ContainerStartupHealthCheckTimeoutInSeconds: null
          ComputeResourceRequirements:
            NumberOfCpuCoresRequired: null
            NumberOfAcceleratorDevicesRequired: null
            MinMemoryRequiredInMb: '{{ MinMemoryRequiredInMb }}'
            MaxMemoryRequiredInMb: null
      - name: RuntimeConfig
        value:
          CopyCount: '{{ CopyCount }}'
          DesiredCopyCount: null
          CurrentCopyCount: null
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.sagemaker.inference_components
WHERE data__Identifier = '<InferenceComponentArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>inference_components</code> resource, the following permissions are required:

### Create
```json
sagemaker:AddTags,
sagemaker:ListTags,
sagemaker:CreateInferenceComponent,
sagemaker:DescribeInferenceComponent
```

### Delete
```json
sagemaker:DescribeInferenceComponent,
sagemaker:DeleteInferenceComponent,
sagemaker:DeleteTags
```

### List
```json
sagemaker:ListInferenceComponents,
sagemaker:DescribeInferenceComponent,
sagemaker:ListTags
```

