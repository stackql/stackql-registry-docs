---
title: domains_records
hide_title: false
hide_table_of_contents: false
keywords:
  - domains_records
  - dns
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains_records</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.dns.domains_records" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="created" /> | `number` |
| <CopyableCode code="createdAt" /> | `number` |
| <CopyableCode code="creator" /> | `string` |
| <CopyableCode code="mxPriority" /> | `number` |
| <CopyableCode code="priority" /> | `number` |
| <CopyableCode code="slug" /> | `string` |
| <CopyableCode code="type" /> | `string` |
| <CopyableCode code="updated" /> | `number` |
| <CopyableCode code="updatedAt" /> | `number` |
| <CopyableCode code="value" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_records" /> | `SELECT` | <CopyableCode code="domain, teamId" /> | Retrieves a list of DNS records created for a domain name. By default it returns 20 records if no limit is provided. The rest can be retrieved using the pagination options. |
| <CopyableCode code="create_record" /> | `INSERT` | <CopyableCode code="domain, teamId, data__type" /> | Creates a DNS record for a domain. |
| <CopyableCode code="remove_record" /> | `DELETE` | <CopyableCode code="domain, recordId, teamId" /> | Removes an existing DNS record from a domain name. |
| <CopyableCode code="_get_records" /> | `EXEC` | <CopyableCode code="domain, teamId" /> | Retrieves a list of DNS records created for a domain name. By default it returns 20 records if no limit is provided. The rest can be retrieved using the pagination options. |
| <CopyableCode code="update_record" /> | `EXEC` | <CopyableCode code="recordId, teamId" /> | Updates an existing DNS record for a domain name. |
