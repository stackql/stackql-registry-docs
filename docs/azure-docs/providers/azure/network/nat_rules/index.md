---
title: nat_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - nat_rules
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
<tr><td><b>Name</b></td><td><code>nat_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.nat_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Parameters for VpnGatewayNatRule. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gatewayName, natRuleName, resourceGroupName, subscriptionId" /> | Retrieves the details of a nat ruleGet. |
| <CopyableCode code="list_by_vpn_gateway" /> | `SELECT` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Retrieves all nat rules for a particular virtual wan vpn gateway. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="gatewayName, natRuleName, resourceGroupName, subscriptionId" /> | Creates a nat rule to a scalable vpn gateway if it doesn't exist else updates the existing nat rules. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="gatewayName, natRuleName, resourceGroupName, subscriptionId" /> | Deletes a nat rule. |
