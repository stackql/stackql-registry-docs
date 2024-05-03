---
title: storage_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_profile
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

Gets or operates on an individual <code>storage_profile</code> resource, use <code>storage_profiles</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Deadline::StorageProfile Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.deadline.storage_profile" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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

## `SELECT` Example
```sql
SELECT
region,
display_name,
farm_id,
file_system_locations,
os_family,
storage_profile_id
FROM aws.deadline.storage_profile
WHERE data__Identifier = '<FarmId>|<StorageProfileId>';
```

## Permissions

To operate on the <code>storage_profile</code> resource, the following permissions are required:

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

