---
title: cloud_exadata_infrastructures
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_exadata_infrastructures
  - oracle
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
<tr><td><b>Name</b></td><td><code>cloud_exadata_infrastructures</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.cloud_exadata_infrastructures" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | CloudExadataInfrastructure resource model |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="zones" /> | `array` | CloudExadataInfrastructure zones |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudexadatainfrastructurename, resourceGroupName, subscriptionId" /> | Get a CloudExadataInfrastructure |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List CloudExadataInfrastructure resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List CloudExadataInfrastructure resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cloudexadatainfrastructurename, resourceGroupName, subscriptionId, data__zones" /> | Create a CloudExadataInfrastructure |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudexadatainfrastructurename, resourceGroupName, subscriptionId" /> | Delete a CloudExadataInfrastructure |
| <CopyableCode code="add_storage_capacity" /> | `EXEC` | <CopyableCode code="cloudexadatainfrastructurename, resourceGroupName, subscriptionId" /> | Perform add storage capacity on exadata infra |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="cloudexadatainfrastructurename, resourceGroupName, subscriptionId" /> | Update a CloudExadataInfrastructure |
