---
title: marketplace_registration_definitions_without_scope
hide_title: false
hide_table_of_contents: false
keywords:
  - marketplace_registration_definitions_without_scope
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
<tr><td><b>Name</b></td><td><code>marketplace_registration_definitions_without_scope</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_services.marketplace_registration_definitions_without_scope" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The fully qualified path of the marketplace registration definition. |
| <CopyableCode code="name" /> | `string` | The name of the marketplace registration definition. |
| <CopyableCode code="plan" /> | `object` | Plan for the resource. |
| <CopyableCode code="properties" /> | `object` | The properties of the marketplace registration definition. |
| <CopyableCode code="type" /> | `string` | The type of the Azure resource (Microsoft.ManagedServices/marketplaceRegistrationDefinitions). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="marketplaceIdentifier" /> | Get the marketplace registration definition for the marketplace identifier. |
| <CopyableCode code="list" /> | `SELECT` |  | Gets a list of the marketplace registration definitions for the marketplace identifier. |
