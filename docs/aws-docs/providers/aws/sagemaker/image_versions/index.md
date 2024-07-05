---
title: image_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - image_versions
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

Creates, updates, deletes or gets an <code>image_version</code> resource or lists <code>image_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::ImageVersion</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.image_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="image_name" /></td><td><code>string</code></td><td>The name of the image this version belongs to.</td></tr>
<tr><td><CopyableCode code="image_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the parent image.</td></tr>
<tr><td><CopyableCode code="image_version_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the image version.</td></tr>
<tr><td><CopyableCode code="base_image" /></td><td><code>string</code></td><td>The registry path of the container image on which this image version is based.</td></tr>
<tr><td><CopyableCode code="container_image" /></td><td><code>string</code></td><td>The image to use for the container that will be materialized for the inference component</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>integer</code></td><td>The version number of the image version.</td></tr>
<tr><td><CopyableCode code="alias" /></td><td><code>string</code></td><td>The alias of the image version.</td></tr>
<tr><td><CopyableCode code="aliases" /></td><td><code>array</code></td><td>List of aliases for the image version.</td></tr>
<tr><td><CopyableCode code="vendor_guidance" /></td><td><code>string</code></td><td>The availability of the image version specified by the maintainer.</td></tr>
<tr><td><CopyableCode code="job_type" /></td><td><code>string</code></td><td>Indicates SageMaker job type compatibility.</td></tr>
<tr><td><CopyableCode code="ml_framework" /></td><td><code>string</code></td><td>The machine learning framework vended in the image version.</td></tr>
<tr><td><CopyableCode code="programming_lang" /></td><td><code>string</code></td><td>The supported programming language and its version.</td></tr>
<tr><td><CopyableCode code="processor" /></td><td><code>string</code></td><td>Indicates CPU or GPU compatibility.</td></tr>
<tr><td><CopyableCode code="horovod" /></td><td><code>boolean</code></td><td>Indicates Horovod compatibility.</td></tr>
<tr><td><CopyableCode code="release_notes" /></td><td><code>string</code></td><td>The maintainer description of the image version.</td></tr>
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
    <td><CopyableCode code="ImageName, BaseImage, region" /></td>
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
Gets all <code>image_versions</code> in a region.
```sql
SELECT
region,
image_name,
image_arn,
image_version_arn,
base_image,
container_image,
version,
alias,
aliases,
vendor_guidance,
job_type,
ml_framework,
programming_lang,
processor,
horovod,
release_notes
FROM aws.sagemaker.image_versions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>image_version</code>.
```sql
SELECT
region,
image_name,
image_arn,
image_version_arn,
base_image,
container_image,
version,
alias,
aliases,
vendor_guidance,
job_type,
ml_framework,
programming_lang,
processor,
horovod,
release_notes
FROM aws.sagemaker.image_versions
WHERE region = 'us-east-1' AND data__Identifier = '<ImageVersionArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>image_version</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.image_versions (
 ImageName,
 BaseImage,
 region
)
SELECT 
'{{ ImageName }}',
 '{{ BaseImage }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.image_versions (
 ImageName,
 BaseImage,
 Alias,
 Aliases,
 VendorGuidance,
 JobType,
 MLFramework,
 ProgrammingLang,
 Processor,
 Horovod,
 ReleaseNotes,
 region
)
SELECT 
 '{{ ImageName }}',
 '{{ BaseImage }}',
 '{{ Alias }}',
 '{{ Aliases }}',
 '{{ VendorGuidance }}',
 '{{ JobType }}',
 '{{ MLFramework }}',
 '{{ ProgrammingLang }}',
 '{{ Processor }}',
 '{{ Horovod }}',
 '{{ ReleaseNotes }}',
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
  - name: image_version
    props:
      - name: ImageName
        value: '{{ ImageName }}'
      - name: BaseImage
        value: '{{ BaseImage }}'
      - name: Alias
        value: '{{ Alias }}'
      - name: Aliases
        value:
          - null
      - name: VendorGuidance
        value: '{{ VendorGuidance }}'
      - name: JobType
        value: '{{ JobType }}'
      - name: MLFramework
        value: '{{ MLFramework }}'
      - name: ProgrammingLang
        value: '{{ ProgrammingLang }}'
      - name: Processor
        value: '{{ Processor }}'
      - name: Horovod
        value: '{{ Horovod }}'
      - name: ReleaseNotes
        value: '{{ ReleaseNotes }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.sagemaker.image_versions
WHERE data__Identifier = '<ImageVersionArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>image_versions</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateImageVersion,
sagemaker:DescribeImageVersion
```

### Read
```json
sagemaker:DescribeImageVersion
```

### Update
```json
sagemaker:UpdateImageVersion,
sagemaker:DescribeImageVersion,
sagemaker:ListAliases
```

### Delete
```json
sagemaker:DeleteImageVersion,
sagemaker:DescribeImageVersion
```

### List
```json
sagemaker:ListImageVersions
```

