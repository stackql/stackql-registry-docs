---
title: secret
hide_title: false
hide_table_of_contents: false
keywords:
  - secret
  - service_fabric_mesh
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
<tr><td><b>Name</b></td><td><code>secret</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_mesh.secret" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a secret resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, secretResourceName, subscriptionId" /> | Gets the information about the secret resource with the given name. The information include the description and other properties of the secret. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Gets the information about all secret resources in a given resource group. The information include the description and other properties of the Secret. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | Gets the information about all secret resources in a given resource group. The information include the description and other properties of the secret. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, resourceGroupName, secretResourceName, subscriptionId, data__properties" /> | Creates a secret resource with the specified name, description and properties. If a secret resource with the same name exists, then it is updated with the specified description and properties. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, resourceGroupName, secretResourceName, subscriptionId" /> | Deletes the secret resource identified by the name. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Gets the information about all secret resources in a given resource group. The information include the description and other properties of the Secret. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> | Gets the information about all secret resources in a given resource group. The information include the description and other properties of the secret. |
