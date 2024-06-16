---
title: node_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - node_reports
  - automation
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.node_reports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the id. |
| <CopyableCode code="configurationVersion" /> | `string` | Gets or sets the configurationVersion of the node report. |
| <CopyableCode code="endTime" /> | `string` | Gets or sets the end time of the node report. |
| <CopyableCode code="errors" /> | `array` | Gets or sets the errors for the node report. |
| <CopyableCode code="hostName" /> | `string` | Gets or sets the hostname of the node that sent the report. |
| <CopyableCode code="iPV4Addresses" /> | `array` | Gets or sets the IPv4 address of the node that sent the report. |
| <CopyableCode code="iPV6Addresses" /> | `array` | Gets or sets the IPv6 address of the node that sent the report. |
| <CopyableCode code="lastModifiedTime" /> | `string` | Gets or sets the lastModifiedTime of the node report. |
| <CopyableCode code="metaConfiguration" /> | `object` | Definition of the DSC Meta Configuration. |
| <CopyableCode code="numberOfResources" /> | `integer` | Gets or sets the number of resource in the node report. |
| <CopyableCode code="rawErrors" /> | `string` | Gets or sets the unparsed errors for the node report. |
| <CopyableCode code="rebootRequested" /> | `string` | Gets or sets the rebootRequested of the node report. |
| <CopyableCode code="refreshMode" /> | `string` | Gets or sets the refreshMode of the node report. |
| <CopyableCode code="reportFormatVersion" /> | `string` | Gets or sets the reportFormatVersion of the node report. |
| <CopyableCode code="reportId" /> | `string` | Gets or sets the id of the node report. |
| <CopyableCode code="resources" /> | `array` | Gets or sets the resource for the node report. |
| <CopyableCode code="startTime" /> | `string` | Gets or sets the start time of the node report. |
| <CopyableCode code="status" /> | `string` | Gets or sets the status of the node report. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type of the node report. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, nodeId, reportId, resourceGroupName, subscriptionId" /> | Retrieve the Dsc node report data by node id and report id. |
| <CopyableCode code="list_by_node" /> | `SELECT` | <CopyableCode code="automationAccountName, nodeId, resourceGroupName, subscriptionId" /> | Retrieve the Dsc node report list by node id. |
