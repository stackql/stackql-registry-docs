---
title: export_pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - export_pipelines
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
<tr><td><b>Name</b></td><td><code>export_pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.export_pipelines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed identity for the resource. |
| <CopyableCode code="location" /> | `string` | The location of the export pipeline. |
| <CopyableCode code="properties" /> | `object` | The properties of an export pipeline. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="exportPipelineName, registryName, resourceGroupName, subscriptionId" /> | Gets the properties of the export pipeline. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all export pipelines for the specified container registry. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="exportPipelineName, registryName, resourceGroupName, subscriptionId" /> | Creates an export pipeline for a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="exportPipelineName, registryName, resourceGroupName, subscriptionId" /> | Deletes an export pipeline from a container registry. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all export pipelines for the specified container registry. |
