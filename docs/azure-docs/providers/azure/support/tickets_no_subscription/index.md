---
title: tickets_no_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - tickets_no_subscription
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
<tr><td><b>Name</b></td><td><code>tickets_no_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.support.tickets_no_subscription</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Id of the resource. |
| `name` | `string` | Name of the resource. |
| `properties` | `object` | Describes the properties of a support ticket. |
| `type` | `string` | Type of the resource 'Microsoft.Support/supportTickets'. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `supportTicketName` | Gets details for a specific support ticket. Support ticket data is available for 18 months after ticket creation. If a ticket was created more than 18 months ago, a request for data might cause an error. |
| `list` | `SELECT` |  | Lists all the support tickets. &lt;br/&gt;&lt;br/&gt;You can also filter the support tickets by &lt;i&gt;Status&lt;/i&gt;, &lt;i&gt;CreatedDate&lt;/i&gt;, , &lt;i&gt;ServiceId&lt;/i&gt;, and &lt;i&gt;ProblemClassificationId&lt;/i&gt; using the $filter parameter. Output will be a paged result with &lt;i&gt;nextLink&lt;/i&gt;, using which you can retrieve the next set of support tickets. &lt;br/&gt;&lt;br/&gt;Support ticket data is available for 18 months after ticket creation. If a ticket was created more than 18 months ago, a request for data might cause an error. |
| `create` | `INSERT` | `supportTicketName` | Creates a new support ticket for Billing, and Subscription Management issues. Learn the [prerequisites](https://aka.ms/supportAPI) required to create a support ticket.&lt;br/&gt;&lt;br/&gt;Always call the Services and ProblemClassifications API to get the most recent set of services and problem categories required for support ticket creation.&lt;br/&gt;&lt;br/&gt;Adding attachments is not currently supported via the API. To add a file to an existing support ticket, visit the [Manage support ticket](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/managesupportrequest) page in the Azure portal, select the support ticket, and use the file upload control to add a new file.&lt;br/&gt;&lt;br/&gt;Providing consent to share diagnostic information with Azure support is currently not supported via the API. The Azure support engineer working on your ticket will reach out to you for consent if your issue requires gathering diagnostic information from your Azure resources.&lt;br/&gt;&lt;br/&gt; |
| `_list` | `EXEC` |  | Lists all the support tickets. &lt;br/&gt;&lt;br/&gt;You can also filter the support tickets by &lt;i&gt;Status&lt;/i&gt;, &lt;i&gt;CreatedDate&lt;/i&gt;, , &lt;i&gt;ServiceId&lt;/i&gt;, and &lt;i&gt;ProblemClassificationId&lt;/i&gt; using the $filter parameter. Output will be a paged result with &lt;i&gt;nextLink&lt;/i&gt;, using which you can retrieve the next set of support tickets. &lt;br/&gt;&lt;br/&gt;Support ticket data is available for 18 months after ticket creation. If a ticket was created more than 18 months ago, a request for data might cause an error. |
| `check_name_availability` | `EXEC` | `data__name, data__type` | Check the availability of a resource name. This API should be used to check the uniqueness of the name for support ticket creation for the selected subscription. |
| `update` | `EXEC` | `supportTicketName` | This API allows you to update the severity level, ticket status, and your contact information in the support ticket.&lt;br/&gt;&lt;br/&gt;Note: The severity levels cannot be changed if a support ticket is actively being worked upon by an Azure support engineer. In such a case, contact your support engineer to request severity update by adding a new communication using the Communications API. |
