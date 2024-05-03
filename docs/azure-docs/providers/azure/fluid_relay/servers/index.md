---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - fluid_relay
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
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.fluid_relay.servers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of a Fluid Relay Service resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fluidRelayServerName, resourceGroup, subscriptionId" /> |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroup, subscriptionId" /> |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="fluidRelayServerName, resourceGroup, subscriptionId" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fluidRelayServerName, resourceGroup, subscriptionId" /> |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroup, subscriptionId" /> |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="fluidRelayServerName, resourceGroup, subscriptionId, data__keyName" /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="fluidRelayServerName, resourceGroup, subscriptionId" /> |
