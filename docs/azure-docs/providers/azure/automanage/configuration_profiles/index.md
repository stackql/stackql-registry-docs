---
title: configuration_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_profiles
  - automanage
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
<tr><td><b>Name</b></td><td><code>configuration_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automanage.configuration_profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Automanage configuration profile properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationProfileName, resourceGroupName, subscriptionId" /> | Get information about a configuration profile |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieve a list of configuration profile within a given resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieve a list of configuration profile within a subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationProfileName, resourceGroupName, subscriptionId" /> | Creates a configuration profile |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationProfileName, resourceGroupName, subscriptionId" /> | Delete a configuration profile |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieve a list of configuration profile within a given resource group |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Retrieve a list of configuration profile within a subscription |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="configurationProfileName, resourceGroupName, subscriptionId" /> | Updates a configuration profile |
