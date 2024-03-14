---
title: cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster
  - docdbelastic
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>cluster</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cluster</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.docdbelastic.cluster</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cluster_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cluster_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cluster_endpoint</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>admin_user_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>admin_user_password</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>shard_capacity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>shard_count</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>vpc_security_group_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>subnet_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>preferred_maintenance_window</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>auth_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
cluster_name,
cluster_arn,
cluster_endpoint,
admin_user_name,
admin_user_password,
shard_capacity,
shard_count,
vpc_security_group_ids,
subnet_ids,
preferred_maintenance_window,
kms_key_id,
tags,
auth_type
FROM awscc.docdbelastic.cluster
WHERE data__Identifier = '<ClusterArn>';
```

## Permissions

To operate on the <code>cluster</code> resource, the following permissions are required:

### Read
```json
docdb-elastic:GetCluster,
docdb-elastic:ListTagsForResource
```

### Update
```json
docdb-elastic:UpdateCluster,
docdb-elastic:TagResource,
docdb-elastic:UntagResource,
ec2:CreateVpcEndpoint,
ec2:DescribeVpcEndpoints,
ec2:DeleteVpcEndpoints,
ec2:ModifyVpcEndpoint,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcAttribute,
ec2:DescribeVpcs,
ec2:DescribeAvailabilityZones,
secretsmanager:ListSecrets,
secretsmanager:ListSecretVersionIds,
secretsmanager:DescribeSecret,
secretsmanager:GetSecretValue,
secretsmanager:GetResourcePolicy,
kms:DescribeKey,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```

### Delete
```json
docdb-elastic:DeleteCluster,
ec2:DescribeVpcEndpoints,
ec2:DeleteVpcEndpoints,
ec2:ModifyVpcEndpoint,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcAttribute,
ec2:DescribeVpcs,
ec2:DescribeAvailabilityZones
```

