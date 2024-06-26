---
title: assessments_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - assessments_metadata
  - security
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
<tr><td><b>Name</b></td><td><code>assessments_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.assessments_metadata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Describes properties of an assessment metadata response. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, assessmentMetadataName" /> | Get metadata information on an assessment type |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version" /> | Get metadata information on all assessment types |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | Get metadata information on all assessment types in a specific subscription |
| <CopyableCode code="create_in_subscription" /> | `EXEC` | <CopyableCode code="api-version, assessmentMetadataName, subscriptionId" /> | Create metadata information on an assessment type in a specific subscription |
| <CopyableCode code="delete_in_subscription" /> | `EXEC` | <CopyableCode code="api-version, assessmentMetadataName, subscriptionId" /> | Delete metadata information on an assessment type in a specific subscription, will cause the deletion of all the assessments of that type in that subscription |
| <CopyableCode code="get_in_subscription" /> | `EXEC` | <CopyableCode code="api-version, assessmentMetadataName, subscriptionId" /> | Get metadata information on an assessment type in a specific subscription |
