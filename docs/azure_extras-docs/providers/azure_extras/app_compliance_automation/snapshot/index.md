---
title: snapshot
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshot
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
<tr><td><b>Name</b></td><td><code>snapshot</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_compliance_automation.snapshot" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="reportName, snapshotName" /> | Get the AppComplianceAutomation snapshot and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="reportName" /> | Get the AppComplianceAutomation snapshot list. |
| <CopyableCode code="download" /> | `EXEC` | <CopyableCode code="reportName, snapshotName, data__downloadType" /> | Download compliance needs from snapshot, like: Compliance Report, Resource List. |
