---
title: network_security_perimeter_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - network_security_perimeter_configurations
  - hybrid_compute
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_compute.network_security_perimeter_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="properties" /> | `object` | Properties that define a Network Security Perimeter resource. |
| <CopyableCode code="type" /> | `string` | Azure resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_private_link_scope" /> | `SELECT` | <CopyableCode code="resourceGroupName, scopeName, subscriptionId" /> | Lists the network security perimeter configurations for a private link scope. |
| <CopyableCode code="_list_by_private_link_scope" /> | `EXEC` | <CopyableCode code="resourceGroupName, scopeName, subscriptionId" /> | Lists the network security perimeter configurations for a private link scope. |
| <CopyableCode code="get_by_private_link_scope" /> | `EXEC` | <CopyableCode code="perimeterName, resourceGroupName, scopeName, subscriptionId" /> | Gets the network security perimeter configuration for a private link scope. |
| <CopyableCode code="reconcile_for_private_link_scope" /> | `EXEC` | <CopyableCode code="perimeterName, resourceGroupName, scopeName, subscriptionId" /> | Forces the network security perimeter configuration to refresh for a private link scope. |
