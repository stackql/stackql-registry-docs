---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
  - media_services
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
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.assets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The Asset properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, api-version, assetName, resourceGroupName, subscriptionId" /> | Get the details of an Asset in the Media Services account |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | List Assets in the Media Services account with optional filtering and ordering |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, api-version, assetName, resourceGroupName, subscriptionId" /> | Creates or updates an Asset in the Media Services account |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, api-version, assetName, resourceGroupName, subscriptionId" /> | Deletes an Asset in the Media Services account |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | List Assets in the Media Services account with optional filtering and ordering |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, api-version, assetName, resourceGroupName, subscriptionId" /> | Updates an existing Asset in the Media Services account |
