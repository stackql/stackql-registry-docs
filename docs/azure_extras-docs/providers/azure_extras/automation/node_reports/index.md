---
title: node_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - node_reports
  - automation
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
<tr><td><b>Name</b></td><td><code>node_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.node_reports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the id. |
| `resources` | `array` | Gets or sets the resource for the node report. |
| `refreshMode` | `string` | Gets or sets the refreshMode of the node report. |
| `endTime` | `string` | Gets or sets the end time of the node report. |
| `numberOfResources` | `integer` | Gets or sets the number of resource in the node report. |
| `errors` | `array` | Gets or sets the errors for the node report. |
| `reportFormatVersion` | `string` | Gets or sets the reportFormatVersion of the node report. |
| `configurationVersion` | `string` | Gets or sets the configurationVersion of the node report. |
| `reportId` | `string` | Gets or sets the id of the node report. |
| `metaConfiguration` | `object` | Definition of the DSC Meta Configuration. |
| `hostName` | `string` | Gets or sets the hostname of the node that sent the report. |
| `lastModifiedTime` | `string` | Gets or sets the lastModifiedTime of the node report. |
| `type` | `string` | Gets or sets the type of the node report. |
| `iPV6Addresses` | `array` | Gets or sets the IPv6 address of the node that sent the report. |
| `startTime` | `string` | Gets or sets the start time of the node report. |
| `iPV4Addresses` | `array` | Gets or sets the IPv4 address of the node that sent the report. |
| `status` | `string` | Gets or sets the status of the node report. |
| `rawErrors` | `string` | Gets or sets the unparsed errors for the node report. |
| `rebootRequested` | `string` | Gets or sets the rebootRequested of the node report. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NodeReports_Get` | `SELECT` | `automationAccountName, nodeId, reportId, resourceGroupName, subscriptionId` | Retrieve the Dsc node report data by node id and report id. |
| `NodeReports_ListByNode` | `SELECT` | `automationAccountName, nodeId, resourceGroupName, subscriptionId` | Retrieve the Dsc node report list by node id. |
| `NodeReports_GetContent` | `EXEC` | `automationAccountName, nodeId, reportId, resourceGroupName, subscriptionId` | Retrieve the Dsc node reports by node id and report id. |
