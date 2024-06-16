---
title: transformations
hide_title: false
hide_table_of_contents: false
keywords:
  - transformations
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
<tr><td><b>Name</b></td><td><code>transformations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.stream_analytics.transformations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | The properties that are associated with a transformation. |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId, transformationName" /> | Gets details about the specified transformation. |
| <CopyableCode code="create_or_replace" /> | `INSERT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId, transformationName" /> | Creates a transformation or replaces an already existing transformation under an existing streaming job. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="jobName, resourceGroupName, subscriptionId, transformationName" /> | Updates an existing transformation under an existing streaming job. This can be used to partially update (ie. update one or two properties) a transformation without affecting the rest the job or transformation definition. |
