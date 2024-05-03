---
title: submissions
hide_title: false
hide_table_of_contents: false
keywords:
  - submissions
  - submission
  - netlify    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Netlify resources using SQL
custom_edit_url: null
image: /img/providers/netlify/stackql-netlify-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>submissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.submission.submissions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="body" /> | `string` |
| <CopyableCode code="company" /> | `string` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="data" /> | `object` |
| <CopyableCode code="email" /> | `string` |
| <CopyableCode code="first_name" /> | `string` |
| <CopyableCode code="last_name" /> | `string` |
| <CopyableCode code="number" /> | `integer` |
| <CopyableCode code="site_url" /> | `string` |
| <CopyableCode code="summary" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="listFormSubmission" /> | `SELECT` | <CopyableCode code="submission_id" /> |
| <CopyableCode code="deleteSubmission" /> | `DELETE` | <CopyableCode code="submission_id" /> |
