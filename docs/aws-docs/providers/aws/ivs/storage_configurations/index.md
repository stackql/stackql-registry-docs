---
title: storage_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_configurations
  - ivs
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

Creates, updates, deletes or gets a <code>storage_configuration</code> resource or lists <code>storage_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IVS::StorageConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivs.storage_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Storage Configuration ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Storage Configuration Name.</td></tr>
<tr><td><CopyableCode code="s3" /></td><td><code>object</code></td><td>A complex type that describes an S3 location where recorded videos will be stored.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the asset model.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-storageconfiguration.html"><code>AWS::IVS::StorageConfiguration</code></a>.

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
    <td><CopyableCode code="S3, region" /></td>
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
Gets all <code>storage_configurations</code> in a region.
```sql
SELECT
region,
arn,
name,
s3,
tags
FROM aws.ivs.storage_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>storage_configuration</code>.
```sql
SELECT
region,
arn,
name,
s3,
tags
FROM aws.ivs.storage_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>storage_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ivs.storage_configurations (
 S3,
 region
)
SELECT 
'{{ S3 }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ivs.storage_configurations (
 Name,
 S3,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ S3 }}',
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
  - name: storage_configuration
    props:
      - name: Name
        value: '{{ Name }}'
      - name: S3
        value:
          BucketName: '{{ BucketName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ivs.storage_configurations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>storage_configurations</code> resource, the following permissions are required:

### Create
```json
ivs:CreateStorageConfiguration,
ivs:GetStorageConfiguration,
ivs:TagResource,
s3:GetBucketLocation,
s3:GetBucketPolicy,
s3:PutBucketPolicy
```

### Read
```json
ivs:GetStorageConfiguration,
ivs:ListTagsForResource,
s3:GetBucketLocation
```

### Update
```json
ivs:GetStorageConfiguration,
ivs:TagResource,
ivs:UntagResource,
ivs:ListTagsForResource
```

### Delete
```json
ivs:DeleteStorageConfiguration,
ivs:UntagResource,
s3:GetBucketPolicy,
s3:DeleteBucketPolicy,
s3:PutBucketPolicy
```

### List
```json
ivs:ListStorageConfigurations,
s3:GetBucketLocation,
ivs:ListTagsForResource
```
