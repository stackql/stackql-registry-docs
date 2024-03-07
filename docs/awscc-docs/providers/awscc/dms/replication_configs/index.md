---
title: replication_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_configs
  - dms
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>replication_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>replication_configs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.dms.replication_configs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>replication_config_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Replication Config</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>replication_configs</code> resource, the following permissions are required:

### Create
```json
dms:CreateReplicationConfig,
dms:AddTagsToResource,
dms:ListTagsForResource,
iam:CreateServiceLinkedRole,
iam:AttachRolePolicy,
iam:PutRolePolicy,
iam:UpdateRoleDescription
```

### List
```json
dms:DescribeReplicationConfigs,
dms:ListTagsForResource
```


## Example
```sql
SELECT
region,
replication_config_arn
FROM awscc.dms.replication_configs
WHERE region = 'us-east-1'
```
