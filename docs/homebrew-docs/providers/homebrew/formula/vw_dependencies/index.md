---
title: vw_dependencies
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_dependencies
  - formula
  - homebrew    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and report on Homebrew packages using SQL
custom_edit_url: null
image: /img/providers/homebrew/stackql-homebrew-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vw_dependencies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="homebrew.formula.vw_dependencies" /></td></tr>
</tbody></table>

## Fields
> This resource is a view. For the view definition, please refer to the provider spec in the [stackql-provider-registry](https://github.com/stackql/stackql-provider-registry/blob/dev/providers/src/homebrew/v00.00.00000/services/formula.yaml), located under `components -> x-stackQL-resources -> vw_dependencies`.

| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="build_dependencies" /> ||
| <CopyableCode code="dependencies" /> ||
| <CopyableCode code="formula_name" /> | `text` |
| <CopyableCode code="head_dependencies" /> ||
| <CopyableCode code="optional_dependencies" /> ||
| <CopyableCode code="recommended_dependencies" /> ||
| <CopyableCode code="test_dependencies" /> ||
## Methods
No additional methods available for this resource
