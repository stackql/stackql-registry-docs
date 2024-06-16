---
title: web_apps_host_name_binding
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps_host_name_binding
  - app_service
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
<tr><td><b>Name</b></td><td><code>web_apps_host_name_binding</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.web_apps_host_name_binding" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | HostNameBinding resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostName, name, resourceGroupName, subscriptionId" /> | Description for Get the named hostname binding for an app (or deployment slot, if specified). |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hostName, name, resourceGroupName, subscriptionId" /> | Description for Creates a hostname binding for an app. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hostName, name, resourceGroupName, subscriptionId" /> | Description for Deletes a hostname binding for an app. |
