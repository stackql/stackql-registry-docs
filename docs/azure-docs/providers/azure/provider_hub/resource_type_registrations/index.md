---
title: resource_type_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_type_registrations
  - provider_hub
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
<tr><td><b>Name</b></td><td><code>resource_type_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.provider_hub.resource_type_registrations" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="providerNamespace, resourceType, subscriptionId" /> | Gets a resource type details in the given subscription and provider. |
| <CopyableCode code="list_by_provider_registration" /> | `SELECT` | <CopyableCode code="providerNamespace, subscriptionId" /> | Gets the list of the resource types for the given provider. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="providerNamespace, resourceType, subscriptionId" /> | Creates or updates a resource type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="providerNamespace, resourceType, subscriptionId" /> | Deletes a resource type |
| <CopyableCode code="_list_by_provider_registration" /> | `EXEC` | <CopyableCode code="providerNamespace, subscriptionId" /> | Gets the list of the resource types for the given provider. |
