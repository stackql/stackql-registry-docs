---
title: image_recipes
hide_title: false
hide_table_of_contents: false
keywords:
  - image_recipes
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

Creates, updates, deletes or gets an <code>image_recipe</code> resource or lists <code>image_recipes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_recipes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::ImageRecipe</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.image_recipes" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the image recipe.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the image recipe.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the image recipe.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The version of the image recipe.</td></tr>
<tr><td><CopyableCode code="components" /></td><td><code>array</code></td><td>The components of the image recipe.</td></tr>
<tr><td><CopyableCode code="block_device_mappings" /></td><td><code>array</code></td><td>The block device mappings to apply when creating images from this recipe.</td></tr>
<tr><td><CopyableCode code="parent_image" /></td><td><code>string</code></td><td>The parent image of the image recipe.</td></tr>
<tr><td><CopyableCode code="working_directory" /></td><td><code>string</code></td><td>The working directory to be used during build and test workflows.</td></tr>
<tr><td><CopyableCode code="additional_instance_configuration" /></td><td><code>object</code></td><td>Specify additional settings and launch scripts for your build instances.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>The tags of the image recipe.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html"><code>AWS::ImageBuilder::ImageRecipe</code></a>.

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
    <td><CopyableCode code="Name, Version, Components, ParentImage, region" /></td>
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
Gets all <code>image_recipes</code> in a region.
```sql
SELECT
region,
arn,
name,
description,
version,
components,
block_device_mappings,
parent_image,
working_directory,
additional_instance_configuration,
tags
FROM aws.imagebuilder.image_recipes
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>image_recipe</code>.
```sql
SELECT
region,
arn,
name,
description,
version,
components,
block_device_mappings,
parent_image,
working_directory,
additional_instance_configuration,
tags
FROM aws.imagebuilder.image_recipes
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>image_recipe</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.imagebuilder.image_recipes (
 Name,
 Version,
 Components,
 ParentImage,
 region
)
SELECT 
'{{ Name }}',
 '{{ Version }}',
 '{{ Components }}',
 '{{ ParentImage }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.imagebuilder.image_recipes (
 Name,
 Description,
 Version,
 Components,
 BlockDeviceMappings,
 ParentImage,
 WorkingDirectory,
 AdditionalInstanceConfiguration,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ Version }}',
 '{{ Components }}',
 '{{ BlockDeviceMappings }}',
 '{{ ParentImage }}',
 '{{ WorkingDirectory }}',
 '{{ AdditionalInstanceConfiguration }}',
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
  - name: image_recipe
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
      - name: BlockDeviceMappings
        value:
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
      - name: ParentImage
        value: '{{ ParentImage }}'
      - name: WorkingDirectory
        value: '{{ WorkingDirectory }}'
      - name: AdditionalInstanceConfiguration
        value:
          SystemsManagerAgent:
            UninstallAfterBuild: '{{ UninstallAfterBuild }}'
          UserDataOverride: '{{ UserDataOverride }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.imagebuilder.image_recipes
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>image_recipes</code> resource, the following permissions are required:

### Create
```json
iam:GetRole,
iam:CreateServiceLinkedRole,
imagebuilder:GetComponent,
imagebuilder:GetImage,
imagebuilder:TagResource,
imagebuilder:GetImageRecipe,
imagebuilder:CreateImageRecipe,
ec2:DescribeImages
```

### Read
```json
imagebuilder:GetImageRecipe
```

### Delete
```json
imagebuilder:UnTagResource,
imagebuilder:GetImageRecipe,
imagebuilder:DeleteImageRecipe
```

### List
```json
imagebuilder:ListImageRecipes
```
