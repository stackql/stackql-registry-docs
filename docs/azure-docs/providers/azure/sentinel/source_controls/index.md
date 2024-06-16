---
title: source_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - source_controls
  - sentinel
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
<tr><td><b>Name</b></td><td><code>source_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.source_controls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | Describes source control properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sourceControlId, subscriptionId, workspaceName" /> | Gets a source control byt its identifier. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets all source controls, without source control items. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, sourceControlId, subscriptionId, workspaceName, data__properties" /> | Creates a source control. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sourceControlId, subscriptionId, workspaceName, data__properties" /> | Delete a source control. |
