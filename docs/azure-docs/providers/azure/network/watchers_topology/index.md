---
title: watchers_topology
hide_title: false
hide_table_of_contents: false
keywords:
  - watchers_topology
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
<tr><td><b>Name</b></td><td><code>watchers_topology</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.watchers_topology" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | GUID representing the operation id. |
| <CopyableCode code="createdDateTime" /> | `string` | The datetime when the topology was initially created for the resource group. |
| <CopyableCode code="lastModified" /> | `string` | The datetime when the topology was last modified. |
| <CopyableCode code="resources" /> | `array` | A list of topology resources. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId" /> |
