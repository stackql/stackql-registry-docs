---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - spring_apps
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
<tr><td><b>Id</b></td><td><code>azure.spring_apps.certificates</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `certificateName, resourceGroupName, serviceName, subscriptionId` | Get the certificate resource. |
| `list` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | List all the certificates of one user. |
| `create_or_update` | `INSERT` | `certificateName, resourceGroupName, serviceName, subscriptionId` | Create or update certificate resource. |
| `delete` | `DELETE` | `certificateName, resourceGroupName, serviceName, subscriptionId` | Delete the certificate resource. |
| `_list` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | List all the certificates of one user. |
