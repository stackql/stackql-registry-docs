---
title: storage_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_profiles
  - deadline
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

Creates, updates, deletes or gets a <code>storage_profile</code> resource or lists <code>storage_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Deadline::StorageProfile Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.deadline.storage_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="farm_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="file_system_locations" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="os_family" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="storage_profile_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="DisplayName, OsFamily, region" /></td>
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
Gets all <code>storage_profiles</code> in a region.
```sql
SELECT
region,
display_name,
farm_id,
file_system_locations,
os_family,
storage_profile_id
FROM aws.deadline.storage_profiles
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>storage_profile</code>.
```sql
SELECT
region,
display_name,
farm_id,
file_system_locations,
os_family,
storage_profile_id
FROM aws.deadline.storage_profiles
WHERE region = 'us-east-1' AND data__Identifier = '<FarmId>|<StorageProfileId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>storage_profile</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.deadline.storage_profiles (
 DisplayName,
 OsFamily,
 region
)
SELECT 
'{{ DisplayName }}',
 '{{ OsFamily }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.deadline.storage_profiles (
 DisplayName,
 FarmId,
 FileSystemLocations,
 OsFamily,
 region
)
SELECT 
 '{{ DisplayName }}',
 '{{ FarmId }}',
 '{{ FileSystemLocations }}',
 '{{ OsFamily }}',
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
  - name: storage_profile
    props:
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: FarmId
        value: '{{ FarmId }}'
      - name: FileSystemLocations
        value:
          - Name: '{{ Name }}'
            Path: '{{ Path }}'
            Type: '{{ Type }}'
      - name: OsFamily
        value: '{{ OsFamily }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.deadline.storage_profiles
WHERE data__Identifier = '<FarmId|StorageProfileId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>storage_profiles</code> resource, the following permissions are required:

### Create
```json
deadline:CreateStorageProfile,
deadline:GetStorageProfile,
identitystore:ListGroupMembershipsForMember
```

### Read
```json
deadline:GetStorageProfile,
identitystore:ListGroupMembershipsForMember
```

### Update
```json
deadline:UpdateStorageProfile,
deadline:GetStorageProfile,
identitystore:ListGroupMembershipsForMember
```

### Delete
```json
deadline:DeleteStorageProfile,
deadline:GetStorageProfile,
identitystore:ListGroupMembershipsForMember
```

### List
```json
deadline:ListStorageProfiles,
identitystore:ListGroupMembershipsForMember
```

