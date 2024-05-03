---
title: tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - tokens
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
<tr><td><b>Name</b></td><td><code>tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.edge_config.tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | This is not the token itself, but rather an id to identify the token by |
| <CopyableCode code="createdAt" /> | `number` |  |
| <CopyableCode code="edgeConfigId" /> | `string` |  |
| <CopyableCode code="label" /> | `string` |  |
| <CopyableCode code="token" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_edge_config_tokens" /> | `SELECT` | <CopyableCode code="edgeConfigId, teamId" /> | Returns all tokens of an Edge Config. |
| <CopyableCode code="delete_edge_config_tokens" /> | `DELETE` | <CopyableCode code="edgeConfigId, teamId, data__tokens" /> | Deletes one or more tokens of an existing Edge Config. |
