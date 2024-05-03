---
title: feeds
hide_title: false
hide_table_of_contents: false
keywords:
  - feeds
  - activity
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
<tr><td><b>Name</b></td><td><code>feeds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.activity.feeds" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="_links" /> | `object` |  |
| <CopyableCode code="current_user_actor_url" /> | `string` |  |
| <CopyableCode code="current_user_organization_url" /> | `string` |  |
| <CopyableCode code="current_user_organization_urls" /> | `array` |  |
| <CopyableCode code="current_user_public_url" /> | `string` |  |
| <CopyableCode code="current_user_url" /> | `string` |  |
| <CopyableCode code="repository_discussions_category_url" /> | `string` | A feed of discussions for a given repository and category. |
| <CopyableCode code="repository_discussions_url" /> | `string` | A feed of discussions for a given repository. |
| <CopyableCode code="security_advisories_url" /> | `string` |  |
| <CopyableCode code="timeline_url" /> | `string` |  |
| <CopyableCode code="user_url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_feeds" /> | `SELECT` |  |
