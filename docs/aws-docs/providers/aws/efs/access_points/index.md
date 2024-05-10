---
title: access_points
hide_title: false
hide_table_of_contents: false
keywords:
  - access_points
  - efs
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


Used to retrieve a list of <code>access_points</code> in a region or to create or delete a <code>access_points</code> resource, use <code>access_point</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::EFS::AccessPoint`` resource creates an EFS access point. An access point is an application-specific view into an EFS file system that applies an operating system user and group, and a file system path, to any file system request made through the access point. The operating system user and group override any identity information provided by the NFS client. The file system path is exposed as the access point's root directory. Applications using the access point can only access data in its own directory and below. To learn more, see &#91;Mounting a file system using EFS access points&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;efs&#x2F;latest&#x2F;ug&#x2F;efs-access-points.html).&lt;br&#x2F;&gt; This operation requires permissions for the ``elasticfilesystem:CreateAccessPoint`` action.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.efs.access_points" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="access_point_id" /></td><td><code>string</code></td><td></td></tr>
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
access_point_id
FROM aws.efs.access_points
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>access_point</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- access_point.iql (required properties only)
INSERT INTO aws.efs.access_points (
 FileSystemId,
 region
)
SELECT 
'{{ FileSystemId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- access_point.iql (all properties)
INSERT INTO aws.efs.access_points (
 ClientToken,
 AccessPointTags,
 FileSystemId,
 PosixUser,
 RootDirectory,
 region
)
SELECT 
 '{{ ClientToken }}',
 '{{ AccessPointTags }}',
 '{{ FileSystemId }}',
 '{{ PosixUser }}',
 '{{ RootDirectory }}',
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
  - name: access_point
    props:
      - name: ClientToken
        value: '{{ ClientToken }}'
      - name: AccessPointTags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: FileSystemId
        value: '{{ FileSystemId }}'
      - name: PosixUser
        value:
          Uid: '{{ Uid }}'
          Gid: '{{ Gid }}'
          SecondaryGids:
            - '{{ SecondaryGids[0] }}'
      - name: RootDirectory
        value:
          Path: '{{ Path }}'
          CreationInfo:
            OwnerUid: '{{ OwnerUid }}'
            OwnerGid: '{{ OwnerGid }}'
            Permissions: '{{ Permissions }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.efs.access_points
WHERE data__Identifier = '<AccessPointId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>access_points</code> resource, the following permissions are required:

### Create
```json
elasticfilesystem:CreateAccessPoint,
elasticfilesystem:TagResource,
elasticfilesystem:DescribeAccessPoints
```

### Delete
```json
elasticfilesystem:DeleteAccessPoint,
elasticfilesystem:DescribeAccessPoints
```

### List
```json
elasticfilesystem:DescribeAccessPoints
```

