---
title: report
hide_title: false
hide_table_of_contents: false
keywords:
  - report
  - app_compliance_automation
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
<tr><td><b>Name</b></td><td><code>report</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.app_compliance_automation.report</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `reportName` | Get the AppComplianceAutomation report and its properties. |
| `create_or_update` | `INSERT` | `reportName, data__properties` | Create a new AppComplianceAutomation report or update an exiting AppComplianceAutomation report. |
| `delete` | `DELETE` | `reportName` | Delete an AppComplianceAutomation report. |
| `update` | `EXEC` | `reportName` | Update an exiting AppComplianceAutomation report. |
