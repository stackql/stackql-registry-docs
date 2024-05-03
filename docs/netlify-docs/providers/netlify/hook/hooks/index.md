---
title: hooks
hide_title: false
hide_table_of_contents: false
keywords:
  - hooks
  - hook
  - netlify    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Netlify resources using SQL
custom_edit_url: null
image: /img/providers/netlify/stackql-netlify-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.hook.hooks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="data" /> | `object` |
| <CopyableCode code="disabled" /> | `boolean` |
| <CopyableCode code="event" /> | `string` |
| <CopyableCode code="site_id" /> | `string` |
| <CopyableCode code="type" /> | `string` |
| <CopyableCode code="updated_at" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getHook" /> | `SELECT` | <CopyableCode code="hook_id" /> |
| <CopyableCode code="listHooksBySiteId" /> | `SELECT` | <CopyableCode code="site_id" /> |
| <CopyableCode code="createHookBySiteId" /> | `INSERT` | <CopyableCode code="site_id" /> |
| <CopyableCode code="deleteHook" /> | `DELETE` | <CopyableCode code="hook_id" /> |
| <CopyableCode code="updateHook" /> | `EXEC` | <CopyableCode code="hook_id" /> |
