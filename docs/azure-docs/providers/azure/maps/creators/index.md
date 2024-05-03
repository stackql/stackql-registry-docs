---
title: creators
hide_title: false
hide_table_of_contents: false
keywords:
  - creators
  - maps
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
<tr><td><b>Name</b></td><td><code>creators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maps.creators" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Creator resource properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, creatorName, resourceGroupName, subscriptionId" /> | Get a Maps Creator resource. |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Get all Creator instances for an Azure Maps Account |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, creatorName, resourceGroupName, subscriptionId, data__properties" /> | Create or update a Maps Creator resource. Creator resource will manage Azure resources required to populate a custom set of mapping data. It requires an account to exist before it can be created. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, creatorName, resourceGroupName, subscriptionId" /> | Delete a Maps Creator resource. |
| <CopyableCode code="_list_by_account" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Get all Creator instances for an Azure Maps Account |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, creatorName, resourceGroupName, subscriptionId" /> | Updates the Maps Creator resource. Only a subset of the parameters may be updated after creation, such as Tags. |
