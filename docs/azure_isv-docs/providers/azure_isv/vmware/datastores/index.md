---
title: datastores
hide_title: false
hide_table_of_contents: false
keywords:
  - datastores
  - vmware
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>datastores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware.datastores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | The properties of a datastore |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, datastoreName, privateCloudName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, privateCloudName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, datastoreName, privateCloudName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, datastoreName, privateCloudName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="clusterName, privateCloudName, resourceGroupName, subscriptionId" /> |
