---
title: workflow_run_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_run_logs
  - actions
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
<tr><td><b>Name</b></td><td><code>workflow_run_logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.actions.workflow_run_logs" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete_workflow_run_logs" /> | `DELETE` | <CopyableCode code="owner, repo, run_id" /> | Deletes all logs for a workflow run. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `actions:write` permission to use this endpoint. |
| <CopyableCode code="download_workflow_run_attempt_logs" /> | `EXEC` | <CopyableCode code="attempt_number, owner, repo, run_id" /> | Gets a redirect URL to download an archive of log files for a specific workflow run attempt. This link expires after<br />1 minute. Look for `Location:` in the response header to find the URL for the download. Anyone with read access to<br />the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope.<br />GitHub Apps must have the `actions:read` permission to use this endpoint. |
| <CopyableCode code="download_workflow_run_logs" /> | `EXEC` | <CopyableCode code="owner, repo, run_id" /> | Gets a redirect URL to download an archive of log files for a workflow run. This link expires after 1 minute. Look for<br />`Location:` in the response header to find the URL for the download. Anyone with read access to the repository can use<br />this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have<br />the `actions:read` permission to use this endpoint. |
