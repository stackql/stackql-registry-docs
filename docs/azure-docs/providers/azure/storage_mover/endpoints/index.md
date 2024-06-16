---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - storage_mover
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
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_mover.endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The resource specific properties for the Storage Mover resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointName, resourceGroupName, storageMoverName, subscriptionId" /> | Gets an Endpoint resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageMoverName, subscriptionId" /> | Lists all Endpoints in a Storage Mover. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="endpointName, resourceGroupName, storageMoverName, subscriptionId, data__properties" /> | Creates or updates an Endpoint resource, which represents a data transfer source or destination. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="endpointName, resourceGroupName, storageMoverName, subscriptionId" /> | Deletes an Endpoint resource. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="endpointName, resourceGroupName, storageMoverName, subscriptionId" /> | Updates properties for an Endpoint resource. Properties not specified in the request body will be unchanged. |
