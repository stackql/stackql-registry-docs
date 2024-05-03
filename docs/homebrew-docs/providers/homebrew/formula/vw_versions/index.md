---
title: vw_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_versions
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
<tr><td><b>Name</b></td><td><code>vw_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="homebrew.formula.vw_versions" /></td></tr>
</tbody></table>

## Fields
> This resource is a view. For the view definition, please refer to the provider spec in the [stackql-provider-registry](https://github.com/stackql/stackql-provider-registry/blob/dev/providers/src/homebrew/v00.00.00000/services/formula.yaml), located under `components -> x-stackQL-resources -> vw_versions`.

| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="bottle_available" /> ||
| <CopyableCode code="formula_name" /> | `text` |
| <CopyableCode code="head_version" /> ||
| <CopyableCode code="stable_version" /> ||
## Methods
No additional methods available for this resource
