---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - container_apps
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
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_apps.certificates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Certificate resource specific properties |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Certificates_Get` | `SELECT` | `certificateName, environmentName, resourceGroupName, subscriptionId` |  |
| `Certificates_List` | `SELECT` | `environmentName, resourceGroupName, subscriptionId` |  |
| `Certificates_CreateOrUpdate` | `INSERT` | `certificateName, environmentName, resourceGroupName, subscriptionId` |  |
| `Certificates_Delete` | `DELETE` | `certificateName, environmentName, resourceGroupName, subscriptionId` |  |
| `Certificates_Update` | `EXEC` | `certificateName, environmentName, resourceGroupName, subscriptionId` | Patches a certificate. Currently only patching of tags is supported |
