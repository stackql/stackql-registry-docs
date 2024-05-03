---
title: workflow_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_jobs
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
<tr><td><b>Name</b></td><td><code>workflow_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.actions.workflow_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="jobs" /> | `array` |
| <CopyableCode code="total_count" /> | `integer` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_job_for_workflow_run" /> | `SELECT` | <CopyableCode code="job_id, owner, repo" /> | Gets a specific job in a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| <CopyableCode code="list_jobs_for_workflow_run" /> | `SELECT` | <CopyableCode code="owner, repo, run_id" /> | Lists jobs for a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/rest/overview/resources-in-the-rest-api#parameters). |
| <CopyableCode code="list_jobs_for_workflow_run_attempt" /> | `SELECT` | <CopyableCode code="attempt_number, owner, repo, run_id" /> | Lists jobs for a specific workflow run attempt. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/rest/overview/resources-in-the-rest-api#parameters). |
| <CopyableCode code="download_job_logs_for_workflow_run" /> | `EXEC` | <CopyableCode code="job_id, owner, repo" /> | Gets a redirect URL to download a plain text file of logs for a workflow job. This link expires after 1 minute. Look<br />for `Location:` in the response header to find the URL for the download. Anyone with read access to the repository can<br />use this endpoint. If the repository is private you must use an access token with the `repo` scope. GitHub Apps must<br />have the `actions:read` permission to use this endpoint. |
