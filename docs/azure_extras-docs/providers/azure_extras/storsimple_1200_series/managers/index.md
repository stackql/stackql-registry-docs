---
title: managers
hide_title: false
hide_table_of_contents: false
keywords:
  - managers
  - storsimple_1200_series
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>managers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.managers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The Resource Id |
| <CopyableCode code="name" /> | `string` | The Resource Name |
| <CopyableCode code="etag" /> | `string` | ETag of the Manager |
| <CopyableCode code="location" /> | `string` | The Geo location of the Manager |
| <CopyableCode code="properties" /> | `object` | The properties of the Manager |
| <CopyableCode code="tags" /> | `object` | Tags attached to the Manager |
| <CopyableCode code="type" /> | `string` | The Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Returns the properties of the specified manager name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieves all the managers in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieves all the managers in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Creates or updates the manager. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Deletes the manager. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Retrieves all the managers in a subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieves all the managers in a resource group. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Updates the StorSimple Manager. |
| <CopyableCode code="upload_registration_certificate" /> | `EXEC` | <CopyableCode code="certificateName, managerName, resourceGroupName, subscriptionId, data__properties" /> | Upload Vault Cred Certificate.<br />Returns UploadCertificateResponse |
