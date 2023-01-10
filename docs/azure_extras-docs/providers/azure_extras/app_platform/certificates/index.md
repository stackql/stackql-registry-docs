---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - app_platform
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
<tr><td><b>Id</b></td><td><code>azure_extras.app_platform.certificates</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Certificates_Get` | `SELECT` | `certificateName, resourceGroupName, serviceName, subscriptionId` | Get the certificate resource. |
| `Certificates_List` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | List all the certificates of one user. |
| `Certificates_CreateOrUpdate` | `INSERT` | `certificateName, resourceGroupName, serviceName, subscriptionId` | Create or update certificate resource. |
| `Certificates_Delete` | `DELETE` | `certificateName, resourceGroupName, serviceName, subscriptionId` | Delete the certificate resource. |
