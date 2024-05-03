---
title: dns_zones_dns_records
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_zones_dns_records
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
<tr><td><b>Name</b></td><td><code>dns_zones_dns_records</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.dns_zone.dns_zones_dns_records" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="dns_zone_id" /> | `string` |
| <CopyableCode code="flag" /> | `integer` |
| <CopyableCode code="hostname" /> | `string` |
| <CopyableCode code="managed" /> | `boolean` |
| <CopyableCode code="priority" /> | `integer` |
| <CopyableCode code="site_id" /> | `string` |
| <CopyableCode code="tag" /> | `string` |
| <CopyableCode code="ttl" /> | `integer` |
| <CopyableCode code="type" /> | `string` |
| <CopyableCode code="value" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getDnsRecords" /> | `SELECT` | <CopyableCode code="zone_id" /> |
| <CopyableCode code="getIndividualDnsRecord" /> | `SELECT` | <CopyableCode code="dns_record_id, zone_id" /> |
| <CopyableCode code="createDnsRecord" /> | `INSERT` | <CopyableCode code="zone_id" /> |
| <CopyableCode code="deleteDnsRecord" /> | `DELETE` | <CopyableCode code="dns_record_id, zone_id" /> |
