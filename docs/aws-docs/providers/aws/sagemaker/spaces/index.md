---
title: spaces
hide_title: false
hide_table_of_contents: false
keywords:
  - spaces
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

Creates, updates, deletes or gets a <code>space</code> resource or lists <code>spaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>spaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::Space</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.spaces" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="space_arn" /></td><td><code>string</code></td><td>The space Amazon Resource Name (ARN).</td></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The ID of the associated Domain.</td></tr>
<tr><td><CopyableCode code="space_name" /></td><td><code>string</code></td><td>A name for the Space.</td></tr>
<tr><td><CopyableCode code="space_settings" /></td><td><code>object</code></td><td>A collection of settings.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of tags to apply to the space.</td></tr>
<tr><td><CopyableCode code="ownership_settings" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="space_sharing_settings" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="space_display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="url" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="DomainId, SpaceName, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>spaces</code> in a region.
```sql
SELECT
region,
domain_id,
space_name
FROM aws.sagemaker.spaces
WHERE region = 'us-east-1';
```
Gets all properties from a <code>space</code>.
```sql
SELECT
region,
space_arn,
domain_id,
space_name,
space_settings,
tags,
ownership_settings,
space_sharing_settings,
space_display_name,
url
FROM aws.sagemaker.spaces
WHERE region = 'us-east-1' AND data__Identifier = '<DomainId>|<SpaceName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>space</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.spaces (
 DomainId,
 SpaceName,
 region
)
SELECT 
'{{ DomainId }}',
 '{{ SpaceName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.spaces (
 DomainId,
 SpaceName,
 SpaceSettings,
 Tags,
 OwnershipSettings,
 SpaceSharingSettings,
 SpaceDisplayName,
 region
)
SELECT 
 '{{ DomainId }}',
 '{{ SpaceName }}',
 '{{ SpaceSettings }}',
 '{{ Tags }}',
 '{{ OwnershipSettings }}',
 '{{ SpaceSharingSettings }}',
 '{{ SpaceDisplayName }}',
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
  - name: space
    props:
      - name: DomainId
        value: '{{ DomainId }}'
      - name: SpaceName
        value: '{{ SpaceName }}'
      - name: SpaceSettings
        value:
          JupyterServerAppSettings:
            DefaultResourceSpec:
              InstanceType: '{{ InstanceType }}'
              SageMakerImageArn: '{{ SageMakerImageArn }}'
              SageMakerImageVersionArn: '{{ SageMakerImageVersionArn }}'
          KernelGatewayAppSettings:
            CustomImages:
              - AppImageConfigName: '{{ AppImageConfigName }}'
                ImageName: '{{ ImageName }}'
                ImageVersionNumber: '{{ ImageVersionNumber }}'
            DefaultResourceSpec: null
          JupyterLabAppSettings:
            DefaultResourceSpec: null
            CodeRepositories:
              - RepositoryUrl: '{{ RepositoryUrl }}'
          CodeEditorAppSettings:
            DefaultResourceSpec: null
          SpaceStorageSettings:
            EbsStorageSettings:
              EbsVolumeSizeInGb: '{{ EbsVolumeSizeInGb }}'
          AppType: '{{ AppType }}'
          CustomFileSystems:
            - EFSFileSystem:
                FileSystemId: '{{ FileSystemId }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: OwnershipSettings
        value:
          OwnerUserProfileName: '{{ OwnerUserProfileName }}'
      - name: SpaceSharingSettings
        value:
          SharingType: '{{ SharingType }}'
      - name: SpaceDisplayName
        value: '{{ SpaceDisplayName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.sagemaker.spaces
WHERE data__Identifier = '<DomainId|SpaceName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>spaces</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateSpace,
sagemaker:DescribeSpace
```

### Read
```json
sagemaker:DescribeSpace
```

### Update
```json
sagemaker:UpdateSpace,
sagemaker:DescribeSpace
```

### Delete
```json
sagemaker:DeleteSpace,
sagemaker:DescribeSpace
```

### List
```json
sagemaker:ListSpaces
```

