---
title: outputs
hide_title: false
hide_table_of_contents: false
keywords:
  - outputs
  - stream_analytics
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
<tr><td><b>Name</b></td><td><code>outputs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.stream_analytics.outputs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | The properties that are associated with an output. |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobName, outputName, resourceGroupName, subscriptionId" /> | Gets details about the specified output. |
| <CopyableCode code="list_by_streaming_job" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Lists all of the outputs under the specified streaming job. |
| <CopyableCode code="create_or_replace" /> | `INSERT` | <CopyableCode code="jobName, outputName, resourceGroupName, subscriptionId" /> | Creates an output or replaces an already existing output under an existing streaming job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobName, outputName, resourceGroupName, subscriptionId" /> | Deletes an output from the streaming job. |
| <CopyableCode code="test" /> | `EXEC` | <CopyableCode code="jobName, outputName, resourceGroupName, subscriptionId" /> | Tests whether an output’s datasource is reachable and usable by the Azure Stream Analytics service. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="jobName, outputName, resourceGroupName, subscriptionId" /> | Updates an existing output under an existing streaming job. This can be used to partially update (ie. update one or two properties) an output without affecting the rest the job or output definition. |
