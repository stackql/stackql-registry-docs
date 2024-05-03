---
title: dns_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_zones
  - dns_zone
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
<tr><td><b>Name</b></td><td><code>dns_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.dns_zone.dns_zones" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="account_id" /> | `string` |
| <CopyableCode code="account_name" /> | `string` |
| <CopyableCode code="account_slug" /> | `string` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="dedicated" /> | `boolean` |
| <CopyableCode code="dns_servers" /> | `array` |
| <CopyableCode code="domain" /> | `string` |
| <CopyableCode code="errors" /> | `array` |
| <CopyableCode code="ipv6_enabled" /> | `boolean` |
| <CopyableCode code="records" /> | `array` |
| <CopyableCode code="site_id" /> | `string` |
| <CopyableCode code="supported_record_types" /> | `array` |
| <CopyableCode code="updated_at" /> | `string` |
| <CopyableCode code="user_id" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getDnsZone" /> | `SELECT` | <CopyableCode code="zone_id" /> |
| <CopyableCode code="getDnsZones" /> | `SELECT` |  |
| <CopyableCode code="createDnsZone" /> | `INSERT` |  |
| <CopyableCode code="deleteDnsZone" /> | `DELETE` | <CopyableCode code="zone_id" /> |
