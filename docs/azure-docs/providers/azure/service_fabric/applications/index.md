---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - service_fabric
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
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric.applications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource identifier. |
| <CopyableCode code="name" /> | `string` | Azure resource name. |
| <CopyableCode code="etag" /> | `string` | Azure resource etag. |
| <CopyableCode code="identity" /> | `object` | Describes the managed identities for an Azure resource. |
| <CopyableCode code="location" /> | `string` | It will be deprecated in New API, resource location depends on the parent resource. |
| <CopyableCode code="properties" /> | `object` | The application resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Azure resource tags. |
| <CopyableCode code="type" /> | `string` | Azure resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, applicationName, clusterName, resourceGroupName, subscriptionId" /> | Get a Service Fabric application resource created or in the process of being created in the Service Fabric cluster resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, clusterName, resourceGroupName, subscriptionId" /> | Gets all application resources created or in the process of being created in the Service Fabric cluster resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, applicationName, clusterName, resourceGroupName, subscriptionId" /> | Create or update a Service Fabric application resource with the specified name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, applicationName, clusterName, resourceGroupName, subscriptionId" /> | Delete a Service Fabric application resource with the specified name. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, applicationName, clusterName, resourceGroupName, subscriptionId" /> | Update a Service Fabric application resource with the specified name. |
