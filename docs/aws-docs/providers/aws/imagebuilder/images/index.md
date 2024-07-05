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

Creates, updates, deletes or gets an <code>image</code> resource or lists <code>images</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::Image</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.images" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the image.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the image.</td></tr>
<tr><td><CopyableCode code="image_tests_configuration" /></td><td><code>object</code></td><td>The image tests configuration used when creating this image.</td></tr>
<tr><td><CopyableCode code="image_recipe_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.</td></tr>
<tr><td><CopyableCode code="container_recipe_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested.</td></tr>
<tr><td><CopyableCode code="distribution_configuration_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the distribution configuration.</td></tr>
<tr><td><CopyableCode code="infrastructure_configuration_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the infrastructure configuration.</td></tr>
<tr><td><CopyableCode code="workflows" /></td><td><code>array</code></td><td>Workflows to define the image build process</td></tr>
<tr><td><CopyableCode code="image_id" /></td><td><code>string</code></td><td>The AMI ID of the EC2 AMI in current region.</td></tr>
<tr><td><CopyableCode code="image_uri" /></td><td><code>string</code></td><td>URI for containers created in current Region with default ECR image tag</td></tr>
<tr><td><CopyableCode code="enhanced_image_metadata_enabled" /></td><td><code>boolean</code></td><td>Collects additional information about the image being created, including the operating system (OS) version and package list.</td></tr>
<tr><td><CopyableCode code="image_scanning_configuration" /></td><td><code>object</code></td><td>Contains settings for vulnerability scans.</td></tr>
<tr><td><CopyableCode code="execution_role" /></td><td><code>string</code></td><td>The execution role name/ARN for the image build, if provided</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>The tags associated with the image.</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>images</code> in a region.
```sql
SELECT
region,
arn,
name,
image_tests_configuration,
image_recipe_arn,
container_recipe_arn,
distribution_configuration_arn,
infrastructure_configuration_arn,
workflows,
image_id,
image_uri,
enhanced_image_metadata_enabled,
image_scanning_configuration,
execution_role,
tags
FROM aws.imagebuilder.images
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>image</code>.
```sql
SELECT
region,
arn,
name,
image_tests_configuration,
image_recipe_arn,
container_recipe_arn,
distribution_configuration_arn,
infrastructure_configuration_arn,
workflows,
image_id,
image_uri,
enhanced_image_metadata_enabled,
image_scanning_configuration,
execution_role,
tags
FROM aws.imagebuilder.images
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
imagebuilder:GetImage
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

