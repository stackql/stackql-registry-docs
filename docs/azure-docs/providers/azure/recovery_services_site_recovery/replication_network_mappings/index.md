---
title: replication_network_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_network_mappings
  - recovery_services_site_recovery
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
<tr><td><b>Name</b></td><td><code>replication_network_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_network_mappings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Network Mapping Properties. |
| <CopyableCode code="type" /> | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, fabricName, networkMappingName, networkName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of an ASR network mapping. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Lists all ASR network mappings in the vault. |
| <CopyableCode code="list_by_replication_networks" /> | `SELECT` | <CopyableCode code="api-version, fabricName, networkName, resourceGroupName, resourceName, subscriptionId" /> | Lists all ASR network mappings for the specified network. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, fabricName, networkMappingName, networkName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to create an ASR network mapping. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, fabricName, networkMappingName, networkName, resourceGroupName, resourceName, subscriptionId" /> | The operation to delete a network mapping. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, fabricName, networkMappingName, networkName, resourceGroupName, resourceName, subscriptionId" /> | The operation to update an ASR network mapping. |
