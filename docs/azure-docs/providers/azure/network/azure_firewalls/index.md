---
title: azure_firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_firewalls
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
<tr><td><b>Name</b></td><td><code>azure_firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.azure_firewalls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of the Azure Firewall. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
| <CopyableCode code="zones" /> | `array` | A list of availability zones denoting where the resource needs to come from. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="azureFirewallName, resourceGroupName, subscriptionId" /> | Gets the specified Azure Firewall. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Azure Firewalls in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="azureFirewallName, resourceGroupName, subscriptionId" /> | Creates or updates the specified Azure Firewall. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="azureFirewallName, resourceGroupName, subscriptionId" /> | Deletes the specified Azure Firewall. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Azure Firewalls in a resource group. |
| <CopyableCode code="packet_capture" /> | `EXEC` | <CopyableCode code="azureFirewallName, resourceGroupName, subscriptionId" /> | Runs a packet capture on AzureFirewall. |
