---
title: license_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - license_profiles
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
<tr><td><b>Name</b></td><td><code>license_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_compute.license_profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Describe the properties of a license profile. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="licenseProfileName, machineName, resourceGroupName, subscriptionId" /> | Retrieves information about the view of a license profile. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="machineName, resourceGroupName, subscriptionId" /> | The operation to get all license profiles of a non-Azure machine |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="licenseProfileName, machineName, resourceGroupName, subscriptionId" /> | The operation to create or update a license profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="licenseProfileName, machineName, resourceGroupName, subscriptionId" /> | The operation to delete a license profile. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="machineName, resourceGroupName, subscriptionId" /> | The operation to get all license profiles of a non-Azure machine |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="licenseProfileName, machineName, resourceGroupName, subscriptionId" /> | The operation to update a license profile. |
