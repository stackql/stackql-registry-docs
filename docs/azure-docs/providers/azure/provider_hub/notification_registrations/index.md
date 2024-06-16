---
title: notification_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_registrations
  - provider_hub
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
<tr><td><b>Name</b></td><td><code>notification_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.provider_hub.notification_registrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="notificationRegistrationName, providerNamespace, subscriptionId" /> | Gets the notification registration details. |
| <CopyableCode code="list_by_provider_registration" /> | `SELECT` | <CopyableCode code="providerNamespace, subscriptionId" /> | Gets the list of the notification registrations for the given provider. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="notificationRegistrationName, providerNamespace, subscriptionId" /> | Creates or updates a notification registration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="notificationRegistrationName, providerNamespace, subscriptionId" /> | Deletes a notification registration. |
