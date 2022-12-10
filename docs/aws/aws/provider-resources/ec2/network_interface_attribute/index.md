---
title: network_interface_attribute
hide_title: false
hide_table_of_contents: false
keywords:
  - network_interface_attribute
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_interface_attribute</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.network_interface_attribute</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `object` | Describes a value for a resource attribute that is a String. |
| `networkInterfaceId` | `string` | The ID of the network interface. |
| `sourceDestCheck` | `object` | Describes a value for a resource attribute that is a Boolean value. |
| `attachment` | `object` | Describes a network interface attachment. |
| `groupSet` | `array` | The security groups associated with the network interface. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `network_interface_attribute_Describe` | `SELECT` | `NetworkInterfaceId` | Describes a network interface attribute. You can specify only one attribute at a time. |
| `network_interface_attribute_Modify` | `EXEC` | `NetworkInterfaceId` | Modifies the specified network interface attribute. You can specify only one attribute at a time. You can use this action to attach and detach security groups from an existing EC2 instance. |
| `network_interface_attribute_Reset` | `EXEC` | `NetworkInterfaceId` | Resets a network interface attribute. You can specify only one attribute at a time. |
