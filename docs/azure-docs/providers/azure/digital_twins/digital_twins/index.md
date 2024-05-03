---
title: digital_twins
hide_title: false
hide_table_of_contents: false
keywords:
  - digital_twins
  - digital_twins
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
<tr><td><b>Name</b></td><td><code>digital_twins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.digital_twins.digital_twins" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="identity" /> | `object` | The managed identity for the DigitalTwinsInstance. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The properties of a DigitalTwinsInstance. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Get DigitalTwinsInstances resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | Get all the DigitalTwinsInstances in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Get all the DigitalTwinsInstances in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Create or update the metadata of a DigitalTwinsInstance. The usual pattern to modify a property is to retrieve the DigitalTwinsInstance and security metadata, and then combine them with the modified values in a new body to update the DigitalTwinsInstance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Delete a DigitalTwinsInstance. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> | Get all the DigitalTwinsInstances in a subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Get all the DigitalTwinsInstances in a resource group. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="api-version, location, subscriptionId, data__name, data__type" /> | Check if a DigitalTwinsInstance name is available. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Update metadata of DigitalTwinsInstance. |
