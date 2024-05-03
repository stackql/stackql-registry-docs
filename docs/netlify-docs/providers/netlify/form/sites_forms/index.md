---
title: sites_forms
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_forms
  - form
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
<tr><td><b>Name</b></td><td><code>sites_forms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.form.sites_forms" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="fields" /> | `array` |
| <CopyableCode code="paths" /> | `array` |
| <CopyableCode code="site_id" /> | `string` |
| <CopyableCode code="submission_count" /> | `integer` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="listSiteForms" /> | `SELECT` | <CopyableCode code="site_id" /> |
| <CopyableCode code="deleteSiteForm" /> | `DELETE` | <CopyableCode code="form_id, site_id" /> |
