---
title: network_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - network_configurations
  - hybrid_compute
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_compute.network_configurations" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceUri" /> | Returns a NetworkConfiguration for the target resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceUri" /> | Create or update the NetworkConfiguration of the target resource. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceUri" /> | Update the endpoint to the target resource. |
