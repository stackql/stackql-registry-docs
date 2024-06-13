---
title: vpc_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_connections
  - msk
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

Creates, updates, deletes or gets a <code>vpc_connection</code> resource or lists <code>vpc_connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MSK::VpcConnection</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.msk.vpc_connections" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="authentication" /></td><td><code>string</code></td><td>The type of private link authentication</td></tr>
<tr><td><CopyableCode code="client_subnets" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="target_cluster_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the target cluster</td></tr>
<tr><td><CopyableCode code="security_groups" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="Authentication, ClientSubnets, SecurityGroups, TargetClusterArn, VpcId, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>vpc_connections</code> in a region.
```sql
SELECT
region,
arn
FROM aws.msk.vpc_connections
WHERE region = 'us-east-1';
```
Gets all properties from a <code>vpc_connection</code>.
```sql
SELECT
region,
arn,
authentication,
client_subnets,
target_cluster_arn,
security_groups,
tags,
vpc_id
FROM aws.msk.vpc_connections
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpc_connection</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.msk.vpc_connections (
 Authentication,
 ClientSubnets,
 TargetClusterArn,
 SecurityGroups,
 VpcId,
 region
)
SELECT 
'{{ Authentication }}',
 '{{ ClientSubnets }}',
 '{{ TargetClusterArn }}',
 '{{ SecurityGroups }}',
 '{{ VpcId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.msk.vpc_connections (
 Authentication,
 ClientSubnets,
 TargetClusterArn,
 SecurityGroups,
 Tags,
 VpcId,
 region
)
SELECT 
 '{{ Authentication }}',
 '{{ ClientSubnets }}',
 '{{ TargetClusterArn }}',
 '{{ SecurityGroups }}',
 '{{ Tags }}',
 '{{ VpcId }}',
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
  - name: vpc_connection
    props:
      - name: Authentication
        value: '{{ Authentication }}'
      - name: ClientSubnets
        value:
          - '{{ ClientSubnets[0] }}'
      - name: TargetClusterArn
        value: '{{ TargetClusterArn }}'
      - name: SecurityGroups
        value:
          - '{{ SecurityGroups[0] }}'
      - name: Tags
        value: {}
      - name: VpcId
        value: '{{ VpcId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.msk.vpc_connections
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpc_connections</code> resource, the following permissions are required:

### Create
```json
ec2:CreateVpcEndpoint,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcAttribute,
ec2:DescribeVpcs,
ec2:DescribeVpcEndpoints,
ec2:AcceptVpcEndpointConnections,
ec2:RejectVpcEndpointConnections,
ec2:DescribeVpcEndpointConnections,
ec2:CreateTags,
iam:AttachRolePolicy,
iam:CreateServiceLinkedRole,
iam:PutRolePolicy,
kafka:CreateVpcConnection,
kafka:DescribeVpcConnection,
kafka:TagResource,
kms:CreateGrant,
kms:DescribeKey
```

### Read
```json
kafka:DescribeVpcConnection,
kms:CreateGrant,
kms:DescribeKey
```

### Update
```json
kafka:DescribeVpcConnection,
kms:CreateGrant,
kms:DescribeKey,
kafka:TagResource,
kafka:UntagResource
```

### Delete
```json
ec2:DeleteVpcEndpoint,
ec2:DeleteVpcEndpoints,
ec2:DescribeVpcEndpoints,
ec2:DescribeVpcEndpointConnections,
kafka:DeleteVpcConnection,
kafka:DescribeVpcConnection,
kms:CreateGrant,
kms:DescribeKey
```

### List
```json
kafka:ListVpcConnections,
kms:CreateGrant,
kms:DescribeKey
```

