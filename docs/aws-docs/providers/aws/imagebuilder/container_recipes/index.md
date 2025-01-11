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

Creates, updates, deletes or gets a <code>container_recipe</code> resource or lists <code>container_recipes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_recipes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::ContainerRecipe</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.container_recipes" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the container recipe.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the container recipe.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the container recipe.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The semantic version of the container recipe (&lt;major&gt;.&lt;minor&gt;.&lt;patch&gt;).</td></tr>
<tr><td><CopyableCode code="components" /></td><td><code>array</code></td><td>Components for build and test that are included in the container recipe.</td></tr>
<tr><td><CopyableCode code="instance_configuration" /></td><td><code>object</code></td><td>A group of options that can be used to configure an instance for building and testing container images.</td></tr>
<tr><td><CopyableCode code="dockerfile_template_data" /></td><td><code>string</code></td><td>Dockerfiles are text documents that are used to build Docker containers, and ensure that they contain all of the elements required by the application running inside. The template data consists of contextual variables where Image Builder places build information or scripts, based on your container image recipe.</td></tr>
<tr><td><CopyableCode code="dockerfile_template_uri" /></td><td><code>string</code></td><td>The S3 URI for the Dockerfile that will be used to build your container image.</td></tr>
<tr><td><CopyableCode code="platform_override" /></td><td><code>string</code></td><td>Specifies the operating system platform when you use a custom source image.</td></tr>
<tr><td><CopyableCode code="container_type" /></td><td><code>string</code></td><td>Specifies the type of container, such as Docker.</td></tr>
<tr><td><CopyableCode code="image_os_version_override" /></td><td><code>string</code></td><td>Specifies the operating system version for the source image.</td></tr>
<tr><td><CopyableCode code="target_repository" /></td><td><code>object</code></td><td>The destination repository for the container image.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>Identifies which KMS key is used to encrypt the container image.</td></tr>
<tr><td><CopyableCode code="parent_image" /></td><td><code>string</code></td><td>The source image for the container recipe.</td></tr>
<tr><td><CopyableCode code="working_directory" /></td><td><code>string</code></td><td>The working directory to be used during build and test workflows.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>Tags that are attached to the container recipe.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html"><code>AWS::ImageBuilder::ContainerRecipe</code></a>.

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
Gets all <code>container_recipes</code> in a region.
```sql
SELECT
region,
arn,
name,
description,
version,
components,
instance_configuration,
dockerfile_template_data,
dockerfile_template_uri,
platform_override,
container_type,
image_os_version_override,
target_repository,
kms_key_id,
parent_image,
working_directory,
tags
FROM aws.imagebuilder.container_recipes
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>container_recipe</code>.
```sql
SELECT
region,
arn,
name,
description,
version,
components,
instance_configuration,
dockerfile_template_data,
dockerfile_template_uri,
platform_override,
container_type,
image_os_version_override,
target_repository,
kms_key_id,
parent_image,
working_directory,
tags
FROM aws.imagebuilder.container_recipes
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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
kms:GenerateDataKey,
kms:GenerateDataKeyPair,
kms:GenerateDataKeyPairWithoutPlaintext,
kms:GenerateDataKeyWithoutPlaintext,
s3:GetObject,
s3:ListBucket,
ecr:DescribeRepositories,
ec2:DescribeImages
```

### Read
```json
imagebuilder:GetContainerRecipe,
kms:Decrypt
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
