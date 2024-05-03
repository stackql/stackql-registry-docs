---
title: sites_service_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_service_instances
  - service_instance
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
<tr><td><b>Name</b></td><td><code>sites_service_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.service_instance.sites_service_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="auth_url" /> | `string` |
| <CopyableCode code="config" /> | `object` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="env" /> | `object` |
| <CopyableCode code="external_attributes" /> | `object` |
| <CopyableCode code="service_name" /> | `string` |
| <CopyableCode code="service_path" /> | `string` |
| <CopyableCode code="service_slug" /> | `string` |
| <CopyableCode code="snippets" /> | `array` |
| <CopyableCode code="updated_at" /> | `string` |
| <CopyableCode code="url" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="listServiceInstancesForSite" /> | `SELECT` | <CopyableCode code="site_id" /> |
