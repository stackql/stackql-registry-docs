---
title: sites_dns
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_dns
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
<tr><td><b>Name</b></td><td><code>sites_dns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.dns_zone.sites_dns" /></td></tr>
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
| <CopyableCode code="getDNSForSite" /> | `SELECT` | <CopyableCode code="site_id" /> |
| <CopyableCode code="configureDNSForSite" /> | `EXEC` | <CopyableCode code="site_id" /> |
