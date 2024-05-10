---
title: image_pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - image_pipelines
  - imagebuilder
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


Used to retrieve a list of <code>image_pipelines</code> in a region or to create or delete a <code>image_pipelines</code> resource, use <code>image_pipeline</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::ImagePipeline</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.image_pipelines" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the image pipeline.</td></tr>
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
FROM aws.imagebuilder.image_pipelines
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
 "Name": "{{ Name }}",
 "Description": "{{ Description }}",
 "ImageTestsConfiguration": {
  "ImageTestsEnabled": "{{ ImageTestsEnabled }}",
  "TimeoutMinutes": "{{ TimeoutMinutes }}"
 },
 "Status": "{{ Status }}",
 "Schedule": {
  "ScheduleExpression": "{{ ScheduleExpression }}",
  "PipelineExecutionStartCondition": "{{ PipelineExecutionStartCondition }}"
 },
 "ImageRecipeArn": "{{ ImageRecipeArn }}",
 "ContainerRecipeArn": "{{ ContainerRecipeArn }}",
 "DistributionConfigurationArn": "{{ DistributionConfigurationArn }}",
 "InfrastructureConfigurationArn": "{{ InfrastructureConfigurationArn }}",
 "Workflows": [
  {
   "WorkflowArn": "{{ WorkflowArn }}",
   "Parameters": [
    {
     "Name": "{{ Name }}",
     "Value": [
      "{{ Value[0] }}"
     ]
    }
   ],
   "ParallelGroup": "{{ ParallelGroup }}",
   "OnFailure": "{{ OnFailure }}"
  }
 ],
 "EnhancedImageMetadataEnabled": "{{ EnhancedImageMetadataEnabled }}",
 "ImageScanningConfiguration": {
  "EcrConfiguration": {
   "ContainerTags": [
    "{{ ContainerTags[0] }}"
   ],
   "RepositoryName": "{{ RepositoryName }}"
  },
  "ImageScanningEnabled": "{{ ImageScanningEnabled }}"
 },
 "ExecutionRole": "{{ ExecutionRole }}",
 "Tags": {}
}
>>>
--required properties only
INSERT INTO aws.imagebuilder.image_pipelines (
 Name,
 Description,
 ImageTestsConfiguration,
 Status,
 Schedule,
 ImageRecipeArn,
 ContainerRecipeArn,
 DistributionConfigurationArn,
 InfrastructureConfigurationArn,
 Workflows,
 EnhancedImageMetadataEnabled,
 ImageScanningConfiguration,
 ExecutionRole,
 Tags,
 region
)
SELECT 
{{ .Name }},
 {{ .Description }},
 {{ .ImageTestsConfiguration }},
 {{ .Status }},
 {{ .Schedule }},
 {{ .ImageRecipeArn }},
 {{ .ContainerRecipeArn }},
 {{ .DistributionConfigurationArn }},
 {{ .InfrastructureConfigurationArn }},
 {{ .Workflows }},
 {{ .EnhancedImageMetadataEnabled }},
 {{ .ImageScanningConfiguration }},
 {{ .ExecutionRole }},
 {{ .Tags }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Description": "{{ Description }}",
 "ImageTestsConfiguration": {
  "ImageTestsEnabled": "{{ ImageTestsEnabled }}",
  "TimeoutMinutes": "{{ TimeoutMinutes }}"
 },
 "Status": "{{ Status }}",
 "Schedule": {
  "ScheduleExpression": "{{ ScheduleExpression }}",
  "PipelineExecutionStartCondition": "{{ PipelineExecutionStartCondition }}"
 },
 "ImageRecipeArn": "{{ ImageRecipeArn }}",
 "ContainerRecipeArn": "{{ ContainerRecipeArn }}",
 "DistributionConfigurationArn": "{{ DistributionConfigurationArn }}",
 "InfrastructureConfigurationArn": "{{ InfrastructureConfigurationArn }}",
 "Workflows": [
  {
   "WorkflowArn": "{{ WorkflowArn }}",
   "Parameters": [
    {
     "Name": "{{ Name }}",
     "Value": [
      "{{ Value[0] }}"
     ]
    }
   ],
   "ParallelGroup": "{{ ParallelGroup }}",
   "OnFailure": "{{ OnFailure }}"
  }
 ],
 "EnhancedImageMetadataEnabled": "{{ EnhancedImageMetadataEnabled }}",
 "ImageScanningConfiguration": {
  "EcrConfiguration": {
   "ContainerTags": [
    "{{ ContainerTags[0] }}"
   ],
   "RepositoryName": "{{ RepositoryName }}"
  },
  "ImageScanningEnabled": "{{ ImageScanningEnabled }}"
 },
 "ExecutionRole": "{{ ExecutionRole }}",
 "Tags": {}
}
>>>
--all properties
INSERT INTO aws.imagebuilder.image_pipelines (
 Name,
 Description,
 ImageTestsConfiguration,
 Status,
 Schedule,
 ImageRecipeArn,
 ContainerRecipeArn,
 DistributionConfigurationArn,
 InfrastructureConfigurationArn,
 Workflows,
 EnhancedImageMetadataEnabled,
 ImageScanningConfiguration,
 ExecutionRole,
 Tags,
 region
)
SELECT 
 {{ .Name }},
 {{ .Description }},
 {{ .ImageTestsConfiguration }},
 {{ .Status }},
 {{ .Schedule }},
 {{ .ImageRecipeArn }},
 {{ .ContainerRecipeArn }},
 {{ .DistributionConfigurationArn }},
 {{ .InfrastructureConfigurationArn }},
 {{ .Workflows }},
 {{ .EnhancedImageMetadataEnabled }},
 {{ .ImageScanningConfiguration }},
 {{ .ExecutionRole }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.imagebuilder.image_pipelines
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>image_pipelines</code> resource, the following permissions are required:

### Create
```json
ecr:BatchGetRepositoryScanningConfiguration,
iam:GetRole,
iam:PassRole,
iam:CreateServiceLinkedRole,
imagebuilder:TagResource,
imagebuilder:GetImagePipeline,
imagebuilder:GetImageRecipe,
imagebuilder:GetInfrastructureConfiguration,
imagebuilder:GetDistributionConfiguration,
imagebuilder:CreateImagePipeline,
imagebuilder:GetWorkflow,
inspector2:BatchGetAccountStatus
```

### Delete
```json
imagebuilder:UnTagResource,
imagebuilder:GetImagePipeline,
imagebuilder:DeleteImagePipeline
```

### List
```json
imagebuilder:ListImagePipelines
```

