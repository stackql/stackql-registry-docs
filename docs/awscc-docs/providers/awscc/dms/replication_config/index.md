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
Gets an individual <code>replication_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>replication_config</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.dms.replication_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>replication_config_identifier</code></td><td><code>string</code></td><td>A unique identifier of replication configuration</td></tr>
<tr><td><code>replication_config_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Replication Config</td></tr>
<tr><td><code>source_endpoint_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS Serverless replication configuration</td></tr>
<tr><td><code>target_endpoint_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS Serverless replication configuration</td></tr>
<tr><td><code>replication_type</code></td><td><code>string</code></td><td>The type of AWS DMS Serverless replication to provision using this replication configuration</td></tr>
<tr><td><code>compute_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>replication_settings</code></td><td><code>object</code></td><td>JSON settings for Servereless replications that are provisioned using this replication configuration</td></tr>
<tr><td><code>supplemental_settings</code></td><td><code>object</code></td><td>JSON settings for specifying supplemental data</td></tr>
<tr><td><code>resource_identifier</code></td><td><code>string</code></td><td>A unique value or name that you get set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource</td></tr>
<tr><td><code>table_mappings</code></td><td><code>object</code></td><td>JSON table mappings for AWS DMS Serverless replications that are provisioned using this replication configuration</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>&lt;p&gt;Contains a map of the key-value pairs for the resource tag or tags assigned to the dataset.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.dms.replication_config
WHERE region = 'us-east-1'
AND data__Identifier = '{ReplicationConfigArn}';
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

