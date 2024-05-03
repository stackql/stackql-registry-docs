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
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="scope, solutionResourceName" /> | Creates a solution for the specific Azure resource or subscription using the inputs ‘solutionId and requiredInputs’ from discovery solutions. &lt;br/&gt; Azure solutions comprise a comprehensive library of self-help resources that have been thoughtfully curated by Azure engineers to aid customers in resolving typical troubleshooting issues. These solutions encompass (1.) dynamic and context-aware diagnostics, guided troubleshooting wizards, and data visualizations, (2.) rich instructional video tutorials and illustrative diagrams and images, and (3.) thoughtfully assembled textual troubleshooting instructions. All these components are seamlessly converged into unified solutions tailored to address a specific support problem area. Each solution type may require one or more ‘requiredParameters’ that are required to execute the individual solution component. In the absence of the ‘requiredParameters’ it is likely that some of the solutions might fail execution, and you might see an empty response. &lt;br/&gt;&lt;br/&gt; &lt;b&gt;Note:&lt;/b&gt;  &lt;br/&gt;1. ‘requiredInputs’ from Discovery solutions response must be passed via ‘parameters’ in the request body of Solutions API. &lt;br/&gt;2. ‘requiredParameters’ from the Solutions response is the same as ‘ additionalParameters’ in the request for diagnostics &lt;br/&gt;3. ‘requiredParameters’ from the Solutions response is the same as ‘properties.parameters’ in the request for Troubleshooters |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="scope, solutionResourceName" /> | Update the requiredInputs or additional information needed to execute the solution  |
