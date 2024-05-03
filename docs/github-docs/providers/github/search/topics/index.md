---
title: topics
hide_title: false
hide_table_of_contents: false
keywords:
  - topics
  - search
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
<tr><td><b>Name</b></td><td><code>topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.search.topics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="aliases" /> | `array` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="curated" /> | `boolean` |
| <CopyableCode code="display_name" /> | `string` |
| <CopyableCode code="featured" /> | `boolean` |
| <CopyableCode code="logo_url" /> | `string` |
| <CopyableCode code="related" /> | `array` |
| <CopyableCode code="released" /> | `string` |
| <CopyableCode code="repository_count" /> | `integer` |
| <CopyableCode code="score" /> | `number` |
| <CopyableCode code="short_description" /> | `string` |
| <CopyableCode code="text_matches" /> | `array` |
| <CopyableCode code="updated_at" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="topics" /> | `SELECT` | <CopyableCode code="q" /> |
