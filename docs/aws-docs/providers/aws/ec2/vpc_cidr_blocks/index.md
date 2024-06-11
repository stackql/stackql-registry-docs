---
title: vpc_cidr_blocks
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_cidr_blocks
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

Creates, updates, deletes or gets a <code>vpc_cidr_block</code> resource or lists <code>vpc_cidr_blocks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_cidr_blocks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPCCidrBlock</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpc_cidr_blocks" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cidr_block" /></td><td><code>string</code></td><td>An IPv4 CIDR block to associate with the VPC.</td></tr>
<tr><td><CopyableCode code="ipv6_pool" /></td><td><code>string</code></td><td>The ID of an IPv6 address pool from which to allocate the IPv6 CIDR block.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The Id of the VPC associated CIDR Block.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC.</td></tr>
<tr><td><CopyableCode code="ipv6_cidr_block" /></td><td><code>string</code></td><td>An IPv6 CIDR block from the IPv6 address pool.</td></tr>
<tr><td><CopyableCode code="ipv4_ipam_pool_id" /></td><td><code>string</code></td><td>The ID of the IPv4 IPAM pool to Associate a CIDR from to a VPC.</td></tr>
<tr><td><CopyableCode code="ipv4_netmask_length" /></td><td><code>integer</code></td><td>The netmask length of the IPv4 CIDR you would like to associate from an Amazon VPC IP Address Manager (IPAM) pool.</td></tr>
<tr><td><CopyableCode code="ipv6_ipam_pool_id" /></td><td><code>string</code></td><td>The ID of the IPv6 IPAM pool to Associate a CIDR from to a VPC.</td></tr>
<tr><td><CopyableCode code="ipv6_netmask_length" /></td><td><code>integer</code></td><td>The netmask length of the IPv6 CIDR you would like to associate from an Amazon VPC IP Address Manager (IPAM) pool.</td></tr>
<tr><td><CopyableCode code="amazon_provided_ipv6_cidr_block" /></td><td><code>boolean</code></td><td>Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IPv6 addresses, or the size of the CIDR block.</td></tr>
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
    <td><CopyableCode code="VpcId, region" /></td>
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
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>vpc_cidr_blocks</code> in a region.
```sql
SELECT
region,
id,
vpc_id
FROM aws.ec2.vpc_cidr_blocks
WHERE region = 'us-east-1';
```
Gets all properties from a <code>vpc_cidr_block</code>.
```sql
SELECT
region,
cidr_block,
ipv6_pool,
id,
vpc_id,
ipv6_cidr_block,
ipv4_ipam_pool_id,
ipv4_netmask_length,
ipv6_ipam_pool_id,
ipv6_netmask_length,
amazon_provided_ipv6_cidr_block
FROM aws.ec2.vpc_cidr_blocks
WHERE region = 'us-east-1' AND data__Identifier = '<Id>|<VpcId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpc_cidr_block</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.vpc_cidr_blocks (
 VpcId,
 region
)
SELECT 
'{{ VpcId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.vpc_cidr_blocks (
 CidrBlock,
 Ipv6Pool,
 VpcId,
 Ipv6CidrBlock,
 Ipv4IpamPoolId,
 Ipv4NetmaskLength,
 Ipv6IpamPoolId,
 Ipv6NetmaskLength,
 AmazonProvidedIpv6CidrBlock,
 region
)
SELECT 
 '{{ CidrBlock }}',
 '{{ Ipv6Pool }}',
 '{{ VpcId }}',
 '{{ Ipv6CidrBlock }}',
 '{{ Ipv4IpamPoolId }}',
 '{{ Ipv4NetmaskLength }}',
 '{{ Ipv6IpamPoolId }}',
 '{{ Ipv6NetmaskLength }}',
 '{{ AmazonProvidedIpv6CidrBlock }}',
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
  - name: vpc_cidr_block
    props:
      - name: CidrBlock
        value: '{{ CidrBlock }}'
      - name: Ipv6Pool
        value: '{{ Ipv6Pool }}'
      - name: VpcId
        value: '{{ VpcId }}'
      - name: Ipv6CidrBlock
        value: '{{ Ipv6CidrBlock }}'
      - name: Ipv4IpamPoolId
        value: '{{ Ipv4IpamPoolId }}'
      - name: Ipv4NetmaskLength
        value: '{{ Ipv4NetmaskLength }}'
      - name: Ipv6IpamPoolId
        value: '{{ Ipv6IpamPoolId }}'
      - name: Ipv6NetmaskLength
        value: '{{ Ipv6NetmaskLength }}'
      - name: AmazonProvidedIpv6CidrBlock
        value: '{{ AmazonProvidedIpv6CidrBlock }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.vpc_cidr_blocks
WHERE data__Identifier = '<Id|VpcId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpc_cidr_blocks</code> resource, the following permissions are required:

### Create
```json
ec2:AssociateVpcCidrBlock,
ec2:DescribeVpcs,
ec2:AllocateIpamPoolCidr
```

### Read
```json
ec2:DescribeVpcs
```

### Delete
```json
ec2:DescribeVpcs,
ec2:DisassociateVpcCidrBlock
```

### List
```json
ec2:DescribeVpcs
```

