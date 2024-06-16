---
title: published_blueprints
hide_title: false
hide_table_of_contents: false
keywords:
  - published_blueprints
  - blueprints
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
<tr><td><b>Name</b></td><td><code>published_blueprints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.blueprints.published_blueprints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | String Id used to locate any resource on Azure. |
| <CopyableCode code="name" /> | `string` | Name of this resource. |
| <CopyableCode code="properties" /> | `object` | Schema for published blueprint definition properties. |
| <CopyableCode code="type" /> | `string` | Type of this resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="blueprintName, resourceScope, versionId" /> | Get a published version of a blueprint definition. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="blueprintName, resourceScope" /> | List published versions of given blueprint definition. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="blueprintName, resourceScope, versionId, data__properties" /> | Publish a new version of the blueprint definition with the latest artifacts. Published blueprint definitions are immutable. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="blueprintName, resourceScope, versionId" /> | Delete a published version of a blueprint definition. |
