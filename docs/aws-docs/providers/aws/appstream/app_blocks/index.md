---
title: app_blocks
hide_title: false
hide_table_of_contents: false
keywords:
  - app_blocks
  - appstream
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

Creates, updates, deletes or gets an <code>app_block</code> resource or lists <code>app_blocks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_blocks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppStream::AppBlock</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appstream.app_blocks" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source_s3_location" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="setup_script_details" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="packaging_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="post_setup_script_details" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="Name, SourceS3Location, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from an individual <code>app_block</code>.
```sql
SELECT
region,
name,
arn,
description,
display_name,
source_s3_location,
setup_script_details,
tags,
created_time,
packaging_type,
post_setup_script_details
FROM aws.appstream.app_blocks
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>app_block</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.appstream.app_blocks (
 Name,
 SourceS3Location,
 region
)
SELECT 
'{{ Name }}',
 '{{ SourceS3Location }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.appstream.app_blocks (
 Name,
 Description,
 DisplayName,
 SourceS3Location,
 SetupScriptDetails,
 Tags,
 PackagingType,
 PostSetupScriptDetails,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ DisplayName }}',
 '{{ SourceS3Location }}',
 '{{ SetupScriptDetails }}',
 '{{ Tags }}',
 '{{ PackagingType }}',
 '{{ PostSetupScriptDetails }}',
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
  - name: app_block
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: SourceS3Location
        value:
          S3Bucket: '{{ S3Bucket }}'
          S3Key: '{{ S3Key }}'
      - name: SetupScriptDetails
        value:
          ScriptS3Location: null
          ExecutablePath: '{{ ExecutablePath }}'
          ExecutableParameters: '{{ ExecutableParameters }}'
          TimeoutInSeconds: '{{ TimeoutInSeconds }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: PackagingType
        value: '{{ PackagingType }}'
      - name: PostSetupScriptDetails
        value: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.appstream.app_blocks
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>app_blocks</code> resource, the following permissions are required:

### Create
```json
appstream:CreateAppBlock,
appstream:TagResource,
s3:GetObject,
s3:ListBucket,
s3:GetBucketOwnershipControls
```

### Read
```json
appstream:DescribeAppBlocks
```

### Delete
```json
appstream:DeleteAppBlock
```

