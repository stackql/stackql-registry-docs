---
title: default_setup
hide_title: false
hide_table_of_contents: false
keywords:
  - default_setup
  - code_scanning
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
<tr><td><b>Name</b></td><td><code>default_setup</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.code_scanning.default_setup" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="languages" /> | `array` | Languages to be analysed. |
| <CopyableCode code="query_suite" /> | `string` | CodeQL query suite to be used. |
| <CopyableCode code="schedule" /> | `string` | The frequency of the periodic analysis. |
| <CopyableCode code="state" /> | `string` | Code scanning default setup has been configured or not. |
| <CopyableCode code="updated_at" /> | `string` | Timestamp of latest configuration update. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_default_setup" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Gets a code scanning default setup configuration.<br />You must use an access token with the `repo` scope to use this endpoint with private repos or the `public_repo`<br />scope for public repos. GitHub Apps must have the `repo` write permission to use this endpoint. |
| <CopyableCode code="update_default_setup" /> | `EXEC` | <CopyableCode code="owner, repo, data__state" /> | Updates a code scanning default setup configuration.<br />You must use an access token with the `repo` scope to use this endpoint with private repos or the `public_repo`<br />scope for public repos. GitHub Apps must have the `repo` write permission to use this endpoint. |
