---
title: evidence
hide_title: false
hide_table_of_contents: false
keywords:
  - evidence
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
<tr><td><b>Name</b></td><td><code>evidence</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_compliance_automation.evidence" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="evidenceName, reportName" /> | Get the evidence metadata |
| <CopyableCode code="list_by_report" /> | `SELECT` | <CopyableCode code="reportName" /> | Returns a paginated list of evidences for a specified report. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="evidenceName, reportName, data__properties" /> | Create or Update an evidence a specified report |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="evidenceName, reportName" /> | Delete an existent evidence from a specified report |
| <CopyableCode code="download" /> | `EXEC` | <CopyableCode code="evidenceName, reportName" /> | Download evidence file. |
