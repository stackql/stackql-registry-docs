---
title: item
hide_title: false
hide_table_of_contents: false
keywords:
  - item
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
<tr><td><b>Name</b></td><td><code>item</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.edge_config.item" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="createdAt" /> | `number` |
| <CopyableCode code="edgeConfigId" /> | `string` |
| <CopyableCode code="key" /> | `string` |
| <CopyableCode code="updatedAt" /> | `number` |
| <CopyableCode code="value" /> ||
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_edge_config_item" /> | `SELECT` | <CopyableCode code="edgeConfigId, edgeConfigItemKey, teamId" /> |
