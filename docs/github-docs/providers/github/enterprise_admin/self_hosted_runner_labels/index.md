---
title: self_hosted_runner_labels
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
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
<tr><td><b>Id</b></td><td><code>github.enterprise_admin.self_hosted_runner_labels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `total_count` | `integer` |
| `labels` | `array` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_labels_for_self_hosted_runner_for_enterprise` | `SELECT` | `enterprise, runner_id` | Lists all labels for a self-hosted runner configured in an enterprise.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. |
| `add_custom_labels_to_self_hosted_runner_for_enterprise` | `INSERT` | `enterprise, runner_id, data__labels` | Add custom labels to a self-hosted runner configured in an enterprise.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. |
| `remove_all_custom_labels_from_self_hosted_runner_for_enterprise` | `DELETE` | `enterprise, runner_id` | Remove all custom labels from a self-hosted runner configured in an<br />enterprise. Returns the remaining read-only labels from the runner.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. |
| `remove_custom_label_from_self_hosted_runner_for_enterprise` | `DELETE` | `enterprise, name, runner_id` | Remove a custom label from a self-hosted runner configured<br />in an enterprise. Returns the remaining labels from the runner.<br /><br />This endpoint returns a `404 Not Found` status if the custom label is not<br />present on the runner.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. |
| `set_custom_labels_for_self_hosted_runner_for_enterprise` | `EXEC` | `enterprise, runner_id, data__labels` | Remove all previous custom labels and set the new custom labels for a specific<br />self-hosted runner configured in an enterprise.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. |
