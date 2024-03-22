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
Retrieves a list of <code>snapshot_block_public_accesses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshot_block_public_accesses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>snapshot_block_public_accesses</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.snapshot_block_public_accesses</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>account_id</code></td><td><code>string</code></td><td>The identifier for the specified AWS account.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
account_id
FROM awscc.ec2.snapshot_block_public_accesses
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

