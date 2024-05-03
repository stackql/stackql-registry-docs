---
title: replication_config
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_config
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>replication_config</code> resource, use <code>replication_configs</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A replication configuration that you later provide to configure and start a AWS DMS Serverless replication</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dms.replication_config" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="replication_config_identifier" /></td><td><code>string</code></td><td>A unique identifier of replication configuration</td></tr>
<tr><td><CopyableCode code="replication_config_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Replication Config</td></tr>
<tr><td><CopyableCode code="source_endpoint_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS Serverless replication configuration</td></tr>
<tr><td><CopyableCode code="target_endpoint_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS Serverless replication configuration</td></tr>
<tr><td><CopyableCode code="replication_type" /></td><td><code>string</code></td><td>The type of AWS DMS Serverless replication to provision using this replication configuration</td></tr>
<tr><td><CopyableCode code="compute_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="replication_settings" /></td><td><code>object</code></td><td>JSON settings for Servereless replications that are provisioned using this replication configuration</td></tr>
<tr><td><CopyableCode code="supplemental_settings" /></td><td><code>object</code></td><td>JSON settings for specifying supplemental data</td></tr>
<tr><td><CopyableCode code="resource_identifier" /></td><td><code>string</code></td><td>A unique value or name that you get set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource</td></tr>
<tr><td><CopyableCode code="table_mappings" /></td><td><code>object</code></td><td>JSON table mappings for AWS DMS Serverless replications that are provisioned using this replication configuration</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>&lt;p&gt;Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.&lt;&#x2F;p&gt;</td></tr>
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
replication_config_identifier,
replication_config_arn,
source_endpoint_arn,
target_endpoint_arn,
replication_type,
compute_config,
replication_settings,
supplemental_settings,
resource_identifier,
table_mappings,
tags
FROM aws.dms.replication_config
WHERE data__Identifier = '<ReplicationConfigArn>';
```

## Permissions

To operate on the <code>replication_config</code> resource, the following permissions are required:

### Read
```json
dms:DescribeReplicationConfigs,
dms:ListTagsForResource
```

### Update
```json
dms:ModifyReplicationConfig,
dms:AddTagsToResource,
dms:RemoveTagsToResource,
dms:ListTagsForResource,
iam:CreateServiceLinkedRole,
iam:AttachRolePolicy,
iam:PutRolePolicy,
iam:UpdateRoleDescription
```

### Delete
```json
dms:DescribeReplicationConfigs,
dms:DeleteReplicationConfig,
dms:ListTagsForResource,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```

