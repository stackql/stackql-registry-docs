---
title: alert_instances
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
<tr><td><b>Name</b></td><td><code>alert_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.code_scanning.alert_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `ref` | `string` | The full Git reference, formatted as `refs/heads/&#x7B;branch name&#x7D;`,<br />`refs/pull/&#x7B;number&#x7D;/merge`, or `refs/pull/&#x7B;number&#x7D;/head`. |
| `location` | `object` | Describe a region within a file for the alert. |
| `html_url` | `string` |  |
| `environment` | `string` | Identifies the variable values associated with the environment in which the analysis that generated this alert instance was performed, such as the language that was analyzed. |
| `state` | `string` | State of a code scanning alert. |
| `category` | `string` | Identifies the configuration under which the analysis was executed. Used to distinguish between multiple analyses for the same tool and commit, but performed on different languages or different parts of the code. |
| `message` | `object` |  |
| `analysis_key` | `string` | Identifies the configuration under which the analysis was executed. For example, in GitHub Actions this includes the workflow filename and job name. |
| `classifications` | `array` | Classifications that have been applied to the file that triggered the alert.<br />For example identifying it as documentation, or a generated file. |
| `commit_sha` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_alert_instances` | `SELECT` | `alert_number, owner, repo` |
