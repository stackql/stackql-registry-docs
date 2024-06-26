---
title: pipeline_topologies
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline_topologies
  - video_analyzer
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
<tr><td><b>Name</b></td><td><code>pipeline_topologies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.video_analyzer.pipeline_topologies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Topology kind. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a pipeline topology. |
| <CopyableCode code="sku" /> | `object` | The SKU details. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, pipelineTopologyName, resourceGroupName, subscriptionId" /> | Retrieves a specific pipeline topology by name. If a topology with that name has been previously created, the call will return the JSON representation of that topology. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Retrieves a list of pipeline topologies that have been added to the account, if any, along with their JSON representation. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, pipelineTopologyName, resourceGroupName, subscriptionId, data__kind, data__sku" /> | Creates a new pipeline topology or updates an existing one, with the given name. A pipeline topology describes the processing steps to be applied when processing content for a particular outcome. The topology should be defined according to the scenario to be achieved and can be reused across many pipeline instances which share the same processing characteristics. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, pipelineTopologyName, resourceGroupName, subscriptionId" /> | Deletes a pipeline topology with the given name. This method should be called after all instances of the topology have been stopped and deleted. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, pipelineTopologyName, resourceGroupName, subscriptionId" /> | Updates an existing pipeline topology with the given name. If the associated live pipelines or pipeline jobs are in active or processing state, respectively, then only the description can be updated. Else, the properties that can be updated include: description, parameter declarations, sources, processors, and sinks. |
