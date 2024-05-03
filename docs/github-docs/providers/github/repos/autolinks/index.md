---
title: autolinks
hide_title: false
hide_table_of_contents: false
keywords:
  - autolinks
  - repos
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
<tr><td><b>Name</b></td><td><code>autolinks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.autolinks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="is_alphanumeric" /> | `boolean` | Whether this autolink reference matches alphanumeric characters. If false, this autolink reference only matches numeric characters. |
| <CopyableCode code="key_prefix" /> | `string` | The prefix of a key that is linkified. |
| <CopyableCode code="url_template" /> | `string` | A template for the target URL that is generated if a key was found. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_autolink" /> | `SELECT` | <CopyableCode code="autolink_id, owner, repo" /> | This returns a single autolink reference by ID that was configured for the given repository.<br /><br />Information about autolinks are only available to repository administrators. |
| <CopyableCode code="list_autolinks" /> | `SELECT` | <CopyableCode code="owner, repo" /> | This returns a list of autolinks configured for the given repository.<br /><br />Information about autolinks are only available to repository administrators. |
| <CopyableCode code="create_autolink" /> | `INSERT` | <CopyableCode code="owner, repo, data__key_prefix, data__url_template" /> | Users with admin access to the repository can create an autolink. |
| <CopyableCode code="delete_autolink" /> | `DELETE` | <CopyableCode code="autolink_id, owner, repo" /> | This deletes a single autolink reference by ID that was configured for the given repository.<br /><br />Information about autolinks are only available to repository administrators. |
