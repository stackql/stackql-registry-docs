---
title: codes_of_conduct
hide_title: false
hide_table_of_contents: false
keywords:
  - codes_of_conduct
  - codes_of_conduct
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>codes_of_conduct</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.codes_of_conduct.codes_of_conduct" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="body" /> | `string` |
| <CopyableCode code="html_url" /> | `string` |
| <CopyableCode code="key" /> | `string` |
| <CopyableCode code="url" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_all_codes_of_conduct" /> | `SELECT` |  | Returns array of all GitHub's codes of conduct. |
| <CopyableCode code="get_conduct_code" /> | `SELECT` | <CopyableCode code="key" /> | Returns information about the specified GitHub code of conduct. |
