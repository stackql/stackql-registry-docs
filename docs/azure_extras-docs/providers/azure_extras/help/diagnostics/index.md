---
title: diagnostics
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostics
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
<tr><td><b>Name</b></td><td><code>diagnostics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.help.diagnostics" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diagnosticsResourceName, scope" /> | Get the diagnostics using the 'diagnosticsResourceName' you chose while creating the diagnostic. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="diagnosticsResourceName, scope" /> | Creates a diagnostic for the specific resource using solutionId and requiredInputs* from discovery solutions. &lt;br/&gt;Diagnostics are powerful solutions that access product resources or other relevant data and provide the root cause of the issue and the steps to address the issue.&lt;br/&gt;&lt;br/&gt; &lt;b&gt;Note: &lt;/b&gt; ‘requiredInputs’ from Discovery solutions response must be passed via ‘additionalParameters’ as an input to Diagnostics API. |
