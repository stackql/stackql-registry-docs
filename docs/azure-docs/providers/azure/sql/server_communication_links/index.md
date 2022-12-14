---
title: server_communication_links
hide_title: false
hide_table_of_contents: false
keywords:
  - server_communication_links
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
<tr><td><b>Name</b></td><td><code>server_communication_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.server_communication_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Communication link kind.  This property is used for Azure Portal metadata. |
| `location` | `string` | Communication link location. |
| `properties` | `object` | The properties of a server communication link. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerCommunicationLinks_Get` | `SELECT` | `communicationLinkName, resourceGroupName, serverName, subscriptionId` | Returns a server communication link. |
| `ServerCommunicationLinks_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of server communication links. |
| `ServerCommunicationLinks_CreateOrUpdate` | `INSERT` | `communicationLinkName, resourceGroupName, serverName, subscriptionId` | Creates a server communication link. |
| `ServerCommunicationLinks_Delete` | `DELETE` | `communicationLinkName, resourceGroupName, serverName, subscriptionId` | Deletes a server communication link. |
