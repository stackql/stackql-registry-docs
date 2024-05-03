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
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="reportName, data__properties" /> | Create a new AppComplianceAutomation report or update an exiting AppComplianceAutomation report. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="reportName" /> | Delete an AppComplianceAutomation report. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="reportName" /> | Update an exiting AppComplianceAutomation report. |
