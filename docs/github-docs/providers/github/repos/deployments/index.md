---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
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
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | Unique identifier of the deployment |
| <CopyableCode code="description" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="creator" /> | `object` | A GitHub user. |
| <CopyableCode code="environment" /> | `string` | Name for the target deployment environment. |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="original_environment" /> | `string` |  |
| <CopyableCode code="payload" /> | `` |  |
| <CopyableCode code="performed_via_github_app" /> | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| <CopyableCode code="production_environment" /> | `boolean` | Specifies if the given environment is one that end-users directly interact with. Default: false. |
| <CopyableCode code="ref" /> | `string` | The ref to deploy. This can be a branch, tag, or sha. |
| <CopyableCode code="repository_url" /> | `string` |  |
| <CopyableCode code="sha" /> | `string` |  |
| <CopyableCode code="statuses_url" /> | `string` |  |
| <CopyableCode code="task" /> | `string` | Parameter to specify a task to execute |
| <CopyableCode code="transient_environment" /> | `boolean` | Specifies if the given environment is will no longer exist at some point in the future. Default: false. |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_deployment" /> | `SELECT` | <CopyableCode code="deployment_id, owner, repo" /> |  |
| <CopyableCode code="list_deployments" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Simple filtering of deployments is available via query parameters: |
| <CopyableCode code="create_deployment" /> | `INSERT` | <CopyableCode code="owner, repo, data__ref" /> | Deployments offer a few configurable parameters with certain defaults.<br /><br />The `ref` parameter can be any named branch, tag, or SHA. At GitHub we often deploy branches and verify them<br />before we merge a pull request.<br /><br />The `environment` parameter allows deployments to be issued to different runtime environments. Teams often have<br />multiple environments for verifying their applications, such as `production`, `staging`, and `qa`. This parameter<br />makes it easier to track which environments have requested deployments. The default environment is `production`.<br /><br />The `auto_merge` parameter is used to ensure that the requested ref is not behind the repository's default branch. If<br />the ref _is_ behind the default branch for the repository, we will attempt to merge it for you. If the merge succeeds,<br />the API will return a successful merge commit. If merge conflicts prevent the merge from succeeding, the API will<br />return a failure response.<br /><br />By default, [commit statuses](https://docs.github.com/rest/commits/statuses) for every submitted context must be in a `success`<br />state. The `required_contexts` parameter allows you to specify a subset of contexts that must be `success`, or to<br />specify contexts that have not yet been submitted. You are not required to use commit statuses to deploy. If you do<br />not require any contexts or create any commit statuses, the deployment will always succeed.<br /><br />The `payload` parameter is available for any extra information that a deployment system might need. It is a JSON text<br />field that will be passed on when a deployment event is dispatched.<br /><br />The `task` parameter is used by the deployment system to allow different execution paths. In the web world this might<br />be `deploy:migrations` to run schema changes on the system. In the compiled world this could be a flag to compile an<br />application with debugging enabled.<br /><br />Users with `repo` or `repo_deployment` scopes can create a deployment for a given ref.<br /><br />Merged branch response:<br /><br />You will see this response when GitHub automatically merges the base branch into the topic branch instead of creating<br />a deployment. This auto-merge happens when:<br />*   Auto-merge option is enabled in the repository<br />*   Topic branch does not include the latest changes on the base branch, which is `master` in the response example<br />*   There are no merge conflicts<br /><br />If there are no new commits in the base branch, a new request to create a deployment should give a successful<br />response.<br /><br />Merge conflict response:<br /><br />This error happens when the `auto_merge` option is enabled and when the default branch (in this case `master`), can't<br />be merged into the branch that's being deployed (in this case `topic-branch`), due to merge conflicts.<br /><br />Failed commit status checks:<br /><br />This error happens when the `required_contexts` parameter indicates that one or more contexts need to have a `success`<br />status for the commit to be deployed, but one or more of the required contexts do not have a state of `success`. |
| <CopyableCode code="delete_deployment" /> | `DELETE` | <CopyableCode code="deployment_id, owner, repo" /> | If the repository only has one deployment, you can delete the deployment regardless of its status. If the repository has more than one deployment, you can only delete inactive deployments. This ensures that repositories with multiple deployments will always have an active deployment. Anyone with `repo` or `repo_deployment` scopes can delete a deployment.<br /><br />To set a deployment as inactive, you must:<br /><br />*   Create a new deployment that is active so that the system has a record of the current state, then delete the previously active deployment.<br />*   Mark the active deployment as inactive by adding any non-successful deployment status.<br /><br />For more information, see "[Create a deployment](https://docs.github.com/rest/deployments/deployments/#create-a-deployment)" and "[Create a deployment status](https://docs.github.com/rest/deployments/statuses#create-a-deployment-status)." |
