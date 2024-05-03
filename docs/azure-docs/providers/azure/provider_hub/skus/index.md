---
title: skus
hide_title: false
hide_table_of_contents: false
keywords:
  - skus
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
<tr><td><b>Name</b></td><td><code>skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.provider_hub.skus" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="providerNamespace, resourceType, sku, subscriptionId" /> | Gets the sku details for the given resource type and sku name. |
| <CopyableCode code="list_by_resource_type_registrations" /> | `SELECT` | <CopyableCode code="providerNamespace, resourceType, subscriptionId" /> | Gets the list of skus for the given resource type. |
| <CopyableCode code="list_by_resource_type_registrations_nested_resource_type_first" /> | `SELECT` | <CopyableCode code="nestedResourceTypeFirst, providerNamespace, resourceType, subscriptionId" /> | Gets the list of skus for the given resource type. |
| <CopyableCode code="list_by_resource_type_registrations_nested_resource_type_second" /> | `SELECT` | <CopyableCode code="nestedResourceTypeFirst, nestedResourceTypeSecond, providerNamespace, resourceType, subscriptionId" /> | Gets the list of skus for the given resource type. |
| <CopyableCode code="list_by_resource_type_registrations_nested_resource_type_third" /> | `SELECT` | <CopyableCode code="nestedResourceTypeFirst, nestedResourceTypeSecond, nestedResourceTypeThird, providerNamespace, resourceType, subscriptionId" /> | Gets the list of skus for the given resource type. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="providerNamespace, resourceType, sku, subscriptionId" /> | Creates or updates the resource type skus in the given resource type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="providerNamespace, resourceType, sku, subscriptionId" /> | Deletes a resource type sku. |
| <CopyableCode code="_list_by_resource_type_registrations" /> | `EXEC` | <CopyableCode code="providerNamespace, resourceType, subscriptionId" /> | Gets the list of skus for the given resource type. |
| <CopyableCode code="_list_by_resource_type_registrations_nested_resource_type_first" /> | `EXEC` | <CopyableCode code="nestedResourceTypeFirst, providerNamespace, resourceType, subscriptionId" /> | Gets the list of skus for the given resource type. |
| <CopyableCode code="_list_by_resource_type_registrations_nested_resource_type_second" /> | `EXEC` | <CopyableCode code="nestedResourceTypeFirst, nestedResourceTypeSecond, providerNamespace, resourceType, subscriptionId" /> | Gets the list of skus for the given resource type. |
| <CopyableCode code="_list_by_resource_type_registrations_nested_resource_type_third" /> | `EXEC` | <CopyableCode code="nestedResourceTypeFirst, nestedResourceTypeSecond, nestedResourceTypeThird, providerNamespace, resourceType, subscriptionId" /> | Gets the list of skus for the given resource type. |
