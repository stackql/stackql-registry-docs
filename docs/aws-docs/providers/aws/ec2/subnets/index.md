---
title: subnets
hide_title: false
hide_table_of_contents: false
keywords:
  - subnets
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

Creates, updates, deletes or gets a <code>subnet</code> resource or lists <code>subnets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a subnet for the specified VPC. For an IPv4 only subnet, specify an IPv4 CIDR block. If the VPC has an IPv6 CIDR block, you can create an IPv6 only subnet or a dual stack subnet instead. For an IPv6 only subnet, specify an IPv6 CIDR block. For a dual stack subnet, specify both an IPv4 CIDR block and an IPv6 CIDR block. For more information, see &#91;Subnets for your VPC&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html) in the *Amazon VPC User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.subnets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="assign_ipv6_address_on_creation" /></td><td><code>boolean</code></td><td>Indicates whether a network interface created in this subnet receives an IPv6 address. The default value is <code>false</code>. If you specify <code>AssignIpv6AddressOnCreation</code>, you must also specify an IPv6 CIDR block.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC the subnet is in. If you update this property, you must also update the <code>CidrBlock</code> property.</td></tr>
<tr><td><CopyableCode code="map_public_ip_on_launch" /></td><td><code>boolean</code></td><td>Indicates whether instances launched in this subnet receive a public IPv4 address. The default value is <code>false</code>. AWS charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the *Public IPv4 Address* tab on the &#91;VPC pricing page&#93;(https://docs.aws.amazon.com/vpc/pricing/).</td></tr>
<tr><td><CopyableCode code="enable_lni_at_device_index" /></td><td><code>integer</code></td><td>Indicates the device position for local network interfaces in this subnet. For example, <code>1</code> indicates local network interfaces in this subnet are the secondary network interface (eth1).</td></tr>
<tr><td><CopyableCode code="network_acl_association_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="availability_zone" /></td><td><code>string</code></td><td>The Availability Zone of the subnet. If you update this property, you must also update the <code>CidrBlock</code> property.</td></tr>
<tr><td><CopyableCode code="availability_zone_id" /></td><td><code>string</code></td><td>The AZ ID of the subnet.</td></tr>
<tr><td><CopyableCode code="cidr_block" /></td><td><code>string</code></td><td>The IPv4 CIDR block assigned to the subnet. If you update this property, we create a new subnet, and then delete the existing one.</td></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ipv6_cidr_blocks" /></td><td><code>array</code></td><td>The IPv6 network ranges for the subnet, in CIDR notation.</td></tr>
<tr><td><CopyableCode code="ipv6_cidr_block" /></td><td><code>string</code></td><td>The IPv6 CIDR block. If you specify <code>AssignIpv6AddressOnCreation</code>, you must also specify an IPv6 CIDR block.</td></tr>
<tr><td><CopyableCode code="outpost_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Outpost.</td></tr>
<tr><td><CopyableCode code="ipv6_native" /></td><td><code>boolean</code></td><td>Indicates whether this is an IPv6 only subnet. For more information, see &#91;Subnet basics&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#subnet-basics) in the *User Guide*.</td></tr>
<tr><td><CopyableCode code="enable_dns64" /></td><td><code>boolean</code></td><td>Indicates whether DNS queries made to the Amazon-provided DNS Resolver in this subnet should return synthetic IPv6 addresses for IPv4-only destinations. For more information, see &#91;DNS64 and NAT64&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-nat64-dns64) in the *User Guide*.</td></tr>
<tr><td><CopyableCode code="private_dns_name_options_on_launch" /></td><td><code>object</code></td><td>The hostname type for EC2 instances launched into this subnet and how DNS A and AAAA record queries to the instances should be handled. For more information, see &#91;Amazon EC2 instance hostname types&#93;(https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *User Guide*. Available options: + EnableResourceNameDnsAAAARecord (true | false) + EnableResourceNameDnsARecord (true | false) + HostnameType (ip-name | resource-name)</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Any tags assigned to the subnet.</td></tr>
<tr><td><CopyableCode code="ipv4_ipam_pool_id" /></td><td><code>string</code></td><td>An IPv4 IPAM pool ID for the subnet.</td></tr>
<tr><td><CopyableCode code="ipv4_netmask_length" /></td><td><code>integer</code></td><td>An IPv4 netmask length for the subnet.</td></tr>
<tr><td><CopyableCode code="ipv6_ipam_pool_id" /></td><td><code>string</code></td><td>An IPv6 IPAM pool ID for the subnet.</td></tr>
<tr><td><CopyableCode code="ipv6_netmask_length" /></td><td><code>integer</code></td><td>An IPv6 netmask length for the subnet.</td></tr>
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
List all <code>subnets</code> in a region.
```sql
SELECT
region,
subnet_id
FROM aws.ec2.subnets
WHERE region = 'us-east-1';
```
Gets all properties from a <code>subnet</code>.
```sql
SELECT
region,
assign_ipv6_address_on_creation,
vpc_id,
map_public_ip_on_launch,
enable_lni_at_device_index,
network_acl_association_id,
availability_zone,
availability_zone_id,
cidr_block,
subnet_id,
ipv6_cidr_blocks,
ipv6_cidr_block,
outpost_arn,
ipv6_native,
enable_dns64,
private_dns_name_options_on_launch,
tags,
ipv4_ipam_pool_id,
ipv4_netmask_length,
ipv6_ipam_pool_id,
ipv6_netmask_length
FROM aws.ec2.subnets
WHERE region = 'us-east-1' AND data__Identifier = '<SubnetId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>subnet</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.subnets (
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
INSERT INTO aws.ec2.subnets (
 AssignIpv6AddressOnCreation,
 VpcId,
 MapPublicIpOnLaunch,
 EnableLniAtDeviceIndex,
 AvailabilityZone,
 AvailabilityZoneId,
 CidrBlock,
 Ipv6CidrBlocks,
 Ipv6CidrBlock,
 OutpostArn,
 Ipv6Native,
 EnableDns64,
 PrivateDnsNameOptionsOnLaunch,
 Tags,
 Ipv4IpamPoolId,
 Ipv4NetmaskLength,
 Ipv6IpamPoolId,
 Ipv6NetmaskLength,
 region
)
SELECT 
 '{{ AssignIpv6AddressOnCreation }}',
 '{{ VpcId }}',
 '{{ MapPublicIpOnLaunch }}',
 '{{ EnableLniAtDeviceIndex }}',
 '{{ AvailabilityZone }}',
 '{{ AvailabilityZoneId }}',
 '{{ CidrBlock }}',
 '{{ Ipv6CidrBlocks }}',
 '{{ Ipv6CidrBlock }}',
 '{{ OutpostArn }}',
 '{{ Ipv6Native }}',
 '{{ EnableDns64 }}',
 '{{ PrivateDnsNameOptionsOnLaunch }}',
 '{{ Tags }}',
 '{{ Ipv4IpamPoolId }}',
 '{{ Ipv4NetmaskLength }}',
 '{{ Ipv6IpamPoolId }}',
 '{{ Ipv6NetmaskLength }}',
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
  - name: subnet
    props:
      - name: AssignIpv6AddressOnCreation
        value: '{{ AssignIpv6AddressOnCreation }}'
      - name: VpcId
        value: '{{ VpcId }}'
      - name: MapPublicIpOnLaunch
        value: '{{ MapPublicIpOnLaunch }}'
      - name: EnableLniAtDeviceIndex
        value: '{{ EnableLniAtDeviceIndex }}'
      - name: AvailabilityZone
        value: '{{ AvailabilityZone }}'
      - name: AvailabilityZoneId
        value: '{{ AvailabilityZoneId }}'
      - name: CidrBlock
        value: '{{ CidrBlock }}'
      - name: Ipv6CidrBlocks
        value:
          - '{{ Ipv6CidrBlocks[0] }}'
      - name: Ipv6CidrBlock
        value: '{{ Ipv6CidrBlock }}'
      - name: OutpostArn
        value: '{{ OutpostArn }}'
      - name: Ipv6Native
        value: '{{ Ipv6Native }}'
      - name: EnableDns64
        value: '{{ EnableDns64 }}'
      - name: PrivateDnsNameOptionsOnLaunch
        value:
          HostnameType: '{{ HostnameType }}'
          EnableResourceNameDnsARecord: '{{ EnableResourceNameDnsARecord }}'
          EnableResourceNameDnsAAAARecord: '{{ EnableResourceNameDnsAAAARecord }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Ipv4IpamPoolId
        value: '{{ Ipv4IpamPoolId }}'
      - name: Ipv4NetmaskLength
        value: '{{ Ipv4NetmaskLength }}'
      - name: Ipv6IpamPoolId
        value: '{{ Ipv6IpamPoolId }}'
      - name: Ipv6NetmaskLength
        value: '{{ Ipv6NetmaskLength }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.subnets
WHERE data__Identifier = '<SubnetId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>subnets</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeSubnets,
ec2:CreateSubnet,
ec2:CreateTags,
ec2:ModifySubnetAttribute
```

### Read
```json
ec2:DescribeSubnets,
ec2:DescribeNetworkAcls
```

### Update
```json
ec2:DescribeSubnets,
ec2:ModifySubnetAttribute,
ec2:CreateTags,
ec2:DeleteTags,
ec2:AssociateSubnetCidrBlock,
ec2:DisassociateSubnetCidrBlock
```

### Delete
```json
ec2:DescribeSubnets,
ec2:DeleteSubnet
```

### List
```json
ec2:DescribeSubnets,
ec2:DescribeNetworkAcls
```

