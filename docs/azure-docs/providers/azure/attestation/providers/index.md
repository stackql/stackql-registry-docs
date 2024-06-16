---
title: providers
hide_title: false
hide_table_of_contents: false
keywords:
  - providers
  - attestation
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
<tr><td><b>Name</b></td><td><code>providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.attestation.providers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Status of attestation service. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="providerName, resourceGroupName, subscriptionId" /> | Get the status of Attestation Provider. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns a list of attestation providers in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns attestation providers list in a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="providerName, resourceGroupName, subscriptionId, data__location, data__properties" /> | Creates or updates an Attestation Provider. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="providerName, resourceGroupName, subscriptionId" /> | Delete Attestation Service. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="providerName, resourceGroupName, subscriptionId" /> | Updates the Attestation Provider. |
