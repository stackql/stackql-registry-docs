---
title: interfaces_effective_network_security_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - interfaces_effective_network_security_groups
  - network
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>interfaces_effective_network_security_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.interfaces_effective_network_security_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="association" /> | `object` | The effective network security group association. |
| <CopyableCode code="effectiveSecurityRules" /> | `array` | A collection of effective security rules. |
| <CopyableCode code="networkSecurityGroup" /> | `object` | Reference to another subresource. |
| <CopyableCode code="tagMap" /> | `string` | Mapping of tags to list of IP Addresses included within the tag. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkInterfaceName, resourceGroupName, subscriptionId" /> |
