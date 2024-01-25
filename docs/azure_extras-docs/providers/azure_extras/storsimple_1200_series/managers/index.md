---
title: managers
hide_title: false
hide_table_of_contents: false
keywords:
  - managers
  - storsimple_1200_series
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>managers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_1200_series.managers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The Resource Id |
| `name` | `string` | The Resource Name |
| `etag` | `string` | ETag of the Manager |
| `location` | `string` | The Geo location of the Manager |
| `properties` | `object` | The properties of the Manager |
| `tags` | `object` | Tags attached to the Manager |
| `type` | `string` | The Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `managerName, resourceGroupName, subscriptionId` | Returns the properties of the specified manager name. |
| `list` | `SELECT` | `subscriptionId` | Retrieves all the managers in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieves all the managers in a resource group. |
| `create_or_update` | `INSERT` | `managerName, resourceGroupName, subscriptionId` | Creates or updates the manager. |
| `delete` | `DELETE` | `managerName, resourceGroupName, subscriptionId` | Deletes the manager. |
| `_list` | `EXEC` | `subscriptionId` | Retrieves all the managers in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Retrieves all the managers in a resource group. |
| `update` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Updates the StorSimple Manager. |
| `upload_registration_certificate` | `EXEC` | `certificateName, managerName, resourceGroupName, subscriptionId, data__properties` | Upload Vault Cred Certificate.<br />Returns UploadCertificateResponse |
