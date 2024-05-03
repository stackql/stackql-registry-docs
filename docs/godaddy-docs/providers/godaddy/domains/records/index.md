---
title: records
hide_title: false
hide_table_of_contents: false
keywords:
  - records
  - domains
  - godaddy    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GoDaddy resources using SQL
custom_edit_url: null
image: /img/providers/godaddy/stackql-godaddy-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>records</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="godaddy.domains.records" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="data" /> | `string` |  |
| <CopyableCode code="port" /> | `integer` | Service port (SRV only) |
| <CopyableCode code="priority" /> | `integer` | Record priority (MX and SRV only) |
| <CopyableCode code="protocol" /> | `string` | Service protocol (SRV only) |
| <CopyableCode code="service" /> | `string` | Service type (SRV only) |
| <CopyableCode code="ttl" /> | `integer` |  |
| <CopyableCode code="type" /> | `string` |  |
| <CopyableCode code="weight" /> | `integer` | Record weight (SRV only) |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="record_get" /> | `SELECT` | <CopyableCode code="domain, type" /> | Retrieve DNS Records for the specified Domain, optionally with the specified Type and/or Name |
| <CopyableCode code="record_add" /> | `EXEC` | <CopyableCode code="domain" /> | Add the specified DNS Records to the specified Domain |
| <CopyableCode code="record_replace" /> | `EXEC` | <CopyableCode code="domain" /> | Replace all DNS Records for the specified Domain |
| <CopyableCode code="record_replace_type" /> | `EXEC` | <CopyableCode code="domain, type" /> | Replace all DNS Records for the specified Domain with the specified Type |
| <CopyableCode code="record_replace_type_name" /> | `EXEC` | <CopyableCode code="domain, name, type" /> | Replace all DNS Records for the specified Domain with the specified Type and Name |
