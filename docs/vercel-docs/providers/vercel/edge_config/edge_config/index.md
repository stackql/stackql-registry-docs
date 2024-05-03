---
title: edge_config
hide_title: false
hide_table_of_contents: false
keywords:
  - edge_config
  - edge_config
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>edge_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.edge_config.edge_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="createdAt" /> | `number` |  |
| <CopyableCode code="digest" /> | `string` |  |
| <CopyableCode code="itemCount" /> | `number` |  |
| <CopyableCode code="ownerId" /> | `string` |  |
| <CopyableCode code="sizeInBytes" /> | `number` |  |
| <CopyableCode code="slug" /> | `string` | Name for the Edge Config Names are not unique. Must start with an alphabetic character and can contain only alphanumeric characters and underscores). |
| <CopyableCode code="transfer" /> | `object` | Keeps track of the current state of the Edge Config while it gets transferred. |
| <CopyableCode code="updatedAt" /> | `number` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_edge_config" /> | `SELECT` | <CopyableCode code="edgeConfigId, teamId" /> | Returns an Edge Config. |
| <CopyableCode code="get_edge_configs" /> | `SELECT` | <CopyableCode code="teamId" /> | Returns all Edge Configs. |
| <CopyableCode code="create_edge_config" /> | `INSERT` | <CopyableCode code="teamId, data__slug" /> | Creates an Edge Config. |
| <CopyableCode code="delete_edge_config" /> | `DELETE` | <CopyableCode code="edgeConfigId, teamId" /> | Delete an Edge Config by id. |
| <CopyableCode code="update_edge_config" /> | `EXEC` | <CopyableCode code="edgeConfigId, teamId, data__slug" /> | Updates an Edge Config. |
