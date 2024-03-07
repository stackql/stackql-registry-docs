---
title: db_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - db_instances
  - rds
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>db_instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>db_instances</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.rds.db_instances</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>d_binstance_identifier</code></td><td><code>string</code></td><td>A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the DB instance. For more information, see &#91;Name Type&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-name.html).&lt;br&#x2F;&gt; For information about constraints that apply to DB instance identifiers, see &#91;Naming constraints in Amazon RDS&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonRDS&#x2F;latest&#x2F;UserGuide&#x2F;CHAP_Limits.html#RDS_Limits.Constraints) in the *Amazon RDS User Guide*.&lt;br&#x2F;&gt;  If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>db_instances</code> resource, the following permissions are required:

### Create
<pre>
ec2:DescribeAccountAttributes,
ec2:DescribeAvailabilityZones,
ec2:DescribeInternetGateways,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcAttribute,
ec2:DescribeVpcs,
iam:CreateServiceLinkedRole,
iam:GetRole,
iam:ListRoles,
iam:PassRole,
kms:CreateGrant,
kms:DescribeKey,
rds:AddRoleToDBInstance,
rds:AddTagsToResource,
rds:CreateDBInstance,
rds:CreateDBInstanceReadReplica,
rds:DescribeDBInstances,
rds:DescribeDBClusters,
rds:DescribeDBClusterSnapshots,
rds:DescribeDBInstanceAutomatedBackups,
rds:DescribeDBSnapshots,
rds:DescribeEvents,
rds:ModifyDBInstance,
rds:RebootDBInstance,
rds:RestoreDBInstanceFromDBSnapshot,
rds:RestoreDBInstanceToPointInTime,
rds:StartDBInstanceAutomatedBackupsReplication,
secretsmanager:CreateSecret,
secretsmanager:TagResource</pre>

### List
<pre>
rds:DescribeDBInstances</pre>


## Example
```sql
SELECT
region,
d_binstance_identifier
FROM awscc.rds.db_instances
WHERE region = 'us-east-1'
```
