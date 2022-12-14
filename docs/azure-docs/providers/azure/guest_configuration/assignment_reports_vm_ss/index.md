---
title: assignment_reports_vm_ss
hide_title: false
hide_table_of_contents: false
keywords:
  - assignment_reports_vm_ss
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
<tr><td><b>Name</b></td><td><code>assignment_reports_vm_ss</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.guest_configuration.assignment_reports_vm_ss</code></td></tr>
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
| `GuestConfigurationAssignmentReportsVMSS_Get` | `SELECT` | `id, name, resourceGroupName, subscriptionId, vmssName` | Get a report for the VMSS guest configuration assignment, by reportId. |
| `GuestConfigurationAssignmentReportsVMSS_List` | `SELECT` | `name, resourceGroupName, subscriptionId, vmssName` | List all reports for the VMSS guest configuration assignment, latest report first. |
