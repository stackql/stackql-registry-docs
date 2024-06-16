---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - desktop_virtualization
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
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.applications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Schema for Application properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationGroupName, applicationName, resourceGroupName, subscriptionId" /> | Get an application. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="applicationGroupName, resourceGroupName, subscriptionId" /> | List applications. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationGroupName, applicationName, resourceGroupName, subscriptionId, data__properties" /> | Create or update an application. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationGroupName, applicationName, resourceGroupName, subscriptionId" /> | Remove an application. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="applicationGroupName, applicationName, resourceGroupName, subscriptionId" /> | Update an application. |
