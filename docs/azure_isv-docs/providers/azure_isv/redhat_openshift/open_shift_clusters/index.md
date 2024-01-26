---
title: open_shift_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - open_shift_clusters
  - redhat_openshift
  - azure_isv    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>open_shift_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.redhat_openshift.open_shift_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | OpenShiftClusterProperties represents an OpenShift cluster's properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | The operation returns properties of a OpenShift cluster. |
| `list` | `SELECT` | `subscriptionId` | The operation returns properties of each OpenShift cluster. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | The operation returns properties of each OpenShift cluster. |
| `create_or_update` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | The operation returns properties of a OpenShift cluster. |
| `delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | The operation returns nothing. |
| `_list` | `EXEC` | `subscriptionId` | The operation returns properties of each OpenShift cluster. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | The operation returns properties of each OpenShift cluster. |
| `update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | The operation returns properties of a OpenShift cluster. |
