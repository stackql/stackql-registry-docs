---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>cluster</code> resource or lists <code>clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::DocDBElastic::Cluster Amazon DocumentDB (with MongoDB compatibility) Elastic Scale resource describes a Cluster</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.docdbelastic.clusters" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="cluster_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="cluster_endpoint" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="admin_user_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="admin_user_password" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="shard_capacity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="shard_count" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_security_group_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="preferred_maintenance_window" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="preferred_backup_window" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="backup_retention_period" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="shard_instance_count" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="auth_type" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="ClusterName, AdminUserName, ShardCapacity, ShardCount, AuthType, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>clusters</code> in a region.
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
preferred_backup_window,
backup_retention_period,
shard_instance_count,
kms_key_id,
tags,
auth_type
FROM aws.docdbelastic.clusters
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>cluster</code>.
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
preferred_backup_window,
backup_retention_period,
shard_instance_count,
kms_key_id,
tags,
auth_type
FROM aws.docdbelastic.clusters
WHERE region = 'us-east-1' AND data__Identifier = '<ClusterArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cluster</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.docdbelastic.clusters (
 ClusterName,
 AdminUserName,
 ShardCapacity,
 ShardCount,
 AuthType,
 region
)
SELECT 
'{{ ClusterName }}',
 '{{ AdminUserName }}',
 '{{ ShardCapacity }}',
 '{{ ShardCount }}',
 '{{ AuthType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.docdbelastic.clusters (
 ClusterName,
 AdminUserName,
 AdminUserPassword,
 ShardCapacity,
 ShardCount,
 VpcSecurityGroupIds,
 SubnetIds,
 PreferredMaintenanceWindow,
 PreferredBackupWindow,
 BackupRetentionPeriod,
 ShardInstanceCount,
 KmsKeyId,
 Tags,
 AuthType,
 region
)
SELECT 
 '{{ ClusterName }}',
 '{{ AdminUserName }}',
 '{{ AdminUserPassword }}',
 '{{ ShardCapacity }}',
 '{{ ShardCount }}',
 '{{ VpcSecurityGroupIds }}',
 '{{ SubnetIds }}',
 '{{ PreferredMaintenanceWindow }}',
 '{{ PreferredBackupWindow }}',
 '{{ BackupRetentionPeriod }}',
 '{{ ShardInstanceCount }}',
 '{{ KmsKeyId }}',
 '{{ Tags }}',
 '{{ AuthType }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: cluster
    props:
      - name: ClusterName
        value: '{{ ClusterName }}'
      - name: AdminUserName
        value: '{{ AdminUserName }}'
      - name: AdminUserPassword
        value: '{{ AdminUserPassword }}'
      - name: ShardCapacity
        value: '{{ ShardCapacity }}'
      - name: ShardCount
        value: '{{ ShardCount }}'
      - name: VpcSecurityGroupIds
        value:
          - '{{ VpcSecurityGroupIds[0] }}'
      - name: SubnetIds
        value:
          - '{{ SubnetIds[0] }}'
      - name: PreferredMaintenanceWindow
        value: '{{ PreferredMaintenanceWindow }}'
      - name: PreferredBackupWindow
        value: '{{ PreferredBackupWindow }}'
      - name: BackupRetentionPeriod
        value: '{{ BackupRetentionPeriod }}'
      - name: ShardInstanceCount
        value: '{{ ShardInstanceCount }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: AuthType
        value: '{{ AuthType }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.docdbelastic.clusters
WHERE data__Identifier = '<ClusterArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>clusters</code> resource, the following permissions are required:

### Create
```json
docdb-elastic:CreateCluster,
docdb-elastic:TagResource,
docdb-elastic:GetCluster,
docdb-elastic:ListTagsForResource,
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
kms:Decrypt,
iam:CreateServiceLinkedRole
```

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
docdb-elastic:GetCluster,
docdb-elastic:ListTagsForResource,
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
docdb-elastic:GetCluster,
ec2:DescribeVpcEndpoints,
ec2:DeleteVpcEndpoints,
ec2:ModifyVpcEndpoint,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcAttribute,
ec2:DescribeVpcs,
ec2:DescribeAvailabilityZones
```

### List
```json
docdb-elastic:ListClusters
```

