---
title: locationf_sx_windows
hide_title: false
hide_table_of_contents: false
keywords:
  - locationf_sx_windows
  - datasync
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

Creates, updates, deletes or gets a <code>locationf_sx_window</code> resource or lists <code>locationf_sx_windows</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locationf_sx_windows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::LocationFSxWindows.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.locationf_sx_windows" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain" /></td><td><code>string</code></td><td>The name of the Windows domain that the FSx for Windows server belongs to.</td></tr>
<tr><td><CopyableCode code="fsx_filesystem_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the FSx for Windows file system.</td></tr>
<tr><td><CopyableCode code="password" /></td><td><code>string</code></td><td>The password of the user who has the permissions to access files and folders in the FSx for Windows file system.</td></tr>
<tr><td><CopyableCode code="security_group_arns" /></td><td><code>array</code></td><td>The ARNs of the security groups that are to use to configure the FSx for Windows file system.</td></tr>
<tr><td><CopyableCode code="subdirectory" /></td><td><code>string</code></td><td>A subdirectory in the location's path.</td></tr>
<tr><td><CopyableCode code="user" /></td><td><code>string</code></td><td>The user who has the permissions to access files and folders in the FSx for Windows file system.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="location_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon FSx for Windows file system location that is created.</td></tr>
<tr><td><CopyableCode code="location_uri" /></td><td><code>string</code></td><td>The URL of the FSx for Windows location that was described.</td></tr>
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
    <td><CopyableCode code="User, SecurityGroupArns, region" /></td>
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
List all <code>locationf_sx_windows</code> in a region.
```sql
SELECT
region,
location_arn
FROM aws.datasync.locationf_sx_windows
WHERE region = 'us-east-1';
```
Gets all properties from a <code>locationf_sx_window</code>.
```sql
SELECT
region,
domain,
fsx_filesystem_arn,
password,
security_group_arns,
subdirectory,
user,
tags,
location_arn,
location_uri
FROM aws.datasync.locationf_sx_windows
WHERE region = 'us-east-1' AND data__Identifier = '<LocationArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>locationf_sx_window</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.datasync.locationf_sx_windows (
 SecurityGroupArns,
 User,
 region
)
SELECT 
'{{ SecurityGroupArns }}',
 '{{ User }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.datasync.locationf_sx_windows (
 Domain,
 FsxFilesystemArn,
 Password,
 SecurityGroupArns,
 Subdirectory,
 User,
 Tags,
 region
)
SELECT 
 '{{ Domain }}',
 '{{ FsxFilesystemArn }}',
 '{{ Password }}',
 '{{ SecurityGroupArns }}',
 '{{ Subdirectory }}',
 '{{ User }}',
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
  - name: locationf_sx_window
    props:
      - name: Domain
        value: '{{ Domain }}'
      - name: FsxFilesystemArn
        value: '{{ FsxFilesystemArn }}'
      - name: Password
        value: '{{ Password }}'
      - name: SecurityGroupArns
        value:
          - '{{ SecurityGroupArns[0] }}'
      - name: Subdirectory
        value: '{{ Subdirectory }}'
      - name: User
        value: '{{ User }}'
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
DELETE FROM aws.datasync.locationf_sx_windows
WHERE data__Identifier = '<LocationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>locationf_sx_windows</code> resource, the following permissions are required:

### Create
```json
datasync:CreateLocationFsxWindows,
datasync:DescribeLocationFsxWindows,
datasync:ListTagsForResource,
datasync:TagResource,
fsx:DescribeFileSystems,
ec2:DescribeNetworkInterfaces,
ec2:DescribeSubnets,
ec2:DescribeSecurityGroups
```

### Read
```json
datasync:DescribeLocationFsxWindows,
datasync:ListTagsForResource
```

### Update
```json
datasync:DescribeLocationFsxWindows,
datasync:ListTagsForResource,
datasync:TagResource,
datasync:UntagResource
```

### Delete
```json
datasync:DeleteLocation
```

### List
```json
datasync:ListLocations
```

