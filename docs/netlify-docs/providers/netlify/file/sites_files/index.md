---
title: sites_files
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_files
  - file
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
<tr><td><b>Name</b></td><td><code>sites_files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.file.sites_files" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="mime_type" /> | `string` |
| <CopyableCode code="path" /> | `string` |
| <CopyableCode code="sha" /> | `string` |
| <CopyableCode code="size" /> | `integer` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getSiteFileByPathName" /> | `SELECT` | <CopyableCode code="file_path, site_id" /> |
| <CopyableCode code="listSiteFiles" /> | `SELECT` | <CopyableCode code="site_id" /> |
