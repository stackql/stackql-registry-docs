---
title: runner_applications
hide_title: false
hide_table_of_contents: false
keywords:
  - runner_applications
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
<tr><td><b>Name</b></td><td><code>runner_applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.actions.runner_applications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="architecture" /> | `string` |  |
| <CopyableCode code="download_url" /> | `string` |  |
| <CopyableCode code="filename" /> | `string` |  |
| <CopyableCode code="os" /> | `string` |  |
| <CopyableCode code="sha256_checksum" /> | `string` |  |
| <CopyableCode code="temp_download_token" /> | `string` | A short lived bearer token used to download the runner, if needed. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_runner_applications_for_org" /> | `SELECT` | <CopyableCode code="org" /> | Lists binaries for the runner application that you can download and run.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `administration` permission for repositories and the `organization_self_hosted_runners` permission for organizations.<br />Authenticated users must have admin access to repositories or organizations, or the `manage_runners:enterprise` scope for enterprises, to use these endpoints. |
| <CopyableCode code="list_runner_applications_for_repo" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Lists binaries for the runner application that you can download and run.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `administration` permission for repositories and the `organization_self_hosted_runners` permission for organizations.<br />Authenticated users must have admin access to repositories or organizations, or the `manage_runners:enterprise` scope for enterprises, to use these endpoints. |
