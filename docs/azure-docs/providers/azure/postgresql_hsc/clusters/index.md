---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - postgresql_hsc
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
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql_hsc.clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the cluster. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Gets information about a cluster such as compute and storage configuration and cluster lifecycle metadata such as cluster creation date and time. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all clusters in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all clusters in a resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Creates a new cluster with servers. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Deletes a cluster together with servers in it. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all clusters in a subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all clusters in a resource group. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name, data__type" /> | Checks availability of a cluster name. Cluster names should be globally unique; at least 3 characters and at most 40 characters long; they must only contain lowercase letters, numbers, and hyphens; and must not start or end with a hyphen. |
| <CopyableCode code="promote_read_replica" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Promotes read replica cluster to an independent read-write cluster. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Restarts all nodes in the cluster. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Starts stopped compute on all cluster nodes. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Stops compute on all cluster nodes. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Updates an existing cluster. The request body can contain one or several properties from the cluster definition. |
