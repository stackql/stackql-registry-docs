---
title: container_recipes
hide_title: false
hide_table_of_contents: false
keywords:
  - container_recipes
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


Used to retrieve a list of <code>container_recipes</code> in a region or to create or delete a <code>container_recipes</code> resource, use <code>container_recipe</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_recipes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::ContainerRecipe</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.container_recipes" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the container recipe.</td></tr>
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
FROM aws.imagebuilder.container_recipes
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>container_recipe</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- container_recipe.iql (required properties only)
INSERT INTO aws.imagebuilder.container_recipes (
 Name,
 Description,
 Version,
 Components,
 InstanceConfiguration,
 DockerfileTemplateData,
 DockerfileTemplateUri,
 PlatformOverride,
 ContainerType,
 ImageOsVersionOverride,
 TargetRepository,
 KmsKeyId,
 ParentImage,
 WorkingDirectory,
 Tags,
 region
)
SELECT 
'{{ Name }}',
 '{{ Description }}',
 '{{ Version }}',
 '{{ Components }}',
 '{{ InstanceConfiguration }}',
 '{{ DockerfileTemplateData }}',
 '{{ DockerfileTemplateUri }}',
 '{{ PlatformOverride }}',
 '{{ ContainerType }}',
 '{{ ImageOsVersionOverride }}',
 '{{ TargetRepository }}',
 '{{ KmsKeyId }}',
 '{{ ParentImage }}',
 '{{ WorkingDirectory }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- container_recipe.iql (all properties)
INSERT INTO aws.imagebuilder.container_recipes (
 Name,
 Description,
 Version,
 Components,
 InstanceConfiguration,
 DockerfileTemplateData,
 DockerfileTemplateUri,
 PlatformOverride,
 ContainerType,
 ImageOsVersionOverride,
 TargetRepository,
 KmsKeyId,
 ParentImage,
 WorkingDirectory,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ Version }}',
 '{{ Components }}',
 '{{ InstanceConfiguration }}',
 '{{ DockerfileTemplateData }}',
 '{{ DockerfileTemplateUri }}',
 '{{ PlatformOverride }}',
 '{{ ContainerType }}',
 '{{ ImageOsVersionOverride }}',
 '{{ TargetRepository }}',
 '{{ KmsKeyId }}',
 '{{ ParentImage }}',
 '{{ WorkingDirectory }}',
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
  - name: container_recipe
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: Version
        value: '{{ Version }}'
      - name: Components
        value:
          - ComponentArn: '{{ ComponentArn }}'
            Parameters:
              - Name: '{{ Name }}'
                Value:
                  - '{{ Value[0] }}'
      - name: InstanceConfiguration
        value:
          Image: '{{ Image }}'
          BlockDeviceMappings:
            - DeviceName: '{{ DeviceName }}'
              VirtualName: '{{ VirtualName }}'
              NoDevice: '{{ NoDevice }}'
              Ebs:
                Encrypted: '{{ Encrypted }}'
                DeleteOnTermination: '{{ DeleteOnTermination }}'
                Iops: '{{ Iops }}'
                KmsKeyId: '{{ KmsKeyId }}'
                SnapshotId: '{{ SnapshotId }}'
                Throughput: '{{ Throughput }}'
                VolumeSize: '{{ VolumeSize }}'
                VolumeType: '{{ VolumeType }}'
      - name: DockerfileTemplateData
        value: '{{ DockerfileTemplateData }}'
      - name: DockerfileTemplateUri
        value: '{{ DockerfileTemplateUri }}'
      - name: PlatformOverride
        value: '{{ PlatformOverride }}'
      - name: ContainerType
        value: '{{ ContainerType }}'
      - name: ImageOsVersionOverride
        value: '{{ ImageOsVersionOverride }}'
      - name: TargetRepository
        value:
          Service: '{{ Service }}'
          RepositoryName: '{{ RepositoryName }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: ParentImage
        value: '{{ ParentImage }}'
      - name: WorkingDirectory
        value: '{{ WorkingDirectory }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.imagebuilder.container_recipes
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>container_recipes</code> resource, the following permissions are required:

### Create
```json
iam:GetRole,
iam:CreateServiceLinkedRole,
imagebuilder:GetComponent,
imagebuilder:TagResource,
imagebuilder:GetContainerRecipe,
imagebuilder:CreateContainerRecipe,
imagebuilder:GetImage,
kms:Encrypt,
kms:Decrypt,
kms:ReEncryptFrom,
kms:ReEncryptTo,
kms:GenerateDataKey*,
s3:GetObject,
s3:ListBucket,
ecr:DescribeRepositories,
ec2:DescribeImages
```

### Delete
```json
imagebuilder:UnTagResource,
imagebuilder:GetContainerRecipe,
imagebuilder:DeleteContainerRecipe
```

### List
```json
imagebuilder:ListContainerRecipes
```

