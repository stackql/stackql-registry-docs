---
title: ip_allowlists
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_allowlists
  - ip_allowlist
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_allowlists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.ip_allowlist.ip_allowlists" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique identifier of the org. |
| <CopyableCode code="attributes" /> | `object` | Attributes of the IP allowlist. |
| <CopyableCode code="type" /> | `string` | IP allowlist type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_ip_allowlist" /> | `SELECT` | <CopyableCode code="dd_site" /> | Returns the IP allowlist and its enabled or disabled state. |
| <CopyableCode code="_get_ip_allowlist" /> | `EXEC` | <CopyableCode code="dd_site" /> | Returns the IP allowlist and its enabled or disabled state. |
| <CopyableCode code="update_ip_allowlist" /> | `EXEC` | <CopyableCode code="data__data, dd_site" /> | Edit the entries in the IP allowlist, and enable or disable it. |
