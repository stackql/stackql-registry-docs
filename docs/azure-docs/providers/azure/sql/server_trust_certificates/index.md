---
title: server_trust_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - server_trust_certificates
  - sql
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
<tr><td><b>Name</b></td><td><code>server_trust_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.server_trust_certificates</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerTrustCertificates_Get` | `SELECT` | `certificateName, managedInstanceName, resourceGroupName, subscriptionId` | Gets a server trust certificate that was uploaded from box to Sql Managed Instance. |
| `ServerTrustCertificates_ListByInstance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of server trust certificates that were uploaded from box to the given Sql Managed Instance. |
| `ServerTrustCertificates_CreateOrUpdate` | `INSERT` | `certificateName, managedInstanceName, resourceGroupName, subscriptionId` | Uploads a server trust certificate from box to Sql Managed Instance. |
| `ServerTrustCertificates_Delete` | `DELETE` | `certificateName, managedInstanceName, resourceGroupName, subscriptionId` | Deletes a server trust certificate that was uploaded from box to Sql Managed Instance. |
