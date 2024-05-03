---
title: application_type_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - application_type_versions
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
<tr><td><b>Name</b></td><td><code>application_type_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric.application_type_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource identifier. |
| <CopyableCode code="name" /> | `string` | Azure resource name. |
| <CopyableCode code="etag" /> | `string` | Azure resource etag. |
| <CopyableCode code="location" /> | `string` | It will be deprecated in New API, resource location depends on the parent resource. |
| <CopyableCode code="properties" /> | `object` | The properties of the application type version resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Azure resource tags. |
| <CopyableCode code="type" /> | `string` | Azure resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, applicationTypeName, clusterName, resourceGroupName, subscriptionId, version" /> | Get a Service Fabric application type version resource created or in the process of being created in the Service Fabric application type name resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, applicationTypeName, clusterName, resourceGroupName, subscriptionId" /> | Gets all application type version resources created or in the process of being created in the Service Fabric application type name resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, applicationTypeName, clusterName, resourceGroupName, subscriptionId, version" /> | Create or update a Service Fabric application type version resource with the specified name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, applicationTypeName, clusterName, resourceGroupName, subscriptionId, version" /> | Delete a Service Fabric application type version resource with the specified name. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, applicationTypeName, clusterName, resourceGroupName, subscriptionId" /> | Gets all application type version resources created or in the process of being created in the Service Fabric application type name resource. |
