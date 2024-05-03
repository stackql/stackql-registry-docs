---
title: sites_snippets
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_snippets
  - snippet
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
<tr><td><b>Name</b></td><td><code>sites_snippets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.snippet.sites_snippets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `integer` |
| <CopyableCode code="general" /> | `string` |
| <CopyableCode code="general_position" /> | `string` |
| <CopyableCode code="goal" /> | `string` |
| <CopyableCode code="goal_position" /> | `string` |
| <CopyableCode code="site_id" /> | `string` |
| <CopyableCode code="title" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getSiteSnippet" /> | `SELECT` | <CopyableCode code="site_id, snippet_id" /> |
| <CopyableCode code="listSiteSnippets" /> | `SELECT` | <CopyableCode code="site_id" /> |
| <CopyableCode code="createSiteSnippet" /> | `INSERT` | <CopyableCode code="site_id" /> |
| <CopyableCode code="deleteSiteSnippet" /> | `DELETE` | <CopyableCode code="site_id, snippet_id" /> |
| <CopyableCode code="updateSiteSnippet" /> | `EXEC` | <CopyableCode code="site_id, snippet_id" /> |
