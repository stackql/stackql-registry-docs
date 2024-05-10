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


Used to retrieve a list of <code>app_blocks</code> in a region or to create or delete a <code>app_blocks</code> resource, use <code>app_block</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_blocks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppStream::AppBlock</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appstream.app_blocks" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>undefined</code></td><td></td></tr>
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
FROM aws.appstream.app_blocks
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>app_block</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- app_block.iql (required properties only)
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
-- app_block.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
appstream:DeleteAppBlock
```

