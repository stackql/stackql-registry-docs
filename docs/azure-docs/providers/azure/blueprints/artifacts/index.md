---
title: artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - artifacts
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
<tr><td><b>Name</b></td><td><code>artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.blueprints.artifacts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | String Id used to locate any resource on Azure. |
| <CopyableCode code="name" /> | `string` | Name of this resource. |
| <CopyableCode code="kind" /> | `string` | Specifies the kind of blueprint artifact. |
| <CopyableCode code="type" /> | `string` | Type of this resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="artifactName, blueprintName, resourceScope" /> | Get a blueprint artifact. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="blueprintName, resourceScope" /> | List artifacts for a given blueprint definition. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="artifactName, blueprintName, resourceScope, data__kind" /> | Create or update blueprint artifact. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="artifactName, blueprintName, resourceScope" /> | Delete a blueprint artifact. |
