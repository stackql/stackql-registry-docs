---
title: analyses
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
<tr><td><b>Name</b></td><td><code>analyses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.code_scanning.analyses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier for this analysis. |
| `error` | `string` |  |
| `warning` | `string` | Warning generated when processing the analysis |
| `sarif_id` | `string` | An identifier for the upload. |
| `tool` | `object` |  |
| `results_count` | `integer` | The total number of results in the analysis. |
| `commit_sha` | `string` | The SHA of the commit to which the analysis you are uploading relates. |
| `environment` | `string` | Identifies the variable values associated with the environment in which this analysis was performed. |
| `ref` | `string` | The full Git reference, formatted as `refs/heads/&#x7B;branch name&#x7D;`,<br />`refs/pull/&#x7B;number&#x7D;/merge`, or `refs/pull/&#x7B;number&#x7D;/head`. |
| `rules_count` | `integer` | The total number of rules used in the analysis. |
| `created_at` | `string` | The time that the analysis was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `deletable` | `boolean` |  |
| `category` | `string` | Identifies the configuration under which the analysis was executed. Used to distinguish between multiple analyses for the same tool and commit, but performed on different languages or different parts of the code. |
| `url` | `string` | The REST API URL of the analysis resource. |
| `analysis_key` | `string` | Identifies the configuration under which the analysis was executed. For example, in GitHub Actions this includes the workflow filename and job name. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_analysis` | `SELECT` | `analysis_id, owner, repo` | Gets a specified code scanning analysis for a repository.<br />You must use an access token with the `security_events` scope to use this endpoint with private repos,<br />the `public_repo` scope also grants permission to read security events on public repos only.<br />GitHub Apps must have the `security_events` read permission to use this endpoint.<br /><br />The default JSON response contains fields that describe the analysis.<br />This includes the Git reference and commit SHA to which the analysis relates,<br />the datetime of the analysis, the name of the code scanning tool,<br />and the number of alerts.<br /><br />The `rules_count` field in the default response give the number of rules<br />that were run in the analysis.<br />For very old analyses this data is not available,<br />and `0` is returned in this field.<br /><br />If you use the Accept header `application/sarif+json`,<br />the response contains the analysis data that was uploaded.<br />This is formatted as<br />[SARIF version 2.1.0](https://docs.oasis-open.org/sarif/sarif/v2.1.0/cs01/sarif-v2.1.0-cs01.html). |
| `list_recent_analyses` | `SELECT` | `owner, repo` | Lists the details of all code scanning analyses for a repository,<br />starting with the most recent.<br />The response is paginated and you can use the `page` and `per_page` parameters<br />to list the analyses you're interested in.<br />By default 30 analyses are listed per page.<br /><br />The `rules_count` field in the response give the number of rules<br />that were run in the analysis.<br />For very old analyses this data is not available,<br />and `0` is returned in this field.<br /><br />You must use an access token with the `security_events` scope to use this endpoint with private repos,<br />the `public_repo` scope also grants permission to read security events on public repos only.<br />GitHub Apps must have the `security_events` read permission to use this endpoint.<br /><br />**Deprecation notice**:<br />The `tool_name` field is deprecated and will, in future, not be included in the response for this endpoint. The example response reflects this change. The tool name can now be found inside the `tool` field. |
| `delete_analysis` | `DELETE` | `analysis_id, owner, repo` | Deletes a specified code scanning analysis from a repository. For<br />private repositories, you must use an access token with the `repo` scope. For public repositories,<br />you must use an access token with `public_repo` scope.<br />GitHub Apps must have the `security_events` write permission to use this endpoint.<br /><br />You can delete one analysis at a time.<br />To delete a series of analyses, start with the most recent analysis and work backwards.<br />Conceptually, the process is similar to the undo function in a text editor.<br /><br />When you list the analyses for a repository,<br />one or more will be identified as deletable in the response:<br /><br />```<br />"deletable": true<br />```<br /><br />An analysis is deletable when it's the most recent in a set of analyses.<br />Typically, a repository will have multiple sets of analyses<br />for each enabled code scanning tool,<br />where a set is determined by a unique combination of analysis values:<br /><br />* `ref`<br />* `tool`<br />* `analysis_key`<br />* `environment`<br /><br />If you attempt to delete an analysis that is not the most recent in a set,<br />you'll get a 400 response with the message:<br /><br />```<br />Analysis specified is not deletable.<br />```<br /><br />The response from a successful `DELETE` operation provides you with<br />two alternative URLs for deleting the next analysis in the set:<br />`next_analysis_url` and `confirm_delete_url`.<br />Use the `next_analysis_url` URL if you want to avoid accidentally deleting the final analysis<br />in a set. This is a useful option if you want to preserve at least one analysis<br />for the specified tool in your repository.<br />Use the `confirm_delete_url` URL if you are content to remove all analyses for a tool.<br />When you delete the last analysis in a set, the value of `next_analysis_url` and `confirm_delete_url`<br />in the 200 response is `null`.<br /><br />As an example of the deletion process,<br />let's imagine that you added a workflow that configured a particular code scanning tool<br />to analyze the code in a repository. This tool has added 15 analyses:<br />10 on the default branch, and another 5 on a topic branch.<br />You therefore have two separate sets of analyses for this tool.<br />You've now decided that you want to remove all of the analyses for the tool.<br />To do this you must make 15 separate deletion requests.<br />To start, you must find an analysis that's identified as deletable.<br />Each set of analyses always has one that's identified as deletable.<br />Having found the deletable analysis for one of the two sets,<br />delete this analysis and then continue deleting the next analysis in the set until they're all deleted.<br />Then repeat the process for the second set.<br />The procedure therefore consists of a nested loop:<br /><br />**Outer loop**:<br />* List the analyses for the repository, filtered by tool.<br />* Parse this list to find a deletable analysis. If found:<br /><br />  **Inner loop**:<br />  * Delete the identified analysis.<br />  * Parse the response for the value of `confirm_delete_url` and, if found, use this in the next iteration.<br /><br />The above process assumes that you want to remove all trace of the tool's analyses from the GitHub user interface, for the specified repository, and it therefore uses the `confirm_delete_url` value. Alternatively, you could use the `next_analysis_url` value, which would leave the last analysis in each set undeleted to avoid removing a tool's analysis entirely. |
