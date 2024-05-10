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


Used to retrieve a list of <code>vpc_peering_connections</code> in a region or to create or delete a <code>vpc_peering_connections</code> resource, use <code>vpc_peering_connection</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_peering_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPCPeeringConnection</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpc_peering_connections" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id
FROM aws.ec2.vpc_peering_connections
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "PeerVpcId": "{{ PeerVpcId }}",
 "VpcId": "{{ VpcId }}"
}
>>>
--required properties only
INSERT INTO aws.ec2.vpc_peering_connections (
 PeerVpcId,
 VpcId,
 region
)
SELECT 
{{ PeerVpcId }},
 {{ VpcId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "PeerOwnerId": "{{ PeerOwnerId }}",
 "PeerRegion": "{{ PeerRegion }}",
 "PeerRoleArn": "{{ PeerRoleArn }}",
 "PeerVpcId": "{{ PeerVpcId }}",
 "VpcId": "{{ VpcId }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
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
 {{ PeerOwnerId }},
 {{ PeerRegion }},
 {{ PeerRoleArn }},
 {{ PeerVpcId }},
 {{ VpcId }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
ec2:DeleteVpcPeeringConnection,
ec2:DescribeVpcPeeringConnections
```

### List
```json
ec2:DescribeVpcPeeringConnections
```

