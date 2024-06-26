---
title: monitored_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - monitored_resources
  - scom
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
<tr><td><b>Name</b></td><td><code>monitored_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.scom.monitored_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | The properties of a monitored resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instanceName, monitoredResourceName, resourceGroupName, subscriptionId" /> | Retrieve the details of the monitored resource. |
| <CopyableCode code="list_by_managed_instance" /> | `SELECT` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | A comprehensive list of all monitored resources within a SCOM managed instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="instanceName, monitoredResourceName, resourceGroupName, subscriptionId" /> | Create or update a monitored resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instanceName, monitoredResourceName, resourceGroupName, subscriptionId" /> | Delete a monitored resource. |
