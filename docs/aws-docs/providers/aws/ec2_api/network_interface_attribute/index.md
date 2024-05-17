---
title: network_interface_attribute
hide_title: false
hide_table_of_contents: false
keywords:
  - network_interface_attribute
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
<tr><td><b>Name</b></td><td><code>network_interface_attribute</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.network_interface_attribute" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `object` | Describes a value for a resource attribute that is a String. |
| <CopyableCode code="attachment" /> | `object` | Describes a network interface attachment. |
| <CopyableCode code="groupSet" /> | `array` | The security groups associated with the network interface. |
| <CopyableCode code="networkInterfaceId" /> | `string` | The ID of the network interface. |
| <CopyableCode code="sourceDestCheck" /> | `object` | Describes a value for a resource attribute that is a Boolean value. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="network_interface_attribute_Describe" /> | `SELECT` | <CopyableCode code="NetworkInterfaceId, region" /> | Describes a network interface attribute. You can specify only one attribute at a time. |
| <CopyableCode code="network_interface_attribute_Modify" /> | `EXEC` | <CopyableCode code="NetworkInterfaceId, region" /> | Modifies the specified network interface attribute. You can specify only one attribute at a time. You can use this action to attach and detach security groups from an existing EC2 instance. |
| <CopyableCode code="network_interface_attribute_Reset" /> | `EXEC` | <CopyableCode code="NetworkInterfaceId, region" /> | Resets a network interface attribute. You can specify only one attribute at a time. |
