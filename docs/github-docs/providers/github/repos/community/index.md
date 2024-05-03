---
title: community
hide_title: false
hide_table_of_contents: false
keywords:
  - community
  - repos
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>community</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.community" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="content_reports_enabled" /> | `boolean` |
| <CopyableCode code="documentation" /> | `string` |
| <CopyableCode code="files" /> | `object` |
| <CopyableCode code="health_percentage" /> | `integer` |
| <CopyableCode code="updated_at" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_community_profile_metrics" /> | `SELECT` | <CopyableCode code="owner, repo" /> |
