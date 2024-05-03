---
title: instance_sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_sizes
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
<tr><td><b>Name</b></td><td><code>instance_sizes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.apps.instance_sizes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="cpu_type" /> | `string` |
| <CopyableCode code="cpus" /> | `string` |
| <CopyableCode code="memory_bytes" /> | `string` |
| <CopyableCode code="slug" /> | `string` |
| <CopyableCode code="tier_downgrade_to" /> | `string` |
| <CopyableCode code="tier_slug" /> | `string` |
| <CopyableCode code="tier_upgrade_to" /> | `string` |
| <CopyableCode code="usd_per_month" /> | `string` |
| <CopyableCode code="usd_per_second" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_instanceSize" /> | `SELECT` | <CopyableCode code="slug" /> | Retrieve information about a specific instance size for `service`, `worker`, and `job` components. |
| <CopyableCode code="list_instanceSizes" /> | `SELECT` |  | List all instance sizes for `service`, `worker`, and `job` components. |
| <CopyableCode code="_get_instanceSize" /> | `EXEC` | <CopyableCode code="slug" /> | Retrieve information about a specific instance size for `service`, `worker`, and `job` components. |
| <CopyableCode code="_list_instanceSizes" /> | `EXEC` |  | List all instance sizes for `service`, `worker`, and `job` components. |
