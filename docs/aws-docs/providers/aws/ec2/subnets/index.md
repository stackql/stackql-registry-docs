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


Used to retrieve a list of <code>subnets</code> in a region or to create or delete a <code>subnets</code> resource, use <code>subnet</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a subnet for the specified VPC.&lt;br&#x2F;&gt; For an IPv4 only subnet, specify an IPv4 CIDR block. If the VPC has an IPv6 CIDR block, you can create an IPv6 only subnet or a dual stack subnet instead. For an IPv6 only subnet, specify an IPv6 CIDR block. For a dual stack subnet, specify both an IPv4 CIDR block and an IPv6 CIDR block.&lt;br&#x2F;&gt; For more information, see &#91;Subnets for your VPC&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;vpc&#x2F;latest&#x2F;userguide&#x2F;configure-subnets.html) in the *Amazon VPC User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.subnets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td></td></tr>
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
subnet_id
FROM aws.ec2.subnets
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- subnet.iql (required properties only)
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
-- subnet.iql (all properties)
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

## `DELETE` Example

```sql
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

