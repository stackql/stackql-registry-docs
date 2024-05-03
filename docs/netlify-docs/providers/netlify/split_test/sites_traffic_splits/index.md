---
title: sites_traffic_splits
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_traffic_splits
  - split_test
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
<tr><td><b>Name</b></td><td><code>sites_traffic_splits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.split_test.sites_traffic_splits" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="active" /> | `boolean` |
| <CopyableCode code="branches" /> | `array` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="path" /> | `string` |
| <CopyableCode code="site_id" /> | `string` |
| <CopyableCode code="unpublished_at" /> | `string` |
| <CopyableCode code="updated_at" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getSplitTest" /> | `SELECT` | <CopyableCode code="site_id, split_test_id" /> |
| <CopyableCode code="getSplitTests" /> | `SELECT` | <CopyableCode code="site_id" /> |
| <CopyableCode code="createSplitTest" /> | `INSERT` | <CopyableCode code="site_id" /> |
| <CopyableCode code="updateSplitTest" /> | `EXEC` | <CopyableCode code="site_id, split_test_id" /> |
