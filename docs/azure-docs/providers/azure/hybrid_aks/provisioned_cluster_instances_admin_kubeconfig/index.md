---
title: provisioned_cluster_instances_admin_kubeconfig
hide_title: false
hide_table_of_contents: false
keywords:
  - provisioned_cluster_instances_admin_kubeconfig
  - hybrid_aks
  - azure    
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
<tr><td><b>Name</b></td><td><code>provisioned_cluster_instances_admin_kubeconfig</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_aks.provisioned_cluster_instances_admin_kubeconfig</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Operation Id |
| `name` | `string` | Operation Name |
| `error` | `object` |  |
| `properties` | `object` |  |
| `resourceId` | `string` | ARM Resource Id of the provisioned cluster instance |
| `status` | `string` | Provisioning state of the resource |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `connectedClusterResourceUri` |
