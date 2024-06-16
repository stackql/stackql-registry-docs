---
title: archives
hide_title: false
hide_table_of_contents: false
keywords:
  - archives
  - container_registry
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
<tr><td><b>Name</b></td><td><code>archives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.archives" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | The properties of a archive. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="archiveName, packageType, registryName, resourceGroupName, subscriptionId" /> | Gets the properties of the archive. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="packageType, registryName, resourceGroupName, subscriptionId" /> | Lists all archives for the specified container registry and package type. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="archiveName, packageType, registryName, resourceGroupName, subscriptionId" /> | Creates a archive for a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="archiveName, packageType, registryName, resourceGroupName, subscriptionId" /> | Deletes a archive from a container registry. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="archiveName, packageType, registryName, resourceGroupName, subscriptionId" /> | Updates a archive for a container registry with the specified parameters. |
