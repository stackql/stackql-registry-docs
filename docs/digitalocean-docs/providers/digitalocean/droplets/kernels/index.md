---
title: kernels
hide_title: false
hide_table_of_contents: false
keywords:
  - kernels
  - droplets
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
<tr><td><b>Name</b></td><td><code>kernels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.droplets.kernels" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | A unique number used to identify and reference a specific kernel. |
| <CopyableCode code="name" /> | `string` | The display name of the kernel. This is shown in the web UI and is generally a descriptive title for the kernel in question. |
| <CopyableCode code="version" /> | `string` | A standard kernel version string representing the version, patch, and release information. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_kernels" /> | `SELECT` | <CopyableCode code="droplet_id" /> |
| <CopyableCode code="_list_kernels" /> | `EXEC` | <CopyableCode code="droplet_id" /> |
