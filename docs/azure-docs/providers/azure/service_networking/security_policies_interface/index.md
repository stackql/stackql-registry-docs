---
title: security_policies_interface
hide_title: false
hide_table_of_contents: false
keywords:
  - security_policies_interface
  - service_networking
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
<tr><td><b>Name</b></td><td><code>security_policies_interface</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_networking.security_policies_interface" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | SecurityPolicy Properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, securityPolicyName, subscriptionId, trafficControllerName" /> | Get a SecurityPolicy |
| <CopyableCode code="list_by_traffic_controller" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, trafficControllerName" /> | List SecurityPolicy resources by TrafficController |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, securityPolicyName, subscriptionId, trafficControllerName" /> | Create a SecurityPolicy |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, securityPolicyName, subscriptionId, trafficControllerName" /> | Delete a SecurityPolicy |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, securityPolicyName, subscriptionId, trafficControllerName" /> | Update a SecurityPolicy |
