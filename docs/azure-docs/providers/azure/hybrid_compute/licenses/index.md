---
title: licenses
hide_title: false
hide_table_of_contents: false
keywords:
  - licenses
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
<tr><td><b>Name</b></td><td><code>licenses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_compute.licenses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a License Profile. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="licenseName, resourceGroupName, subscriptionId" /> | Retrieves information about the view of a license. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The operation to get all licenses of a non-Azure machine |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The operation to get all licenses of a non-Azure machine |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="licenseName, resourceGroupName, subscriptionId" /> | The operation to create or update a license. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="licenseName, resourceGroupName, subscriptionId" /> | The operation to delete a license. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The operation to get all licenses of a non-Azure machine |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | The operation to get all licenses of a non-Azure machine |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="licenseName, resourceGroupName, subscriptionId" /> | The operation to update a license. |
| <CopyableCode code="validate_license" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | The operation to validate a license. |
