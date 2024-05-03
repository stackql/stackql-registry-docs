---
title: url_slugs
hide_title: false
hide_table_of_contents: false
keywords:
  - url_slugs
  - status_dashboards
  - pagerduty    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>url_slugs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.status_dashboards.url_slugs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="url_slug" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_status_dashboard_by_url_slug" /> | `SELECT` | <CopyableCode code="X-EARLY-ACCESS, url_slug" /> |
| <CopyableCode code="_get_status_dashboard_by_url_slug" /> | `EXEC` | <CopyableCode code="X-EARLY-ACCESS, url_slug" /> |
