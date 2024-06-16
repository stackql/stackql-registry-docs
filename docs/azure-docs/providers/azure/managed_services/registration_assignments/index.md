---
title: registration_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - registration_assignments
  - managed_services
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
<tr><td><b>Name</b></td><td><code>registration_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_services.registration_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The fully qualified path of the registration assignment. |
| <CopyableCode code="name" /> | `string` | The name of the registration assignment. |
| <CopyableCode code="properties" /> | `object` | The properties of the registration assignment. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the Azure resource (Microsoft.ManagedServices/registrationAssignments). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registrationAssignmentId, scope" /> | Gets the details of the specified registration assignment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Gets a list of the registration assignments. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="registrationAssignmentId, scope" /> | Creates or updates a registration assignment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="registrationAssignmentId, scope" /> | Deletes the specified registration assignment. |
