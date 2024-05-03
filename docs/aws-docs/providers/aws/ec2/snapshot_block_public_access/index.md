---
title: snapshot_block_public_access
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshot_block_public_access
  - ec2
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

Gets or operates on an individual <code>snapshot_block_public_access</code> resource, use <code>snapshot_block_public_accesses</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshot_block_public_access</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::SnapshotBlockPublicAccess</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.snapshot_block_public_access" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of EBS Snapshot Block Public Access.</td></tr>
<tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>The identifier for the specified AWS account.</td></tr>
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
state,
account_id
FROM aws.ec2.snapshot_block_public_access
WHERE data__Identifier = '<AccountId>';
```

## Permissions

To operate on the <code>snapshot_block_public_access</code> resource, the following permissions are required:

### Read
```json
ec2:GetSnapshotBlockPublicAccessState
```

### Update
```json
ec2:EnableSnapshotBlockPublicAccess,
ec2:GetSnapshotBlockPublicAccessState
```

### Delete
```json
ec2:DisableSnapshotBlockPublicAccess,
ec2:GetSnapshotBlockPublicAccessState
```
