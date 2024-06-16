---
title: firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls
  - paloaltonetworks
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloaltonetworks.firewalls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | The properties of the managed service identities assigned to this resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties specific to the Firewall resource deployment. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="firewallName, resourceGroupName, subscriptionId" /> | Get a FirewallResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List FirewallResource resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List FirewallResource resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="firewallName, resourceGroupName, subscriptionId, data__properties" /> | Create a FirewallResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="firewallName, resourceGroupName, subscriptionId" /> | Delete a FirewallResource |
| <CopyableCode code="save_log_profile" /> | `EXEC` | <CopyableCode code="firewallName, resourceGroupName, subscriptionId" /> | Log Profile for Firewall |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="firewallName, resourceGroupName, subscriptionId" /> | Update a FirewallResource |
