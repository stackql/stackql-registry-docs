---
title: communications
hide_title: false
hide_table_of_contents: false
keywords:
  - communications
  - support
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
<tr><td><b>Name</b></td><td><code>communications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.support.communications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Id of the resource. |
| `name` | `string` | Name of the resource. |
| `properties` | `object` | Describes the properties of a communication resource. |
| `type` | `string` | Type of the resource 'Microsoft.Support/communications'. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Communications_Get` | `SELECT` | `communicationName, subscriptionId, supportTicketName` | Returns communication details for a support ticket. |
| `Communications_List` | `SELECT` | `subscriptionId, supportTicketName` | Lists all communications (attachments not included) for a support ticket. &lt;br/&gt;&lt;/br&gt; You can also filter support ticket communications by _CreatedDate_ or _CommunicationType_ using the $filter parameter. The only type of communication supported today is _Web_. Output will be a paged result with _nextLink_, using which you can retrieve the next set of Communication results. &lt;br/&gt;&lt;br/&gt;Support ticket data is available for 18 months after ticket creation. If a ticket was created more than 18 months ago, a request for data might cause an error. |
| `Communications_Create` | `INSERT` | `communicationName, subscriptionId, supportTicketName` | Adds a new customer communication to an Azure support ticket. |
| `Communications_CheckNameAvailability` | `EXEC` | `subscriptionId, supportTicketName, data__name, data__type` | Check the availability of a resource name. This API should be used to check the uniqueness of the name for adding a new communication to the support ticket. |
