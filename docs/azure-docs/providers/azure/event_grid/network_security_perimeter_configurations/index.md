---
title: network_security_perimeter_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - network_security_perimeter_configurations
  - event_grid
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
<tr><td><b>Name</b></td><td><code>network_security_perimeter_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.network_security_perimeter_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified identifier of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="properties" /> | `object` | Network security perimeter configuration information to reflect latest association and nsp profile configuration. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="associationName, perimeterGuid, resourceGroupName, resourceName, resourceType, subscriptionId" /> | Get a specific network security perimeter configuration with a topic or domain. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, resourceType, subscriptionId" /> | Get all network security perimeter configurations associated with a topic or domain. |
| <CopyableCode code="reconcile" /> | `EXEC` | <CopyableCode code="associationName, perimeterGuid, resourceGroupName, resourceName, resourceType, subscriptionId" /> | Reconcile a specific network security perimeter configuration for a given network security perimeter association with a topic or domain. |
