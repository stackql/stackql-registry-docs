---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
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


Used to retrieve a list of <code>images</code> in a region or to create or delete a <code>images</code> resource, use <code>image</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::Image</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.images" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the image.</td></tr>
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
FROM aws.imagebuilder.images
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>image</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- image.iql (required properties only)
INSERT INTO aws.imagebuilder.images (
 ImageTestsConfiguration,
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
'{{ ImageTestsConfiguration }}',
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
-- image.iql (all properties)
INSERT INTO aws.imagebuilder.images (
 ImageTestsConfiguration,
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
 '{{ ImageTestsConfiguration }}',
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
  - name: image
    props:
      - name: ImageTestsConfiguration
        value:
          ImageTestsEnabled: '{{ ImageTestsEnabled }}'
          TimeoutMinutes: '{{ TimeoutMinutes }}'
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
DELETE FROM aws.imagebuilder.images
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>images</code> resource, the following permissions are required:

### Create
```json
ecr:BatchGetRepositoryScanningConfiguration,
iam:GetRole,
iam:PassRole,
iam:CreateServiceLinkedRole,
imagebuilder:GetImageRecipe,
imagebuilder:GetInfrastructureConfiguration,
imagebuilder:GetDistributionConfiguration,
imagebuilder:GetWorkflow,
imagebuilder:GetImage,
imagebuilder:CreateImage,
imagebuilder:TagResource,
inspector2:BatchGetAccountStatus
```

### Delete
```json
imagebuilder:GetImage,
imagebuilder:DeleteImage,
imagebuilder:UnTagResource,
imagebuilder:CancelImageCreation
```

### List
```json
imagebuilder:ListImages
```

