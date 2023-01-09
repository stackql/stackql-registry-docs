---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - sasportal
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.sasportal.deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name. |
| `displayName` | `string` | The deployment's display name. |
| `frns` | `array` | Output only. The FRNs copied from its direct parent. |
| `sasUserIds` | `array` | User ID used by the devices belonging to this deployment. Each deployment should be associated with one unique user ID. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `customers_deployments_get` | `SELECT` | `customersId, deploymentsId` | Returns a requested deployment. |
| `customers_deployments_list` | `SELECT` | `customersId` | Lists deployments. |
| `customers_nodes_deployments_list` | `SELECT` | `customersId, nodesId` | Lists deployments. |
| `get` | `SELECT` | `deploymentsId` | Returns a requested deployment. |
| `nodes_deployments_get` | `SELECT` | `deploymentsId, nodesId` | Returns a requested deployment. |
| `nodes_deployments_list` | `SELECT` | `nodesId` | Lists deployments. |
| `nodes_nodes_deployments_list` | `SELECT` | `nodesId, nodesId1` | Lists deployments. |
| `customers_deployments_create` | `INSERT` | `customersId` | Creates a new deployment. |
| `customers_nodes_deployments_create` | `INSERT` | `customersId, nodesId` | Creates a new deployment. |
| `nodes_nodes_deployments_create` | `INSERT` | `nodesId, nodesId1` | Creates a new deployment. |
| `customers_deployments_delete` | `DELETE` | `customersId, deploymentsId` | Deletes a deployment. |
| `nodes_deployments_delete` | `DELETE` | `deploymentsId, nodesId` | Deletes a deployment. |
| `customers_deployments_move` | `EXEC` | `customersId, deploymentsId` | Moves a deployment under another node or customer. |
| `customers_deployments_patch` | `EXEC` | `customersId, deploymentsId` | Updates an existing deployment. |
| `nodes_deployments_move` | `EXEC` | `deploymentsId, nodesId` | Moves a deployment under another node or customer. |
| `nodes_deployments_patch` | `EXEC` | `deploymentsId, nodesId` | Updates an existing deployment. |
