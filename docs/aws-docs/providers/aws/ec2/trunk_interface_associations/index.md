---
title: trunk_interface_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - trunk_interface_associations
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
<tr><td><b>Name</b></td><td><code>trunk_interface_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.trunk_interface_associations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `associationId` | `string` | The ID of the association. |
| `branchInterfaceId` | `string` | The ID of the branch network interface. |
| `greKey` | `integer` | The application key when you use the GRE protocol. |
| `interfaceProtocol` | `string` | The interface protocol. Valid values are &lt;code&gt;VLAN&lt;/code&gt; and &lt;code&gt;GRE&lt;/code&gt;. |
| `tagSet` | `array` | The tags for the trunk interface association. |
| `trunkInterfaceId` | `string` | The ID of the trunk network interface. |
| `vlanId` | `integer` | The ID of the VLAN when you use the VLAN protocol. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `trunk_interface_associations_Describe` | `SELECT` | `region` |
