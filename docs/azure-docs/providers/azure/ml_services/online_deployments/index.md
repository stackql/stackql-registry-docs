---
title: online_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - online_deployments
  - ml_services
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
<tr><td><b>Name</b></td><td><code>online_deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.online_deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="kind" /> | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deploymentName, endpointName, resourceGroupName, subscriptionId, workspaceName" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="endpointName, resourceGroupName, subscriptionId, workspaceName" /> |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deploymentName, endpointName, resourceGroupName, subscriptionId, workspaceName, data__location, data__properties" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deploymentName, endpointName, resourceGroupName, subscriptionId, workspaceName" /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="deploymentName, endpointName, resourceGroupName, subscriptionId, workspaceName" /> |
