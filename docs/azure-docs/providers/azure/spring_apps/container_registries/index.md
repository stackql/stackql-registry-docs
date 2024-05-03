---
title: container_registries
hide_title: false
hide_table_of_contents: false
keywords:
  - container_registries
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>container_registries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.container_registries" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="containerRegistryName, resourceGroupName, serviceName, subscriptionId" /> | Get the container registries resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | List container registries resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="containerRegistryName, resourceGroupName, serviceName, subscriptionId" /> | Create or update container registry resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="containerRegistryName, resourceGroupName, serviceName, subscriptionId" /> | Delete a container registry resource. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | List container registries resource. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="containerRegistryName, resourceGroupName, serviceName, subscriptionId, data__credentials" /> | Check if the container registry properties are valid. |
