---
title: app_attach_package
hide_title: false
hide_table_of_contents: false
keywords:
  - app_attach_package
  - desktop_virtualization
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
<tr><td><b>Name</b></td><td><code>app_attach_package</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.app_attach_package" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Schema for App Attach Package properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appAttachPackageName, resourceGroupName, subscriptionId" /> | Get an app attach package. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List App Attach packages in resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List App Attach packages in subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="appAttachPackageName, resourceGroupName, subscriptionId, data__properties" /> | Create or update an App Attach package. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appAttachPackageName, resourceGroupName, subscriptionId" /> | Remove an App Attach Package. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List App Attach packages in resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List App Attach packages in subscription. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="appAttachPackageName, resourceGroupName, subscriptionId" /> | Update an App Attach Package |
