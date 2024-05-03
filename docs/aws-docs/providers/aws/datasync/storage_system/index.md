---
title: storage_system
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_system
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

Gets or operates on an individual <code>storage_system</code> resource, use <code>storage_systems</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_system</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::StorageSystem.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.storage_system" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="server_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="server_credentials" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="secrets_manager_arn" /></td><td><code>string</code></td><td>The ARN of a secret stored by AWS Secrets Manager.</td></tr>
<tr><td><CopyableCode code="system_type" /></td><td><code>string</code></td><td>The type of on-premises storage system that DataSync Discovery will analyze.</td></tr>
<tr><td><CopyableCode code="agent_arns" /></td><td><code>array</code></td><td>The ARN of the DataSync agent that connects to and reads from the on-premises storage system's management interface.</td></tr>
<tr><td><CopyableCode code="cloud_watch_log_group_arn" /></td><td><code>string</code></td><td>The ARN of the Amazon CloudWatch log group used to monitor and log discovery job events.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A familiar name for the on-premises storage system.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="storage_system_arn" /></td><td><code>string</code></td><td>The ARN of the on-premises storage system added to DataSync Discovery.</td></tr>
<tr><td><CopyableCode code="connectivity_status" /></td><td><code>string</code></td><td>Indicates whether the DataSync agent can access the on-premises storage system.</td></tr>
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
server_configuration,
server_credentials,
secrets_manager_arn,
system_type,
agent_arns,
cloud_watch_log_group_arn,
name,
tags,
storage_system_arn,
connectivity_status
FROM aws.datasync.storage_system
WHERE data__Identifier = '<StorageSystemArn>';
```

## Permissions

To operate on the <code>storage_system</code> resource, the following permissions are required:

### Read
```json
datasync:DescribeStorageSystem,
datasync:ListTagsForResource,
secretsmanager:DescribeSecret
```

### Update
```json
datasync:UpdateStorageSystem,
datasync:DescribeStorageSystem,
datasync:ListTagsForResource,
datasync:TagResource,
datasync:UntagResource,
secretsmanager:DescribeSecret,
secretsmanager:PutSecretValue
```

### Delete
```json
datasync:DescribeStorageSystem,
datasync:RemoveStorageSystem,
secretsmanager:DescribeSecret,
secretsmanager:DeleteSecret
```

