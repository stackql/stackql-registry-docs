---
title: solution
hide_title: false
hide_table_of_contents: false
keywords:
  - solution
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
<tr><td><b>Name</b></td><td><code>solution</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.help.solution" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="scope, solutionResourceName" /> | Get the solution using the applicable solutionResourceName while creating the solution. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="scope, solutionResourceName" /> | Creates a solution for the specific Azure resource or subscription using the inputs ‘solutionId and requiredInputs’ from discovery solutions. &lt;br/&gt; Azure solutions comprise a comprehensive library of self-help resources that have been thoughtfully curated by Azure engineers to aid customers in resolving typical troubleshooting issues. These solutions encompass: &lt;br/&gt; (1.) Dynamic and context-aware diagnostics, guided troubleshooting wizards, and data visualizations. &lt;br/&gt; (2.) Rich instructional video tutorials and illustrative diagrams and images. &lt;br/&gt; (3.) Thoughtfully assembled textual troubleshooting instructions. &lt;br/&gt; All these components are seamlessly converged into unified solutions tailored to address a specific support problem area. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="scope, solutionResourceName" /> | Update the requiredInputs or additional information needed to execute the solution  |
| <CopyableCode code="warm_up" /> | `EXEC` | <CopyableCode code="scope, solutionResourceName" /> | Warm up the solution resource by preloading asynchronous diagnostics results into cache |
