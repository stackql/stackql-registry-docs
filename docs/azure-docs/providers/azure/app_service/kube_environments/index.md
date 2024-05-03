---
title: kube_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - kube_environments
  - app_service
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
<tr><td><b>Name</b></td><td><code>kube_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.kube_environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="extendedLocation" /> | `object` | Extended Location. |
| <CopyableCode code="properties" /> | `object` | KubeEnvironment resource specific properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Get the properties of a Kubernetes Environment. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Description for Get all the Kubernetes Environments in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Description for Get all Kubernetes Environments for a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Creates or updates a Kubernetes Environment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Delete a Kubernetes Environment. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Description for Get all the Kubernetes Environments in a resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Description for Get all Kubernetes Environments for a subscription. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Creates or updates a Kubernetes Environment. |
