---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
  - cdn
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
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.secrets" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, secretName, subscriptionId" /> | Gets an existing Secret within a profile. |
| <CopyableCode code="list_by_profile" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Lists existing AzureFrontDoor secrets. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="profileName, resourceGroupName, secretName, subscriptionId" /> | Creates a new Secret within the specified profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="profileName, resourceGroupName, secretName, subscriptionId" /> | Deletes an existing Secret within profile. |
| <CopyableCode code="_list_by_profile" /> | `EXEC` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Lists existing AzureFrontDoor secrets. |
