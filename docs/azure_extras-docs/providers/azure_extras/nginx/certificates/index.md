---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - nginx
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
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.nginx.certificates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` |  |
| `type` | `string` |  |
| `location` | `string` |  |
| `properties` | `object` |  |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Certificates_Get` | `SELECT` | `certificateName, deploymentName, resourceGroupName, subscriptionId` |
| `Certificates_List` | `SELECT` | `deploymentName, resourceGroupName, subscriptionId` |
| `Certificates_Create` | `INSERT` | `certificateName, deploymentName, resourceGroupName, subscriptionId` |
| `Certificates_Delete` | `DELETE` | `certificateName, deploymentName, resourceGroupName, subscriptionId` |
