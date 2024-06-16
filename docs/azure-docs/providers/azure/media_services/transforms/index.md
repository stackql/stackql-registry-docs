---
title: transforms
hide_title: false
hide_table_of_contents: false
keywords:
  - transforms
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
<tr><td><b>Name</b></td><td><code>transforms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.transforms" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A Transform. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId, transformName" /> | Gets a Transform. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | Lists the Transforms in the account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId, transformName" /> | Creates or updates a new Transform. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId, transformName" /> | Deletes a Transform. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId, transformName" /> | Updates a Transform. |
