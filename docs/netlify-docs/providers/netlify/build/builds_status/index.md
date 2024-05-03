---
title: builds_status
hide_title: false
hide_table_of_contents: false
keywords:
  - builds_status
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
<tr><td><b>Name</b></td><td><code>builds_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.build.builds_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="active" /> | `integer` |
| <CopyableCode code="build_count" /> | `integer` |
| <CopyableCode code="enqueued" /> | `integer` |
| <CopyableCode code="minutes" /> | `object` |
| <CopyableCode code="pending_concurrency" /> | `integer` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getAccountBuildStatus" /> | `SELECT` | <CopyableCode code="account_id" /> |
