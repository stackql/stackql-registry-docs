---
title: discovery_solution_nlp
hide_title: false
hide_table_of_contents: false
keywords:
  - discovery_solution_nlp
  - help
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
<tr><td><b>Name</b></td><td><code>discovery_solution_nlp</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.help.discovery_solution_nlp" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="discover_solutions" /> | `EXEC` | <CopyableCode code="data__issueSummary" /> | Search for relevant Azure Diagnostics, Solutions and Troubleshooters using a natural language issue summary. |
| <CopyableCode code="discover_solutions_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId, data__issueSummary" /> | Search for relevant Azure Diagnostics, Solutions and Troubleshooters using a natural language issue summary and subscription. |
