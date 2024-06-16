---
title: schema
hide_title: false
hide_table_of_contents: false
keywords:
  - schema
  - log_analytics
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
<tr><td><b>Name</b></td><td><code>schema</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.schema" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the schema. |
| <CopyableCode code="displayName" /> | `string` | The display name of the schema. |
| <CopyableCode code="facet" /> | `boolean` | The boolean that indicates whether or not the field is a facet. |
| <CopyableCode code="indexed" /> | `boolean` | The boolean that indicates the field is searchable as free text. |
| <CopyableCode code="ownerType" /> | `array` | The array of workflows containing the field. |
| <CopyableCode code="stored" /> | `boolean` | The boolean that indicates whether or not the field is stored. |
| <CopyableCode code="type" /> | `string` | The type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |
