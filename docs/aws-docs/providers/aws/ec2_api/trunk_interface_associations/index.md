---
title: trunk_interface_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - trunk_interface_associations
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
<tr><td><b>Name</b></td><td><code>trunk_interface_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.trunk_interface_associations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="associationId" /> | `string` | The ID of the association. |
| <CopyableCode code="branchInterfaceId" /> | `string` | The ID of the branch network interface. |
| <CopyableCode code="greKey" /> | `integer` | The application key when you use the GRE protocol. |
| <CopyableCode code="interfaceProtocol" /> | `string` | The interface protocol. Valid values are &lt;code&gt;VLAN&lt;/code&gt; and &lt;code&gt;GRE&lt;/code&gt;. |
| <CopyableCode code="tagSet" /> | `array` | The tags for the trunk interface association. |
| <CopyableCode code="trunkInterfaceId" /> | `string` | The ID of the trunk network interface. |
| <CopyableCode code="vlanId" /> | `integer` | The ID of the VLAN when you use the VLAN protocol. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="trunk_interface_associations_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
