---
title: orgs
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs
  - migrations
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
<tr><td><b>Name</b></td><td><code>orgs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.migrations.orgs" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete_archive_for_org" /> | `EXEC` | <CopyableCode code="migration_id, org" /> | Deletes a previous migration archive. Migration archives are automatically deleted after seven days. |
| <CopyableCode code="download_archive_for_org" /> | `EXEC` | <CopyableCode code="migration_id, org" /> | Fetches the URL to a migration archive. |
