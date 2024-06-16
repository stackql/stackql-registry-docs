---
title: autoscale_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - autoscale_settings
  - monitor
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
<tr><td><b>Name</b></td><td><code>autoscale_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.autoscale_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | A setting that contains all of the configuration for the automatic scaling of a resource. |
| <CopyableCode code="tags" /> | `` | Resource tags |
| <CopyableCode code="type" /> | `string` | Azure resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="autoscaleSettingName, resourceGroupName, subscriptionId" /> | Gets an autoscale setting |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the autoscale settings for a resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists the autoscale settings for a subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="autoscaleSettingName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates an autoscale setting. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="autoscaleSettingName, resourceGroupName, subscriptionId" /> | Deletes and autoscale setting |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="autoscaleSettingName, resourceGroupName, subscriptionId" /> | Updates an existing AutoscaleSettingsResource. To update other fields use the CreateOrUpdate method. |
