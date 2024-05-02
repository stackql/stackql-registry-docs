---
title: addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - addresses
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2_api.addresses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `allocationId` | `string` | The ID representing the allocation of the address for use with EC2-VPC. |
| `associationId` | `string` | The ID representing the association of the address with an instance in a VPC. |
| `carrierIp` | `string` | The carrier IP address associated. This option is only available for network interfaces which reside in a subnet in a Wavelength Zone (for example an EC2 instance).  |
| `customerOwnedIp` | `string` | The customer-owned IP address. |
| `customerOwnedIpv4Pool` | `string` | The ID of the customer-owned address pool. |
| `domain` | `string` | Indicates whether this Elastic IP address is for use with instances in EC2-Classic (&lt;code&gt;standard&lt;/code&gt;) or instances in a VPC (&lt;code&gt;vpc&lt;/code&gt;). |
| `instanceId` | `string` | The ID of the instance that the address is associated with (if any). |
| `networkBorderGroup` | `string` | The name of the unique set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses. |
| `networkInterfaceId` | `string` | The ID of the network interface. |
| `networkInterfaceOwnerId` | `string` | The ID of the Amazon Web Services account that owns the network interface. |
| `privateIpAddress` | `string` | The private IP address associated with the Elastic IP address. |
| `publicIp` | `string` | The Elastic IP address. |
| `publicIpv4Pool` | `string` | The ID of an address pool. |
| `tagSet` | `array` | Any tags assigned to the Elastic IP address. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `addresses_Describe` | `SELECT` | `region` |
