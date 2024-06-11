---
title: nat_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - nat_gateways
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

Creates, updates, deletes or gets a <code>nat_gateway</code> resource or lists <code>nat_gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nat_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a network address translation (NAT) gateway in the specified subnet. You can create either a public NAT gateway or a private NAT gateway. The default is a public NAT gateway. If you create a public NAT gateway, you must specify an elastic IP address. With a NAT gateway, instances in a private subnet can connect to the internet, other AWS services, or an on-premises network using the IP address of the NAT gateway. For more information, see &#91;NAT gateways&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the *Amazon VPC User Guide*. If you add a default route (<code>AWS::EC2::Route</code> resource) that points to a NAT gateway, specify the NAT gateway ID for the route's <code>NatGatewayId</code> property. When you associate an Elastic IP address or secondary Elastic IP address with a public NAT gateway, the network border group of the Elastic IP address must match the network border group of the Availability Zone (AZ) that the public NAT gateway is in. Otherwise, the NAT gateway fails to launch. You can see the network border group for the AZ by viewing the details of the subnet. Similarly, you can view the network border group for the Elastic IP address by viewing its details. For more information, see &#91;Allocate an Elastic IP address&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html#allocate-eip) in the *Amazon VPC User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.nat_gateways" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="secondary_allocation_ids" /></td><td><code>array</code></td><td>Secondary EIP allocation IDs. For more information, see &#91;Create a NAT gateway&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-creating) in the *Amazon VPC User Guide*.</td></tr>
<tr><td><CopyableCode code="private_ip_address" /></td><td><code>string</code></td><td>The private IPv4 address to assign to the NAT gateway. If you don't provide an address, a private IPv4 address will be automatically assigned.</td></tr>
<tr><td><CopyableCode code="connectivity_type" /></td><td><code>string</code></td><td>Indicates whether the NAT gateway supports public or private connectivity. The default is public connectivity.</td></tr>
<tr><td><CopyableCode code="secondary_private_ip_addresses" /></td><td><code>array</code></td><td>Secondary private IPv4 addresses. For more information about secondary addresses, see &#91;Create a NAT gateway&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-creating) in the *Amazon Virtual Private Cloud User Guide*. <code>SecondaryPrivateIpAddressCount</code> and <code>SecondaryPrivateIpAddresses</code> cannot be set at the same time.</td></tr>
<tr><td><CopyableCode code="secondary_private_ip_address_count" /></td><td><code>integer</code></td><td>&#91;Private NAT gateway only&#93; The number of secondary private IPv4 addresses you want to assign to the NAT gateway. For more information about secondary addresses, see &#91;Create a NAT gateway&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-creating) in the *Amazon Virtual Private Cloud User Guide*. <code>SecondaryPrivateIpAddressCount</code> and <code>SecondaryPrivateIpAddresses</code> cannot be set at the same time.</td></tr>
<tr><td><CopyableCode code="allocation_id" /></td><td><code>string</code></td><td>&#91;Public NAT gateway only&#93; The allocation ID of the Elastic IP address that's associated with the NAT gateway. This property is required for a public NAT gateway and cannot be specified with a private NAT gateway.</td></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td>The ID of the subnet in which the NAT gateway is located.</td></tr>
<tr><td><CopyableCode code="nat_gateway_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags for the NAT gateway.</td></tr>
<tr><td><CopyableCode code="max_drain_duration_seconds" /></td><td><code>integer</code></td><td>The maximum amount of time to wait (in seconds) before forcibly releasing the IP addresses if connections are still in progress. Default value is 350 seconds.</td></tr>
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
    <td><CopyableCode code="SubnetId, region" /></td>
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
List all <code>nat_gateways</code> in a region.
```sql
SELECT
region,
nat_gateway_id
FROM aws.ec2.nat_gateways
WHERE region = 'us-east-1';
```
Gets all properties from a <code>nat_gateway</code>.
```sql
SELECT
region,
secondary_allocation_ids,
private_ip_address,
connectivity_type,
secondary_private_ip_addresses,
secondary_private_ip_address_count,
allocation_id,
subnet_id,
nat_gateway_id,
tags,
max_drain_duration_seconds
FROM aws.ec2.nat_gateways
WHERE region = 'us-east-1' AND data__Identifier = '<NatGatewayId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>nat_gateway</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.nat_gateways (
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
INSERT INTO aws.ec2.nat_gateways (
 SecondaryAllocationIds,
 PrivateIpAddress,
 ConnectivityType,
 SecondaryPrivateIpAddresses,
 SecondaryPrivateIpAddressCount,
 AllocationId,
 SubnetId,
 Tags,
 MaxDrainDurationSeconds,
 region
)
SELECT 
 '{{ SecondaryAllocationIds }}',
 '{{ PrivateIpAddress }}',
 '{{ ConnectivityType }}',
 '{{ SecondaryPrivateIpAddresses }}',
 '{{ SecondaryPrivateIpAddressCount }}',
 '{{ AllocationId }}',
 '{{ SubnetId }}',
 '{{ Tags }}',
 '{{ MaxDrainDurationSeconds }}',
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
  - name: nat_gateway
    props:
      - name: SecondaryAllocationIds
        value:
          - '{{ SecondaryAllocationIds[0] }}'
      - name: PrivateIpAddress
        value: '{{ PrivateIpAddress }}'
      - name: ConnectivityType
        value: '{{ ConnectivityType }}'
      - name: SecondaryPrivateIpAddresses
        value:
          - '{{ SecondaryPrivateIpAddresses[0] }}'
      - name: SecondaryPrivateIpAddressCount
        value: '{{ SecondaryPrivateIpAddressCount }}'
      - name: AllocationId
        value: '{{ AllocationId }}'
      - name: SubnetId
        value: '{{ SubnetId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: MaxDrainDurationSeconds
        value: '{{ MaxDrainDurationSeconds }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.nat_gateways
WHERE data__Identifier = '<NatGatewayId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>nat_gateways</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeNatGateways
```

### Create
```json
ec2:CreateNatGateway,
ec2:DescribeNatGateways,
ec2:CreateTags
```

### Update
```json
ec2:DescribeNatGateways,
ec2:CreateTags,
ec2:DeleteTags,
ec2:AssociateNatGatewayAddress,
ec2:DisassociateNatGatewayAddress,
ec2:AssignPrivateNatGatewayAddress,
ec2:UnassignPrivateNatGatewayAddress
```

### List
```json
ec2:DescribeNatGateways
```

### Delete
```json
ec2:DeleteNatGateway,
ec2:DescribeNatGateways
```

