---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - communication
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
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.communication.domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | A class that describes the properties of a Domains resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `domainName, emailServiceName, resourceGroupName, subscriptionId` | Get the Domains resource and its properties. |
| `list_by_email_service_resource` | `SELECT` | `emailServiceName, resourceGroupName, subscriptionId` | Handles requests to list all Domains resources under the parent EmailServices resource. |
| `create_or_update` | `INSERT` | `domainName, emailServiceName, resourceGroupName, subscriptionId` | Add a new Domains resource under the parent EmailService resource or update an existing Domains resource. |
| `delete` | `DELETE` | `domainName, emailServiceName, resourceGroupName, subscriptionId` | Operation to delete a Domains resource. |
| `_list_by_email_service_resource` | `EXEC` | `emailServiceName, resourceGroupName, subscriptionId` | Handles requests to list all Domains resources under the parent EmailServices resource. |
| `cancel_verification` | `EXEC` | `domainName, emailServiceName, resourceGroupName, subscriptionId, data__verificationType` | Cancel verification of DNS record. |
| `initiate_verification` | `EXEC` | `domainName, emailServiceName, resourceGroupName, subscriptionId, data__verificationType` | Initiate verification of DNS record. |
| `update` | `EXEC` | `domainName, emailServiceName, resourceGroupName, subscriptionId` | Operation to update an existing Domains resource. |
