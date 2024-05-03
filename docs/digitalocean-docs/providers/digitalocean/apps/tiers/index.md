---
title: tiers
hide_title: false
hide_table_of_contents: false
keywords:
  - tiers
  - apps
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.apps.tiers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="build_seconds" /> | `string` |
| <CopyableCode code="egress_bandwidth_bytes" /> | `string` |
| <CopyableCode code="slug" /> | `string` |
| <CopyableCode code="storage_bytes" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_tier" /> | `SELECT` | <CopyableCode code="slug" /> | Retrieve information about a specific app tier. |
| <CopyableCode code="list_tiers" /> | `SELECT` |  | List all app tiers. |
| <CopyableCode code="_get_tier" /> | `EXEC` | <CopyableCode code="slug" /> | Retrieve information about a specific app tier. |
| <CopyableCode code="_list_tiers" /> | `EXEC` |  | List all app tiers. |
