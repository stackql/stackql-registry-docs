---
title: network_interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - network_interfaces
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

Creates, updates, deletes or gets a <code>network_interface</code> resource or lists <code>network_interfaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::NetworkInterface resource creates network interface</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.network_interfaces" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the network interface.</td></tr>
<tr><td><CopyableCode code="private_ip_address" /></td><td><code>string</code></td><td>Assigns a single private IP address to the network interface, which is used as the primary private IP address. If you want to specify multiple private IP address, use the PrivateIpAddresses property. </td></tr>
<tr><td><CopyableCode code="private_ip_addresses" /></td><td><code>array</code></td><td>Assigns a list of private IP addresses to the network interface. You can specify a primary private IP address by setting the value of the Primary property to true in the PrivateIpAddressSpecification property. If you want EC2 to automatically assign private IP addresses, use the SecondaryPrivateIpAddressCount property and do not specify this property.</td></tr>
<tr><td><CopyableCode code="secondary_private_ip_address_count" /></td><td><code>integer</code></td><td>The number of secondary private IPv4 addresses to assign to a network interface. When you specify a number of secondary IPv4 addresses, Amazon EC2 selects these IP addresses within the subnet's IPv4 CIDR range. You can't specify this option and specify more than one private IP address using privateIpAddresses</td></tr>
<tr><td><CopyableCode code="primary_private_ip_address" /></td><td><code>string</code></td><td>Returns the primary private IP address of the network interface.</td></tr>
<tr><td><CopyableCode code="ipv4_prefixes" /></td><td><code>array</code></td><td>Assigns a list of IPv4 prefixes to the network interface. If you want EC2 to automatically assign IPv4 prefixes, use the Ipv4PrefixCount property and do not specify this property. Presently, only /28 prefixes are supported. You can't specify IPv4 prefixes if you've specified one of the following: a count of IPv4 prefixes, specific private IPv4 addresses, or a count of private IPv4 addresses.</td></tr>
<tr><td><CopyableCode code="ipv4_prefix_count" /></td><td><code>integer</code></td><td>The number of IPv4 prefixes to assign to a network interface. When you specify a number of IPv4 prefixes, Amazon EC2 selects these prefixes from your existing subnet CIDR reservations, if available, or from free spaces in the subnet. By default, these will be /28 prefixes. You can't specify a count of IPv4 prefixes if you've specified one of the following: specific IPv4 prefixes, specific private IPv4 addresses, or a count of private IPv4 addresses.</td></tr>
<tr><td><CopyableCode code="group_set" /></td><td><code>array</code></td><td>A list of security group IDs associated with this network interface.</td></tr>
<tr><td><CopyableCode code="ipv6_addresses" /></td><td><code>array</code></td><td>One or more specific IPv6 addresses from the IPv6 CIDR block range of your subnet to associate with the network interface. If you're specifying a number of IPv6 addresses, use the Ipv6AddressCount property and don't specify this property.</td></tr>
<tr><td><CopyableCode code="ipv6_prefixes" /></td><td><code>array</code></td><td>Assigns a list of IPv6 prefixes to the network interface. If you want EC2 to automatically assign IPv6 prefixes, use the Ipv6PrefixCount property and do not specify this property. Presently, only /80 prefixes are supported. You can't specify IPv6 prefixes if you've specified one of the following: a count of IPv6 prefixes, specific IPv6 addresses, or a count of IPv6 addresses.</td></tr>
<tr><td><CopyableCode code="ipv6_prefix_count" /></td><td><code>integer</code></td><td>The number of IPv6 prefixes to assign to a network interface. When you specify a number of IPv6 prefixes, Amazon EC2 selects these prefixes from your existing subnet CIDR reservations, if available, or from free spaces in the subnet. By default, these will be /80 prefixes. You can't specify a count of IPv6 prefixes if you've specified one of the following: specific IPv6 prefixes, specific IPv6 addresses, or a count of IPv6 addresses.</td></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td>The ID of the subnet to associate with the network interface.</td></tr>
<tr><td><CopyableCode code="source_dest_check" /></td><td><code>boolean</code></td><td>Indicates whether traffic to or from the instance is validated.</td></tr>
<tr><td><CopyableCode code="interface_type" /></td><td><code>string</code></td><td>Indicates the type of network interface.</td></tr>
<tr><td><CopyableCode code="secondary_private_ip_addresses" /></td><td><code>array</code></td><td>Returns the secondary private IP addresses of the network interface.</td></tr>
<tr><td><CopyableCode code="ipv6_address_count" /></td><td><code>integer</code></td><td>The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. To specify specific IPv6 addresses, use the Ipv6Addresses property and don't specify this property.</td></tr>
<tr><td><CopyableCode code="enable_primary_ipv6" /></td><td><code>boolean</code></td><td>If you have instances or ENIs that rely on the IPv6 address not changing, to avoid disrupting traffic to instances or ENIs, you can enable a primary IPv6 address. Enable this option to automatically assign an IPv6 associated with the ENI attached to your instance to be the primary IPv6 address. When you enable an IPv6 address to be a primary IPv6, you cannot disable it. Traffic will be routed to the primary IPv6 address until the instance is terminated or the ENI is detached. If you have multiple IPv6 addresses associated with an ENI and you enable a primary IPv6 address, the first IPv6 address associated with the ENI becomes the primary IPv6 address.</td></tr>
<tr><td><CopyableCode code="primary_ipv6_address" /></td><td><code>string</code></td><td>The primary IPv6 address</td></tr>
<tr><td><CopyableCode code="connection_tracking_specification" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Network interface id.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this network interface.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC</td></tr>
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
List all <code>network_interfaces</code> in a region.
```sql
SELECT
region,
id
FROM aws.ec2.network_interfaces
WHERE region = 'us-east-1';
```
Gets all properties from a <code>network_interface</code>.
```sql
SELECT
region,
description,
private_ip_address,
private_ip_addresses,
secondary_private_ip_address_count,
primary_private_ip_address,
ipv4_prefixes,
ipv4_prefix_count,
group_set,
ipv6_addresses,
ipv6_prefixes,
ipv6_prefix_count,
subnet_id,
source_dest_check,
interface_type,
secondary_private_ip_addresses,
ipv6_address_count,
enable_primary_ipv6,
primary_ipv6_address,
connection_tracking_specification,
id,
tags,
vpc_id
FROM aws.ec2.network_interfaces
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_interface</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.network_interfaces (
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
INSERT INTO aws.ec2.network_interfaces (
 Description,
 PrivateIpAddress,
 PrivateIpAddresses,
 SecondaryPrivateIpAddressCount,
 Ipv4Prefixes,
 Ipv4PrefixCount,
 GroupSet,
 Ipv6Addresses,
 Ipv6Prefixes,
 Ipv6PrefixCount,
 SubnetId,
 SourceDestCheck,
 InterfaceType,
 Ipv6AddressCount,
 EnablePrimaryIpv6,
 ConnectionTrackingSpecification,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ PrivateIpAddress }}',
 '{{ PrivateIpAddresses }}',
 '{{ SecondaryPrivateIpAddressCount }}',
 '{{ Ipv4Prefixes }}',
 '{{ Ipv4PrefixCount }}',
 '{{ GroupSet }}',
 '{{ Ipv6Addresses }}',
 '{{ Ipv6Prefixes }}',
 '{{ Ipv6PrefixCount }}',
 '{{ SubnetId }}',
 '{{ SourceDestCheck }}',
 '{{ InterfaceType }}',
 '{{ Ipv6AddressCount }}',
 '{{ EnablePrimaryIpv6 }}',
 '{{ ConnectionTrackingSpecification }}',
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
  - name: network_interface
    props:
      - name: Description
        value: '{{ Description }}'
      - name: PrivateIpAddress
        value: '{{ PrivateIpAddress }}'
      - name: PrivateIpAddresses
        value:
          - Primary: '{{ Primary }}'
            PrivateIpAddress: '{{ PrivateIpAddress }}'
      - name: SecondaryPrivateIpAddressCount
        value: '{{ SecondaryPrivateIpAddressCount }}'
      - name: Ipv4Prefixes
        value:
          - Ipv4Prefix: '{{ Ipv4Prefix }}'
      - name: Ipv4PrefixCount
        value: '{{ Ipv4PrefixCount }}'
      - name: GroupSet
        value:
          - '{{ GroupSet[0] }}'
      - name: Ipv6Addresses
        value:
          - Ipv6Address: '{{ Ipv6Address }}'
      - name: Ipv6Prefixes
        value:
          - Ipv6Prefix: '{{ Ipv6Prefix }}'
      - name: Ipv6PrefixCount
        value: '{{ Ipv6PrefixCount }}'
      - name: SubnetId
        value: '{{ SubnetId }}'
      - name: SourceDestCheck
        value: '{{ SourceDestCheck }}'
      - name: InterfaceType
        value: '{{ InterfaceType }}'
      - name: Ipv6AddressCount
        value: '{{ Ipv6AddressCount }}'
      - name: EnablePrimaryIpv6
        value: '{{ EnablePrimaryIpv6 }}'
      - name: ConnectionTrackingSpecification
        value:
          TcpEstablishedTimeout: '{{ TcpEstablishedTimeout }}'
          UdpStreamTimeout: '{{ UdpStreamTimeout }}'
          UdpTimeout: '{{ UdpTimeout }}'
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
DELETE FROM aws.ec2.network_interfaces
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>network_interfaces</code> resource, the following permissions are required:

### Create
```json
ec2:CreateNetworkInterface,
ec2:DescribeNetworkInterfaces,
ec2:CreateTags,
ec2:ModifyNetworkInterfaceAttribute
```

### Delete
```json
ec2:DescribeNetworkInterfaces,
ec2:DeleteNetworkInterface
```

### List
```json
ec2:DescribeNetworkInterfaces
```

### Read
```json
ec2:DescribeNetworkInterfaces
```

### Update
```json
ec2:DescribeNetworkInterfaces,
ec2:ModifyNetworkInterfaceAttribute,
ec2:UnassignIpv6Addresses,
ec2:AssignIpv6Addresses,
ec2:DeleteTags,
ec2:CreateTags,
ec2:UnassignPrivateIpAddresses,
ec2:AssignPrivateIpAddresses
```

