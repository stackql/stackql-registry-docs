---
title: inputs
hide_title: false
hide_table_of_contents: false
keywords:
  - inputs
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
<tr><td><b>Name</b></td><td><code>inputs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.stream_analytics.inputs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | The properties that are associated with an input. |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="inputName, jobName, resourceGroupName, subscriptionId" /> | Gets details about the specified input. |
| <CopyableCode code="list_by_streaming_job" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Lists all of the inputs under the specified streaming job. |
| <CopyableCode code="create_or_replace" /> | `INSERT` | <CopyableCode code="inputName, jobName, resourceGroupName, subscriptionId" /> | Creates an input or replaces an already existing input under an existing streaming job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="inputName, jobName, resourceGroupName, subscriptionId" /> | Deletes an input from the streaming job. |
| <CopyableCode code="test" /> | `EXEC` | <CopyableCode code="inputName, jobName, resourceGroupName, subscriptionId" /> | Tests whether an input’s datasource is reachable and usable by the Azure Stream Analytics service. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="inputName, jobName, resourceGroupName, subscriptionId" /> | Updates an existing input under an existing streaming job. This can be used to partially update (ie. update one or two properties) an input without affecting the rest the job or input definition. |
