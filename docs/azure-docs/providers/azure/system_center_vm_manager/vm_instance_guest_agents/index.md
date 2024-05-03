---
title: vm_instance_guest_agents
hide_title: false
hide_table_of_contents: false
keywords:
  - vm_instance_guest_agents
  - system_center_vm_manager
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
<tr><td><b>Name</b></td><td><code>vm_instance_guest_agents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.system_center_vm_manager.vm_instance_guest_agents" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceUri" /> | Implements GuestAgent GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceUri, data__properties" /> | Create Or Update GuestAgent. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceUri" /> | Implements GuestAgent DELETE method. |
