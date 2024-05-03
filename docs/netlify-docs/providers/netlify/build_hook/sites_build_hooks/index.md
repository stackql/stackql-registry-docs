---
title: sites_build_hooks
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_build_hooks
  - build_hook
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
<tr><td><b>Name</b></td><td><code>sites_build_hooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.build_hook.sites_build_hooks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="branch" /> | `string` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="site_id" /> | `string` |
| <CopyableCode code="title" /> | `string` |
| <CopyableCode code="url" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getSiteBuildHook" /> | `SELECT` | <CopyableCode code="id, site_id" /> |
| <CopyableCode code="listSiteBuildHooks" /> | `SELECT` | <CopyableCode code="site_id" /> |
| <CopyableCode code="createSiteBuildHook" /> | `INSERT` | <CopyableCode code="site_id" /> |
| <CopyableCode code="deleteSiteBuildHook" /> | `DELETE` | <CopyableCode code="id, site_id" /> |
| <CopyableCode code="updateSiteBuildHook" /> | `EXEC` | <CopyableCode code="id, site_id" /> |
