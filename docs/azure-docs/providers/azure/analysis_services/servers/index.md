---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - analysis_services
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.analysis_services.servers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | An identifier that represents the Analysis Services resource. |
| <CopyableCode code="name" /> | `string` | The name of the Analysis Services resource. |
| <CopyableCode code="location" /> | `string` | Location of the Analysis Services resource. |
| <CopyableCode code="properties" /> | `object` | Properties of Analysis Services resource. |
| <CopyableCode code="sku" /> | `object` | Represents the SKU name and Azure pricing tier for Analysis Services resource. |
| <CopyableCode code="tags" /> | `object` | Key-value pairs of additional resource provisioning properties. |
| <CopyableCode code="type" /> | `string` | The type of the Analysis Services resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the Analysis Services servers for the given subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the Analysis Services servers for the given resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Provisions the specified Analysis Services server based on the configuration specified in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Deletes the specified Analysis Services server. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Check the name availability in the target location. |
| <CopyableCode code="dissociate_gateway" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Dissociates a Unified Gateway associated with the server. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Resumes operation of the specified Analysis Services server instance. |
| <CopyableCode code="suspend" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Suspends operation of the specified Analysis Services server instance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Updates the current state of the specified Analysis Services server. |
