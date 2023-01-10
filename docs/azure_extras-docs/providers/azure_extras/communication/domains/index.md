---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - communication
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
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.communication.domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | A class that describes the properties of a Domains resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Domains_Get` | `SELECT` | `domainName, emailServiceName, resourceGroupName, subscriptionId` | Get the Domains resource and its properties. |
| `Domains_ListByEmailServiceResource` | `SELECT` | `emailServiceName, resourceGroupName, subscriptionId` | Handles requests to list all Domains resources under the parent EmailServices resource. |
| `Domains_CreateOrUpdate` | `INSERT` | `domainName, emailServiceName, resourceGroupName, subscriptionId` | Add a new Domains resource under the parent EmailService resource or update an existing Domains resource. |
| `Domains_Delete` | `DELETE` | `domainName, emailServiceName, resourceGroupName, subscriptionId` | Operation to delete a Domains resource. |
| `Domains_CancelVerification` | `EXEC` | `domainName, emailServiceName, resourceGroupName, subscriptionId, data__verificationType` | Cancel verification of DNS record. |
| `Domains_InitiateVerification` | `EXEC` | `domainName, emailServiceName, resourceGroupName, subscriptionId, data__verificationType` | Initiate verification of DNS record. |
| `Domains_Update` | `EXEC` | `domainName, emailServiceName, resourceGroupName, subscriptionId` | Operation to update an existing Domains resource. |
