---
title: sites_builds
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_builds
  - build
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
<tr><td><b>Name</b></td><td><code>sites_builds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.build.sites_builds" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="deploy_id" /> | `string` |
| <CopyableCode code="done" /> | `boolean` |
| <CopyableCode code="error" /> | `string` |
| <CopyableCode code="sha" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="listSiteBuilds" /> | `SELECT` | <CopyableCode code="site_id" /> |
| <CopyableCode code="createSiteBuild" /> | `INSERT` | <CopyableCode code="site_id" /> |
