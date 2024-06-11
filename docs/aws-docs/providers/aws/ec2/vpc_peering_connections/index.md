---
title: vpc_peering_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_peering_connections
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>vpc_peering_connection</code> resource or lists <code>vpc_peering_connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_peering_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPCPeeringConnection</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpc_peering_connections" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="peer_owner_id" /></td><td><code>string</code></td><td>The AWS account ID of the owner of the accepter VPC.</td></tr>
<tr><td><CopyableCode code="peer_region" /></td><td><code>string</code></td><td>The Region code for the accepter VPC, if the accepter VPC is located in a Region other than the Region in which you make the request.</td></tr>
<tr><td><CopyableCode code="peer_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the VPC peer role for the peering connection in another AWS account.</td></tr>
<tr><td><CopyableCode code="peer_vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC with which you are creating the VPC peering connection. You must specify this parameter in the request.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="VpcId, PeerVpcId, region" /></td>
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
List all <code>vpc_peering_connections</code> in a region.
```sql
SELECT
region,
id
FROM aws.ec2.vpc_peering_connections
WHERE region = 'us-east-1';
```
Gets all properties from a <code>vpc_peering_connection</code>.
```sql
SELECT
region,
id,
peer_owner_id,
peer_region,
peer_role_arn,
peer_vpc_id,
vpc_id,
tags
FROM aws.ec2.vpc_peering_connections
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpc_peering_connection</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.vpc_peering_connections (
 PeerVpcId,
 VpcId,
 region
)
SELECT 
'{{ PeerVpcId }}',
 '{{ VpcId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.vpc_peering_connections (
 PeerOwnerId,
 PeerRegion,
 PeerRoleArn,
 PeerVpcId,
 VpcId,
 Tags,
 region
)
SELECT 
 '{{ PeerOwnerId }}',
 '{{ PeerRegion }}',
 '{{ PeerRoleArn }}',
 '{{ PeerVpcId }}',
 '{{ VpcId }}',
 '{{ Tags }}',
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
  - name: vpc_peering_connection
    props:
      - name: PeerOwnerId
        value: '{{ PeerOwnerId }}'
      - name: PeerRegion
        value: '{{ PeerRegion }}'
      - name: PeerRoleArn
        value: '{{ PeerRoleArn }}'
      - name: PeerVpcId
        value: '{{ PeerVpcId }}'
      - name: VpcId
        value: '{{ VpcId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.vpc_peering_connections
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpc_peering_connections</code> resource, the following permissions are required:

### Create
```json
ec2:CreateVpcPeeringConnection,
ec2:DescribeVpcPeeringConnections,
ec2:AcceptVpcPeeringConnection,
ec2:CreateTags,
sts:AssumeRole
```

### Read
```json
ec2:DescribeVpcPeeringConnections
```

### Update
```json
ec2:CreateTags,
ec2:DeleteTags,
ec2:DescribeVpcPeeringConnections
```

### Delete
```json
ec2:DeleteVpcPeeringConnection,
ec2:DescribeVpcPeeringConnections
```

### List
```json
ec2:DescribeVpcPeeringConnections
```

