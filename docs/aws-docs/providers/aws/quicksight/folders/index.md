---
title: folders
hide_title: false
hide_table_of_contents: false
keywords:
  - folders
  - quicksight
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

Creates, updates, deletes or gets a <code>folder</code> resource or lists <code>folders</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>folders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::Folder Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.folders" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The Amazon Resource Name (ARN) for the folder.</p></td></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td><p>The time that the folder was created.</p></td></tr>
<tr><td><CopyableCode code="folder_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="folder_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td><p>The time that the folder was last updated.</p></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="parent_folder_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="permissions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="sharing_model" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-folder.html"><code>AWS::QuickSight::Folder</code></a>.

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
Gets all <code>folders</code> in a region.
```sql
SELECT
region,
arn,
aws_account_id,
created_time,
folder_id,
folder_type,
last_updated_time,
name,
parent_folder_arn,
permissions,
sharing_model,
tags
FROM aws.quicksight.folders
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>folder</code>.
```sql
SELECT
region,
arn,
aws_account_id,
created_time,
folder_id,
folder_type,
last_updated_time,
name,
parent_folder_arn,
permissions,
sharing_model,
tags
FROM aws.quicksight.folders
WHERE region = 'us-east-1' AND data__Identifier = '<AwsAccountId>|<FolderId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>folder</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.quicksight.folders (
 AwsAccountId,
 FolderId,
 FolderType,
 Name,
 ParentFolderArn,
 Permissions,
 SharingModel,
 Tags,
 region
)
SELECT 
'{{ AwsAccountId }}',
 '{{ FolderId }}',
 '{{ FolderType }}',
 '{{ Name }}',
 '{{ ParentFolderArn }}',
 '{{ Permissions }}',
 '{{ SharingModel }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.quicksight.folders (
 AwsAccountId,
 FolderId,
 FolderType,
 Name,
 ParentFolderArn,
 Permissions,
 SharingModel,
 Tags,
 region
)
SELECT 
 '{{ AwsAccountId }}',
 '{{ FolderId }}',
 '{{ FolderType }}',
 '{{ Name }}',
 '{{ ParentFolderArn }}',
 '{{ Permissions }}',
 '{{ SharingModel }}',
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
  - name: folder
    props:
      - name: AwsAccountId
        value: '{{ AwsAccountId }}'
      - name: FolderId
        value: '{{ FolderId }}'
      - name: FolderType
        value: '{{ FolderType }}'
      - name: Name
        value: '{{ Name }}'
      - name: ParentFolderArn
        value: '{{ ParentFolderArn }}'
      - name: Permissions
        value:
          - Principal: '{{ Principal }}'
            Actions:
              - '{{ Actions[0] }}'
      - name: SharingModel
        value: '{{ SharingModel }}'
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
DELETE FROM aws.quicksight.folders
WHERE data__Identifier = '<AwsAccountId|FolderId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>folders</code> resource, the following permissions are required:

### Read
```json
quicksight:DescribeFolder,
quicksight:DescribeFolderPermissions,
quicksight:ListTagsForResource
```

### Create
```json
quicksight:CreateFolder,
quicksight:DescribeFolder,
quicksight:UpdateFolderPermissions,
quicksight:DescribeFolderPermissions,
quicksight:TagResource,
quicksight:ListTagsForResource
```

### Update
```json
quicksight:DescribeFolder,
quicksight:UpdateFolder,
quicksight:DescribeFolderPermissions,
quicksight:UpdateFolderPermissions,
quicksight:ListTagsForResource,
quicksight:TagResource,
quicksight:UntagResource
```

### Delete
```json
quicksight:DeleteFolder
```

### List
```json
quicksight:ListFolders
```
