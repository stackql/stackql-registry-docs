---
title: hcrp_assignment_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - hcrp_assignment_reports
  - guest_configuration
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
<tr><td><b>Name</b></td><td><code>hcrp_assignment_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.guest_configuration.hcrp_assignment_reports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ARM resource id of the report for the guest configuration assignment. |
| `name` | `string` | GUID that identifies the guest configuration assignment report under a subscription, resource group. |
| `properties` | `object` | Report for the guest configuration assignment. Report contains information such as compliance status, reason, and more. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GuestConfigurationHCRPAssignmentReports_Get` | `SELECT` | `guestConfigurationAssignmentName, machineName, reportId, resourceGroupName, subscriptionId` | Get a report for the guest configuration assignment, by reportId. |
| `GuestConfigurationHCRPAssignmentReports_List` | `SELECT` | `guestConfigurationAssignmentName, machineName, resourceGroupName, subscriptionId` | List all reports for the guest configuration assignment, latest report first. |
