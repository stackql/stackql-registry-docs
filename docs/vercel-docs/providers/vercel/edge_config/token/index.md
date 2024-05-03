---
title: token
hide_title: false
hide_table_of_contents: false
keywords:
  - token
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
<tr><td><b>Name</b></td><td><code>token</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.edge_config.token" /></td></tr>
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
| <CopyableCode code="get_edge_config_token" /> | `SELECT` | <CopyableCode code="edgeConfigId, teamId, token" /> | Return meta data about an Edge Config token. |
| <CopyableCode code="create_edge_config_token" /> | `INSERT` | <CopyableCode code="edgeConfigId, teamId, data__label" /> | Adds a token to an existing Edge Config. |
