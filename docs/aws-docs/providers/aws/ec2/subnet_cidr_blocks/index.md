---
title: subnet_cidr_blocks
hide_title: false
hide_table_of_contents: false
keywords:
  - subnet_cidr_blocks
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

Creates, updates, deletes or gets a <code>subnet_cidr_block</code> resource or lists <code>subnet_cidr_blocks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnet_cidr_blocks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::SubnetCidrBlock resource creates association between subnet and IPv6 CIDR</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.subnet_cidr_blocks" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Information about the IPv6 association.</td></tr>
<tr><td><CopyableCode code="ipv6_cidr_block" /></td><td><code>string</code></td><td>The IPv6 network range for the subnet, in CIDR notation. The subnet size must use a /64 prefix length</td></tr>
<tr><td><CopyableCode code="ipv6_ipam_pool_id" /></td><td><code>string</code></td><td>The ID of an IPv6 Amazon VPC IP Address Manager (IPAM) pool from which to allocate, to get the subnet's CIDR</td></tr>
<tr><td><CopyableCode code="ipv6_netmask_length" /></td><td><code>integer</code></td><td>The netmask length of the IPv6 CIDR to allocate to the subnet from an IPAM pool</td></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td>The ID of the subnet</td></tr>
<tr><td><CopyableCode code="ipv6_address_attribute" /></td><td><code>string</code></td><td>The value denoting whether an IPv6 Subnet CIDR Block is public or private.</td></tr>
<tr><td><CopyableCode code="ip_source" /></td><td><code>string</code></td><td>The IP Source of an IPv6 Subnet CIDR Block.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetcidrblock.html"><code>AWS::EC2::SubnetCidrBlock</code></a>.

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
    <td><CopyableCode code="SubnetId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>subnet_cidr_blocks</code> in a region.
```sql
SELECT
region,
id,
ipv6_cidr_block,
ipv6_ipam_pool_id,
ipv6_netmask_length,
subnet_id,
ipv6_address_attribute,
ip_source
FROM aws.ec2.subnet_cidr_blocks
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>subnet_cidr_block</code>.
```sql
SELECT
region,
id,
ipv6_cidr_block,
ipv6_ipam_pool_id,
ipv6_netmask_length,
subnet_id,
ipv6_address_attribute,
ip_source
FROM aws.ec2.subnet_cidr_blocks
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>subnet_cidr_block</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.subnet_cidr_blocks (
 SubnetId,
 region
)
SELECT 
'{{ SubnetId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.subnet_cidr_blocks (
 Ipv6CidrBlock,
 Ipv6IpamPoolId,
 Ipv6NetmaskLength,
 SubnetId,
 region
)
SELECT 
 '{{ Ipv6CidrBlock }}',
 '{{ Ipv6IpamPoolId }}',
 '{{ Ipv6NetmaskLength }}',
 '{{ SubnetId }}',
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
  - name: subnet_cidr_block
    props:
      - name: Ipv6CidrBlock
        value: '{{ Ipv6CidrBlock }}'
      - name: Ipv6IpamPoolId
        value: '{{ Ipv6IpamPoolId }}'
      - name: Ipv6NetmaskLength
        value: '{{ Ipv6NetmaskLength }}'
      - name: SubnetId
        value: '{{ SubnetId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.subnet_cidr_blocks
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>subnet_cidr_blocks</code> resource, the following permissions are required:

### Create
```json
ec2:AssociateSubnetCidrBlock,
ec2:DescribeSubnets
```

### Delete
```json
ec2:DisassociateSubnetCidrBlock,
ec2:DescribeSubnets
```

### List
```json
ec2:DescribeSubnets
```

### Read
```json
ec2:DescribeSubnets
```
