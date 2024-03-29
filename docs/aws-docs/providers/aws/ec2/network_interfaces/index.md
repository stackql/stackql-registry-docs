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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.network_interfaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | A description. |
| `association` | `object` | Describes association information for an Elastic IP address (IPv4 only), or a Carrier IP address (for a network interface which resides in a subnet in a Wavelength Zone). |
| `attachment` | `object` | Describes a network interface attachment. |
| `availabilityZone` | `string` | The Availability Zone. |
| `denyAllIgwTraffic` | `boolean` | Indicates whether a network interface with an IPv6 address is unreachable from the public internet. If the value is &lt;code&gt;true&lt;/code&gt;, inbound traffic from the internet is dropped and you cannot assign an elastic IP address to the network interface. The network interface is reachable from peered VPCs and resources connected through a transit gateway, including on-premises networks. |
| `groupSet` | `array` | Any security groups for the network interface. |
| `interfaceType` | `string` | The type of network interface. |
| `ipv4PrefixSet` | `array` | The IPv4 prefixes that are assigned to the network interface. |
| `ipv6Address` | `string` | The IPv6 globally unique address associated with the network interface. |
| `ipv6AddressesSet` | `array` | The IPv6 addresses associated with the network interface. |
| `ipv6Native` | `boolean` | Indicates whether this is an IPv6 only network interface. |
| `ipv6PrefixSet` | `array` | The IPv6 prefixes that are assigned to the network interface. |
| `macAddress` | `string` | The MAC address. |
| `networkInterfaceId` | `string` | The ID of the network interface. |
| `outpostArn` | `string` | The Amazon Resource Name (ARN) of the Outpost. |
| `ownerId` | `string` | The Amazon Web Services account ID of the owner of the network interface. |
| `privateDnsName` | `string` | The private DNS name. |
| `privateIpAddress` | `string` | The IPv4 address of the network interface within the subnet. |
| `privateIpAddressesSet` | `array` | The private IPv4 addresses associated with the network interface. |
| `requesterId` | `string` | The alias or Amazon Web Services account ID of the principal or service that created the network interface. |
| `requesterManaged` | `boolean` | Indicates whether the network interface is being managed by Amazon Web Services. |
| `sourceDestCheck` | `boolean` | Indicates whether source/destination checking is enabled. |
| `status` | `string` | The status of the network interface. |
| `subnetId` | `string` | The ID of the subnet. |
| `tagSet` | `array` | Any tags assigned to the network interface. |
| `vpcId` | `string` | The ID of the VPC. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `network_interfaces_Describe` | `SELECT` | `region` | Describes one or more of your network interfaces. |
| `network_interface_Create` | `INSERT` | `SubnetId, region` | &lt;p&gt;Creates a network interface in the specified subnet.&lt;/p&gt; &lt;p&gt;For more information about network interfaces, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html"&gt;Elastic Network Interfaces&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `network_interface_Delete` | `DELETE` | `NetworkInterfaceId, region` | Deletes the specified network interface. You must detach the network interface before you can delete it. |
| `network_interface_Attach` | `EXEC` | `DeviceIndex, InstanceId, NetworkInterfaceId, region` | Attaches a network interface to an instance. |
| `network_interface_Detach` | `EXEC` | `AttachmentId, region` | Detaches a network interface from an instance. |
