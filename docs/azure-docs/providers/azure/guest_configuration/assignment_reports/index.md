---
title: assignment_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - assignment_reports
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assignment_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.guest_configuration.assignment_reports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ARM resource id of the report for the guest configuration assignment. |
| <CopyableCode code="name" /> | `string` | GUID that identifies the guest configuration assignment report under a subscription, resource group. |
| <CopyableCode code="properties" /> | `object` | Report for the guest configuration assignment. Report contains information such as compliance status, reason, and more. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="guestConfigurationAssignmentName, reportId, resourceGroupName, subscriptionId, vmName" /> | Get a report for the guest configuration assignment, by reportId. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="guestConfigurationAssignmentName, resourceGroupName, subscriptionId, vmName" /> | List all reports for the guest configuration assignment, latest report first. |
