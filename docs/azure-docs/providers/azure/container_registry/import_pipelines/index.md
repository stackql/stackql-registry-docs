---
title: import_pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - import_pipelines
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
<tr><td><b>Name</b></td><td><code>import_pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.import_pipelines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed identity for the resource. |
| <CopyableCode code="location" /> | `string` | The location of the import pipeline. |
| <CopyableCode code="properties" /> | `object` | The properties of an import pipeline. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="importPipelineName, registryName, resourceGroupName, subscriptionId" /> | Gets the properties of the import pipeline. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all import pipelines for the specified container registry. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="importPipelineName, registryName, resourceGroupName, subscriptionId" /> | Creates an import pipeline for a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="importPipelineName, registryName, resourceGroupName, subscriptionId" /> | Deletes an import pipeline from a container registry. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all import pipelines for the specified container registry. |
