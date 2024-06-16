---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.apps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed identity properties retrieved from ARM request headers. |
| <CopyableCode code="location" /> | `string` | The GEO location of the application, always the same with its parent resource |
| <CopyableCode code="properties" /> | `object` | App resource properties payload |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appName, resourceGroupName, serviceName, subscriptionId" /> | Get an App and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all resources in a Service. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="appName, resourceGroupName, serviceName, subscriptionId" /> | Create a new App or update an exiting App. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appName, resourceGroupName, serviceName, subscriptionId" /> | Operation to delete an App. |
| <CopyableCode code="set_active_deployments" /> | `EXEC` | <CopyableCode code="appName, resourceGroupName, serviceName, subscriptionId" /> | Set existing Deployment under the app as active |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="appName, resourceGroupName, serviceName, subscriptionId" /> | Operation to update an exiting App. |
| <CopyableCode code="validate_domain" /> | `EXEC` | <CopyableCode code="appName, resourceGroupName, serviceName, subscriptionId, data__name" /> | Check the resource name is valid as well as not in use. |
