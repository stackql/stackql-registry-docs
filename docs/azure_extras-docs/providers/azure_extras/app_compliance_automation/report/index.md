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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>report</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_compliance_automation.report" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="reportName" /> | Get the AppComplianceAutomation report and its properties. |
| <CopyableCode code="list" /> | `SELECT` |  | Get the AppComplianceAutomation report list for the tenant. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="reportName, data__properties" /> | Create a new AppComplianceAutomation report or update an exiting AppComplianceAutomation report. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="reportName" /> | Delete an AppComplianceAutomation report. |
| <CopyableCode code="fix" /> | `EXEC` | <CopyableCode code="reportName" /> | Fix the AppComplianceAutomation report error. e.g: App Compliance Automation Tool service unregistered, automation removed. |
| <CopyableCode code="nested_resource_check_name_availability" /> | `EXEC` | <CopyableCode code="reportName" /> | Checks the report's nested resource name availability, e.g: Webhooks, Evidences, Snapshots. |
| <CopyableCode code="sync_cert_record" /> | `EXEC` | <CopyableCode code="reportName, data__certRecord" /> | Synchronize attestation record from app compliance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="reportName" /> | Update an exiting AppComplianceAutomation report. |
| <CopyableCode code="verify" /> | `EXEC` | <CopyableCode code="reportName" /> | Verify the AppComplianceAutomation report health status. |
