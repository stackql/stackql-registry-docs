---
title: network_interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - network_interfaces
  - ec2_api
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.network_interfaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | A description. |
| <CopyableCode code="association" /> | `object` | Describes association information for an Elastic IP address (IPv4 only), or a Carrier IP address (for a network interface which resides in a subnet in a Wavelength Zone). |
| <CopyableCode code="attachment" /> | `object` | Describes a network interface attachment. |
| <CopyableCode code="availabilityZone" /> | `string` | The Availability Zone. |
| <CopyableCode code="denyAllIgwTraffic" /> | `boolean` | Indicates whether a network interface with an IPv6 address is unreachable from the public internet. If the value is &lt;code&gt;true&lt;/code&gt;, inbound traffic from the internet is dropped and you cannot assign an elastic IP address to the network interface. The network interface is reachable from peered VPCs and resources connected through a transit gateway, including on-premises networks. |
| <CopyableCode code="groupSet" /> | `array` | Any security groups for the network interface. |
| <CopyableCode code="interfaceType" /> | `string` | The type of network interface. |
| <CopyableCode code="ipv4PrefixSet" /> | `array` | The IPv4 prefixes that are assigned to the network interface. |
| <CopyableCode code="ipv6Address" /> | `string` | The IPv6 globally unique address associated with the network interface. |
| <CopyableCode code="ipv6AddressesSet" /> | `array` | The IPv6 addresses associated with the network interface. |
| <CopyableCode code="ipv6Native" /> | `boolean` | Indicates whether this is an IPv6 only network interface. |
| <CopyableCode code="ipv6PrefixSet" /> | `array` | The IPv6 prefixes that are assigned to the network interface. |
| <CopyableCode code="macAddress" /> | `string` | The MAC address. |
| <CopyableCode code="networkInterfaceId" /> | `string` | The ID of the network interface. |
| <CopyableCode code="outpostArn" /> | `string` | The Amazon Resource Name (ARN) of the Outpost. |
| <CopyableCode code="ownerId" /> | `string` | The Amazon Web Services account ID of the owner of the network interface. |
| <CopyableCode code="privateDnsName" /> | `string` | The private DNS name. |
| <CopyableCode code="privateIpAddress" /> | `string` | The IPv4 address of the network interface within the subnet. |
| <CopyableCode code="privateIpAddressesSet" /> | `array` | The private IPv4 addresses associated with the network interface. |
| <CopyableCode code="requesterId" /> | `string` | The alias or Amazon Web Services account ID of the principal or service that created the network interface. |
| <CopyableCode code="requesterManaged" /> | `boolean` | Indicates whether the network interface is being managed by Amazon Web Services. |
| <CopyableCode code="sourceDestCheck" /> | `boolean` | Indicates whether source/destination checking is enabled. |
| <CopyableCode code="status" /> | `string` | The status of the network interface. |
| <CopyableCode code="subnetId" /> | `string` | The ID of the subnet. |
| <CopyableCode code="tagSet" /> | `array` | Any tags assigned to the network interface. |
| <CopyableCode code="vpcId" /> | `string` | The ID of the VPC. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="network_interfaces_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes one or more of your network interfaces. |
| <CopyableCode code="network_interface_Create" /> | `INSERT` | <CopyableCode code="SubnetId, region" /> | &lt;p&gt;Creates a network interface in the specified subnet.&lt;/p&gt; &lt;p&gt;For more information about network interfaces, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html"&gt;Elastic Network Interfaces&lt;/a&gt; in the &lt;i&gt;Amazon Virtual Private Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| <CopyableCode code="network_interface_Delete" /> | `DELETE` | <CopyableCode code="NetworkInterfaceId, region" /> | Deletes the specified network interface. You must detach the network interface before you can delete it. |
| <CopyableCode code="network_interface_Attach" /> | `EXEC` | <CopyableCode code="DeviceIndex, InstanceId, NetworkInterfaceId, region" /> | Attaches a network interface to an instance. |
| <CopyableCode code="network_interface_Detach" /> | `EXEC` | <CopyableCode code="AttachmentId, region" /> | Detaches a network interface from an instance. |
