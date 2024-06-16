---
title: simplified_solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - simplified_solutions
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
<tr><td><b>Name</b></td><td><code>simplified_solutions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.help.simplified_solutions" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="scope, simplifiedSolutionsResourceName" /> | Get the simplified Solutions using the applicable solutionResourceName while creating the simplified Solutions. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="scope, simplifiedSolutionsResourceName" /> | Creates Simplified Solutions for an Azure subscription using 'solutionId' from Discovery Solutions as the input. &lt;br/&gt;&lt;br/&gt; Simplified Solutions API makes the consumption of solutions APIs easier while still providing access to the same powerful solutions rendered in Solutions API. With Simplified Solutions, users don't have to worry about stitching together the article using replacement maps and can use the content in the API response to directly render as HTML content.&lt;br/&gt; |
