---
title: storage_systems
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_systems
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
Retrieves a list of <code>storage_systems</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_systems</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>storage_systems</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.datasync.storage_systems</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>storage_system_arn</code></td><td><code>string</code></td><td>The ARN of the on-premises storage system added to DataSync Discovery.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
storage_system_arn
FROM awscc.datasync.storage_systems
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>storage_systems</code> resource, the following permissions are required:

### Create
```json
datasync:AddStorageSystem,
datasync:DescribeStorageSystem,
datasync:ListTagsForResource,
datasync:TagResource,
secretsmanager:CreateSecret,
secretsmanager:DescribeSecret,
iam:CreateServiceLinkedRole
```

### List
```json
datasync:ListStorageSystems
```

