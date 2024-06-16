---
title: scoping_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - scoping_configuration
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
<tr><td><b>Name</b></td><td><code>scoping_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_compliance_automation.scoping_configuration" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="reportName, scopingConfigurationName" /> | Get the AppComplianceAutomation scoping configuration of the specific report. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="reportName" /> | Returns a list format of the singleton scopingConfiguration for a specified report. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="reportName, scopingConfigurationName, data__properties" /> | Get the AppComplianceAutomation scoping configuration of the specific report. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="reportName, scopingConfigurationName" /> | Clean the AppComplianceAutomation scoping configuration of the specific report. |
