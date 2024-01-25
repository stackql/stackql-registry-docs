---
title: deployments_at_subscription_scope
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments_at_subscription_scope
  - resources
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
<tr><td><b>Name</b></td><td><code>deployments_at_subscription_scope</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resources.deployments_at_subscription_scope</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the deployment. |
| `name` | `string` | The name of the deployment. |
| `location` | `string` | the location of the deployment. |
| `properties` | `object` | Deployment properties with additional details. |
| `tags` | `object` | Deployment tags |
| `type` | `string` | The type of the deployment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deploymentName, subscriptionId` | Gets a deployment. |
| `list` | `SELECT` | `subscriptionId` | Get all the deployments for a subscription. |
| `create_or_update` | `INSERT` | `deploymentName, subscriptionId, data__properties` | You can provide the template and parameters directly in the request or link to JSON files. |
| `delete` | `DELETE` | `deploymentName, subscriptionId` | A template deployment that is currently running cannot be deleted. Deleting a template deployment removes the associated deployment operations. This is an asynchronous operation that returns a status of 202 until the template deployment is successfully deleted. The Location response header contains the URI that is used to obtain the status of the process. While the process is running, a call to the URI in the Location header returns a status of 202. When the process finishes, the URI in the Location header returns a status of 204 on success. If the asynchronous request failed, the URI in the Location header returns an error-level status code. |
| `_list` | `EXEC` | `subscriptionId` | Get all the deployments for a subscription. |
