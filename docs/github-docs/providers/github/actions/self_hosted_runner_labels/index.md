---
title: self_hosted_runner_labels
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - actions
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>self_hosted_runner_labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.self_hosted_runner_labels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `labels` | `array` |
| `total_count` | `integer` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_labels_for_self_hosted_runner_for_org` | `SELECT` | `org, runner_id` | Lists all labels for a self-hosted runner configured in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `list_labels_for_self_hosted_runner_for_repo` | `SELECT` | `owner, repo, runner_id` | Lists all labels for a self-hosted runner configured in a repository.<br /><br />You must authenticate using an access token with the `repo` scope to use this<br />endpoint. |
| `add_custom_labels_to_self_hosted_runner_for_org` | `INSERT` | `org, runner_id, data__labels` | Add custom labels to a self-hosted runner configured in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `add_custom_labels_to_self_hosted_runner_for_repo` | `INSERT` | `owner, repo, runner_id, data__labels` | Add custom labels to a self-hosted runner configured in a repository.<br /><br />You must authenticate using an access token with the `repo` scope to use this<br />endpoint. |
| `remove_all_custom_labels_from_self_hosted_runner_for_org` | `DELETE` | `org, runner_id` | Remove all custom labels from a self-hosted runner configured in an<br />organization. Returns the remaining read-only labels from the runner.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `remove_all_custom_labels_from_self_hosted_runner_for_repo` | `DELETE` | `owner, repo, runner_id` | Remove all custom labels from a self-hosted runner configured in a<br />repository. Returns the remaining read-only labels from the runner.<br /><br />You must authenticate using an access token with the `repo` scope to use this<br />endpoint. |
| `remove_custom_label_from_self_hosted_runner_for_org` | `DELETE` | `name, org, runner_id` | Remove a custom label from a self-hosted runner configured<br />in an organization. Returns the remaining labels from the runner.<br /><br />This endpoint returns a `404 Not Found` status if the custom label is not<br />present on the runner.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `remove_custom_label_from_self_hosted_runner_for_repo` | `DELETE` | `name, owner, repo, runner_id` | Remove a custom label from a self-hosted runner configured<br />in a repository. Returns the remaining labels from the runner.<br /><br />This endpoint returns a `404 Not Found` status if the custom label is not<br />present on the runner.<br /><br />You must authenticate using an access token with the `repo` scope to use this<br />endpoint. |
| `set_custom_labels_for_self_hosted_runner_for_org` | `EXEC` | `org, runner_id, data__labels` | Remove all previous custom labels and set the new custom labels for a specific<br />self-hosted runner configured in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `set_custom_labels_for_self_hosted_runner_for_repo` | `EXEC` | `owner, repo, runner_id, data__labels` | Remove all previous custom labels and set the new custom labels for a specific<br />self-hosted runner configured in a repository.<br /><br />You must authenticate using an access token with the `repo` scope to use this<br />endpoint. |
