---
title: impactors
hide_title: false
hide_table_of_contents: false
keywords:
  - impactors
  - business_services
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
<tr><td><b>Name</b></td><td><code>impactors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.business_services.impactors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="type" /> | `string` | The kind of object that is impacting |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_business_service_top_level_impactors" /> | `SELECT` | <CopyableCode code="X-EARLY-ACCESS" /> |
| <CopyableCode code="_get_business_service_top_level_impactors" /> | `EXEC` | <CopyableCode code="X-EARLY-ACCESS" /> |
