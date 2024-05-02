---
title: network_interface
hide_title: false
hide_table_of_contents: false
keywords:
  - network_interface
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
Gets or operates on an individual <code>network_interface</code> resource, use <code>network_interfaces</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_interface</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::NetworkInterface resource creates network interface</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.network_interface</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description for the network interface.</td></tr>
<tr><td><code>private_ip_address</code></td><td><code>string</code></td><td>Assigns a single private IP address to the network interface, which is used as the primary private IP address. If you want to specify multiple private IP address, use the PrivateIpAddresses property. </td></tr>
<tr><td><code>private_ip_addresses</code></td><td><code>array</code></td><td>Assigns a list of private IP addresses to the network interface. You can specify a primary private IP address by setting the value of the Primary property to true in the PrivateIpAddressSpecification property. If you want EC2 to automatically assign private IP addresses, use the SecondaryPrivateIpAddressCount property and do not specify this property.</td></tr>
<tr><td><code>secondary_private_ip_address_count</code></td><td><code>integer</code></td><td>The number of secondary private IPv4 addresses to assign to a network interface. When you specify a number of secondary IPv4 addresses, Amazon EC2 selects these IP addresses within the subnet's IPv4 CIDR range. You can't specify this option and specify more than one private IP address using privateIpAddresses</td></tr>
<tr><td><code>primary_private_ip_address</code></td><td><code>string</code></td><td>Returns the primary private IP address of the network interface.</td></tr>
<tr><td><code>ipv4_prefixes</code></td><td><code>array</code></td><td>Assigns a list of IPv4 prefixes to the network interface. If you want EC2 to automatically assign IPv4 prefixes, use the Ipv4PrefixCount property and do not specify this property. Presently, only &#x2F;28 prefixes are supported. You can't specify IPv4 prefixes if you've specified one of the following: a count of IPv4 prefixes, specific private IPv4 addresses, or a count of private IPv4 addresses.</td></tr>
<tr><td><code>ipv4_prefix_count</code></td><td><code>integer</code></td><td>The number of IPv4 prefixes to assign to a network interface. When you specify a number of IPv4 prefixes, Amazon EC2 selects these prefixes from your existing subnet CIDR reservations, if available, or from free spaces in the subnet. By default, these will be &#x2F;28 prefixes. You can't specify a count of IPv4 prefixes if you've specified one of the following: specific IPv4 prefixes, specific private IPv4 addresses, or a count of private IPv4 addresses.</td></tr>
<tr><td><code>group_set</code></td><td><code>array</code></td><td>A list of security group IDs associated with this network interface.</td></tr>
<tr><td><code>ipv6_addresses</code></td><td><code>array</code></td><td>One or more specific IPv6 addresses from the IPv6 CIDR block range of your subnet to associate with the network interface. If you're specifying a number of IPv6 addresses, use the Ipv6AddressCount property and don't specify this property.</td></tr>
<tr><td><code>ipv6_prefixes</code></td><td><code>array</code></td><td>Assigns a list of IPv6 prefixes to the network interface. If you want EC2 to automatically assign IPv6 prefixes, use the Ipv6PrefixCount property and do not specify this property. Presently, only &#x2F;80 prefixes are supported. You can't specify IPv6 prefixes if you've specified one of the following: a count of IPv6 prefixes, specific IPv6 addresses, or a count of IPv6 addresses.</td></tr>
<tr><td><code>ipv6_prefix_count</code></td><td><code>integer</code></td><td>The number of IPv6 prefixes to assign to a network interface. When you specify a number of IPv6 prefixes, Amazon EC2 selects these prefixes from your existing subnet CIDR reservations, if available, or from free spaces in the subnet. By default, these will be &#x2F;80 prefixes. You can't specify a count of IPv6 prefixes if you've specified one of the following: specific IPv6 prefixes, specific IPv6 addresses, or a count of IPv6 addresses.</td></tr>
<tr><td><code>subnet_id</code></td><td><code>string</code></td><td>The ID of the subnet to associate with the network interface.</td></tr>
<tr><td><code>source_dest_check</code></td><td><code>boolean</code></td><td>Indicates whether traffic to or from the instance is validated.</td></tr>
<tr><td><code>interface_type</code></td><td><code>string</code></td><td>Indicates the type of network interface.</td></tr>
<tr><td><code>secondary_private_ip_addresses</code></td><td><code>array</code></td><td>Returns the secondary private IP addresses of the network interface.</td></tr>
<tr><td><code>ipv6_address_count</code></td><td><code>integer</code></td><td>The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. To specify specific IPv6 addresses, use the Ipv6Addresses property and don't specify this property.</td></tr>
<tr><td><code>enable_primary_ipv6</code></td><td><code>boolean</code></td><td>If you have instances or ENIs that rely on the IPv6 address not changing, to avoid disrupting traffic to instances or ENIs, you can enable a primary IPv6 address. Enable this option to automatically assign an IPv6 associated with the ENI attached to your instance to be the primary IPv6 address. When you enable an IPv6 address to be a primary IPv6, you cannot disable it. Traffic will be routed to the primary IPv6 address until the instance is terminated or the ENI is detached. If you have multiple IPv6 addresses associated with an ENI and you enable a primary IPv6 address, the first IPv6 address associated with the ENI becomes the primary IPv6 address.</td></tr>
<tr><td><code>primary_ipv6_address</code></td><td><code>string</code></td><td>The primary IPv6 address</td></tr>
<tr><td><code>connection_tracking_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Network interface id.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this network interface.</td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td>The ID of the VPC</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.ec2.network_interface
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>network_interface</code> resource, the following permissions are required:

### Delete
```json
ec2:DescribeNetworkInterfaces,
ec2:DeleteNetworkInterface
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

