---
title: snapshot_block_public_accesses
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshot_block_public_accesses
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

Used to retrieve a list of <code>snapshot_block_public_accesses</code> in a region or create a <code>snapshot_block_public_accesses</code> resource, use <code>snapshot_block_public_access</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshot_block_public_accesses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::SnapshotBlockPublicAccess</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.snapshot_block_public_accesses" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
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
account_id
FROM aws.ec2.snapshot_block_public_accesses
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>snapshot_block_public_accesses</code> resource, the following permissions are required:

### Create
```json
ec2:EnableSnapshotBlockPublicAccess,
ec2:GetSnapshotBlockPublicAccessState
```

### List
```json
ec2:GetSnapshotBlockPublicAccessState
```

