---
title: repos_alerts_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_alerts_instances
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repos_alerts_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.code_scanning.repos_alerts_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `classifications` | `array` | Classifications that have been applied to the file that triggered the alert.<br />For example identifying it as documentation, or a generated file. |
| `commit_sha` | `string` |  |
| `ref` | `string` | The full Git reference, formatted as `refs/heads/&lt;branch name&gt;`,<br />`refs/pull/&lt;number&gt;/merge`, or `refs/pull/&lt;number&gt;/head`. |
| `message` | `object` |  |
| `state` | `string` | State of a code scanning alert. |
| `category` | `string` | Identifies the configuration under which the analysis was executed. Used to distinguish between multiple analyses for the same tool and commit, but performed on different languages or different parts of the code. |
| `environment` | `string` | Identifies the variable values associated with the environment in which the analysis that generated this alert instance was performed, such as the language that was analyzed. |
| `analysis_key` | `string` | Identifies the configuration under which the analysis was executed. For example, in GitHub Actions this includes the workflow filename and job name. |
| `location` | `object` | Describe a region within a file for the alert. |
| `html_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_alert_instances` | `SELECT` | `alert_number, owner, repo` |
