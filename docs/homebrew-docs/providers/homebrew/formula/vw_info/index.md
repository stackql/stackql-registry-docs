---
title: vw_info
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_info
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
<tr><td><b>Name</b></td><td><code>vw_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="homebrew.formula.vw_info" /></td></tr>
</tbody></table>

## Fields
> This resource is a view. For the view definition, please refer to the provider spec in the [stackql-provider-registry](https://github.com/stackql/stackql-provider-registry/blob/dev/providers/src/homebrew/v00.00.00000/services/formula.yaml), located under `components -> x-stackQL-resources -> vw_info`.

| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="deprecated" /> | `boolean` |
| <CopyableCode code="disabled" /> | `boolean` |
| <CopyableCode code="formula_name" /> | `text` |
| <CopyableCode code="full_name" /> | `text` |
| <CopyableCode code="generated_date" /> | `text` |
| <CopyableCode code="homepage" /> | `text` |
| <CopyableCode code="latest_version" /> ||
| <CopyableCode code="license" /> | `text` |
## Methods
No additional methods available for this resource
