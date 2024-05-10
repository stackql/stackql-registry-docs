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

Use the following StackQL query and manifest file to create a new <code>image_pipeline</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- image_pipeline.iql (required properties only)
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
'{{ Name }}',
 '{{ Description }}',
 '{{ ImageTestsConfiguration }}',
 '{{ Status }}',
 '{{ Schedule }}',
 '{{ ImageRecipeArn }}',
 '{{ ContainerRecipeArn }}',
 '{{ DistributionConfigurationArn }}',
 '{{ InfrastructureConfigurationArn }}',
 '{{ Workflows }}',
 '{{ EnhancedImageMetadataEnabled }}',
 '{{ ImageScanningConfiguration }}',
 '{{ ExecutionRole }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- image_pipeline.iql (all properties)
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
 '{{ Name }}',
 '{{ Description }}',
 '{{ ImageTestsConfiguration }}',
 '{{ Status }}',
 '{{ Schedule }}',
 '{{ ImageRecipeArn }}',
 '{{ ContainerRecipeArn }}',
 '{{ DistributionConfigurationArn }}',
 '{{ InfrastructureConfigurationArn }}',
 '{{ Workflows }}',
 '{{ EnhancedImageMetadataEnabled }}',
 '{{ ImageScanningConfiguration }}',
 '{{ ExecutionRole }}',
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
  - name: image_pipeline
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: ImageTestsConfiguration
        value:
          ImageTestsEnabled: '{{ ImageTestsEnabled }}'
          TimeoutMinutes: '{{ TimeoutMinutes }}'
      - name: Status
        value: '{{ Status }}'
      - name: Schedule
        value:
          ScheduleExpression: '{{ ScheduleExpression }}'
          PipelineExecutionStartCondition: '{{ PipelineExecutionStartCondition }}'
      - name: ImageRecipeArn
        value: '{{ ImageRecipeArn }}'
      - name: ContainerRecipeArn
        value: '{{ ContainerRecipeArn }}'
      - name: DistributionConfigurationArn
        value: '{{ DistributionConfigurationArn }}'
      - name: InfrastructureConfigurationArn
        value: '{{ InfrastructureConfigurationArn }}'
      - name: Workflows
        value:
          - WorkflowArn: '{{ WorkflowArn }}'
            Parameters:
              - Name: '{{ Name }}'
                Value:
                  - '{{ Value[0] }}'
            ParallelGroup: '{{ ParallelGroup }}'
            OnFailure: '{{ OnFailure }}'
      - name: EnhancedImageMetadataEnabled
        value: '{{ EnhancedImageMetadataEnabled }}'
      - name: ImageScanningConfiguration
        value:
          EcrConfiguration:
            ContainerTags:
              - '{{ ContainerTags[0] }}'
            RepositoryName: '{{ RepositoryName }}'
          ImageScanningEnabled: '{{ ImageScanningEnabled }}'
      - name: ExecutionRole
        value: '{{ ExecutionRole }}'
      - name: Tags
        value: {}

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

