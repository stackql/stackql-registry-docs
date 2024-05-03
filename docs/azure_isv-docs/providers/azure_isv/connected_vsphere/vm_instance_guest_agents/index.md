---
title: vm_instance_guest_agents
hide_title: false
hide_table_of_contents: false
keywords:
  - vm_instance_guest_agents
  - connected_vsphere
  - azure_isv    
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.connected_vsphere.vm_instance_guest_agents" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceUri" /> | Returns the list of GuestAgent of the given vm. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, resourceUri, data__properties" /> | Create Or Update GuestAgent. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, resourceUri" /> | Implements GuestAgent DELETE method. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, resourceUri" /> | Returns the list of GuestAgent of the given vm. |
