---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - service
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.service.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="environments" /> | `array` |
| <CopyableCode code="events" /> | `array` |
| <CopyableCode code="icon" /> | `string` |
| <CopyableCode code="long_description" /> | `string` |
| <CopyableCode code="manifest_url" /> | `string` |
| <CopyableCode code="service_path" /> | `string` |
| <CopyableCode code="slug" /> | `string` |
| <CopyableCode code="tags" /> | `array` |
| <CopyableCode code="updated_at" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getServices" /> | `SELECT` |  |
| <CopyableCode code="showService" /> | `EXEC` | <CopyableCode code="addonName" /> |
