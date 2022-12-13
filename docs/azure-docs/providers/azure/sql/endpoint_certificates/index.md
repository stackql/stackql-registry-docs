---
title: endpoint_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_certificates
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
<tr><td><b>Name</b></td><td><code>endpoint_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.endpoint_certificates</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `EndpointCertificates_Get` | `SELECT` | `endpointType, managedInstanceName, resourceGroupName, subscriptionId` | Gets a certificate used on the endpoint with the given id. |
| `EndpointCertificates_ListByInstance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | List certificates used on endpoints on the target instance. |
