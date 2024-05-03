---
title: springbootsites
hide_title: false
hide_table_of_contents: false
keywords:
  - springbootsites
  - off_azure_springboot
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>springbootsites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.off_azure_springboot.springbootsites" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The extended location definition. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The springbootsites resource definition. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, springbootsitesName, subscriptionId" /> | Get a springbootsites resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List springbootsites resource by resourceGroup. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List springbootsites resource by subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, springbootsitesName, subscriptionId, data__location" /> | Create a springbootsites resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, springbootsitesName, subscriptionId" /> | Delete a springbootsites resource. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List springbootsites resource by resourceGroup. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List springbootsites resource by subscription |
| <CopyableCode code="trigger_refresh_site" /> | `EXEC` | <CopyableCode code="resourceGroupName, springbootsitesName, subscriptionId" /> | Trigger refresh springbootsites action |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, springbootsitesName, subscriptionId" /> | Update a springbootsites resource. |
