---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - service_fabric_managed_clusters
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_managed_clusters.applications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource identifier. |
| <CopyableCode code="name" /> | `string` | Azure resource name. |
| <CopyableCode code="identity" /> | `object` | Describes the managed identities for an Azure resource. |
| <CopyableCode code="location" /> | `string` | Resource location depends on the parent resource. |
| <CopyableCode code="properties" /> | `object` | The application resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Azure resource tags. |
| <CopyableCode code="type" /> | `string` | Azure resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, applicationName, clusterName, resourceGroupName, subscriptionId" /> | Get a Service Fabric managed application resource created or in the process of being created in the Service Fabric cluster resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, clusterName, resourceGroupName, subscriptionId" /> | Gets all managed application resources created or in the process of being created in the Service Fabric cluster resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, applicationName, clusterName, resourceGroupName, subscriptionId" /> | Create or update a Service Fabric managed application resource with the specified name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, applicationName, clusterName, resourceGroupName, subscriptionId" /> | Delete a Service Fabric managed application resource with the specified name. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, clusterName, resourceGroupName, subscriptionId" /> | Gets all managed application resources created or in the process of being created in the Service Fabric cluster resource. |
| <CopyableCode code="read_upgrade" /> | `EXEC` | <CopyableCode code="api-version, applicationName, clusterName, resourceGroupName, subscriptionId" /> | Get the status of the latest application upgrade. It will query the cluster to find the status of the latest application upgrade. |
| <CopyableCode code="resume_upgrade" /> | `EXEC` | <CopyableCode code="api-version, applicationName, clusterName, resourceGroupName, subscriptionId" /> | Send a request to resume the current application upgrade. This will resume the application upgrade from where it was paused. |
| <CopyableCode code="start_rollback" /> | `EXEC` | <CopyableCode code="api-version, applicationName, clusterName, resourceGroupName, subscriptionId" /> | Send a request to start a rollback of the current application upgrade. This will start rolling back the application to the previous version. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, applicationName, clusterName, resourceGroupName, subscriptionId" /> | Updates the tags of an application resource of a given managed cluster. |
