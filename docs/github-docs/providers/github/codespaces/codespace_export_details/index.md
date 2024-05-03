---
title: codespace_export_details
hide_title: false
hide_table_of_contents: false
keywords:
  - codespace_export_details
  - codespaces
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
<tr><td><b>Name</b></td><td><code>codespace_export_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.codespaces.codespace_export_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id for the export details |
| <CopyableCode code="branch" /> | `string` | Name of the exported branch |
| <CopyableCode code="completed_at" /> | `string` | Completion time of the last export operation |
| <CopyableCode code="export_url" /> | `string` | Url for fetching export details |
| <CopyableCode code="html_url" /> | `string` | Web url for the exported branch |
| <CopyableCode code="sha" /> | `string` | Git commit SHA of the exported branch |
| <CopyableCode code="state" /> | `string` | State of the latest export |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_export_details_for_authenticated_user" /> | `SELECT` | <CopyableCode code="codespace_name, export_id" /> |
