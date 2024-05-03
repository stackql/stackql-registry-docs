---
title: registration_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - registration_definitions
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
<tr><td><b>Name</b></td><td><code>registration_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_services.registration_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The fully qualified path of the registration definition. |
| <CopyableCode code="name" /> | `string` | The name of the registration definition. |
| <CopyableCode code="plan" /> | `object` | The details for the Managed Services offer’s plan in Azure Marketplace. |
| <CopyableCode code="properties" /> | `object` | The properties of a registration definition. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the Azure resource (Microsoft.ManagedServices/registrationDefinitions). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registrationDefinitionId, scope" /> | Gets the registration definition details. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Gets a list of the registration definitions. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="registrationDefinitionId, scope" /> | Creates or updates a registration definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="registrationDefinitionId, scope" /> | Deletes the registration definition. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="scope" /> | Gets a list of the registration definitions. |
