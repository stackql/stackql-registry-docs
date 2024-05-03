---
title: containers
hide_title: false
hide_table_of_contents: false
keywords:
  - containers
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
<tr><td><b>Name</b></td><td><code>containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.fluid_relay.containers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a Fluid Relay Container resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fluidRelayContainerName, fluidRelayServerName, resourceGroup, subscriptionId" /> |
| <CopyableCode code="list_by_fluid_relay_servers" /> | `SELECT` | <CopyableCode code="fluidRelayServerName, resourceGroup, subscriptionId" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fluidRelayContainerName, fluidRelayServerName, resourceGroup, subscriptionId" /> |
| <CopyableCode code="_list_by_fluid_relay_servers" /> | `EXEC` | <CopyableCode code="fluidRelayServerName, resourceGroup, subscriptionId" /> |
