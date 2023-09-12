---
title: repos_sarifs
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_sarifs
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
<tr><td><b>Name</b></td><td><code>repos_sarifs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.code_scanning.repos_sarifs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `errors` | `array` | Any errors that ocurred during processing of the delivery. |
| `processing_status` | `string` | `pending` files have not yet been processed, while `complete` means results from the SARIF have been stored. `failed` files have either not been processed at all, or could only be partially processed. |
| `analyses_url` | `string` | The REST API URL for getting the analyses associated with the upload. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_sarif` | `SELECT` | `owner, repo, sarif_id` | Gets information about a SARIF upload, including the status and the URL of the analysis that was uploaded so that you can retrieve details of the analysis. For more information, see "[Get a code scanning analysis for a repository](/rest/code-scanning/code-scanning#get-a-code-scanning-analysis-for-a-repository)." You must use an access token with the `security_events` scope to use this endpoint with private repos, the `public_repo` scope also grants permission to read security events on public repos only. GitHub Apps must have the `security_events` read permission to use this endpoint. |
| `upload_sarif` | `EXEC` | `owner, repo, data__commit_sha, data__ref, data__sarif` | Uploads SARIF data containing the results of a code scanning analysis to make the results available in a repository. You must use an access token with the `security_events` scope to use this endpoint for private repositories. You can also use tokens with the `public_repo` scope for public repositories only. GitHub Apps must have the `security_events` write permission to use this endpoint. For troubleshooting information, see "[Troubleshooting SARIF uploads](https://docs.github.com/code-security/code-scanning/troubleshooting-sarif)."<br /><br />There are two places where you can upload code scanning results.<br /> - If you upload to a pull request, for example `--ref refs/pull/42/merge` or `--ref refs/pull/42/head`, then the results appear as alerts in a pull request check. For more information, see "[Triaging code scanning alerts in pull requests](/code-security/secure-coding/triaging-code-scanning-alerts-in-pull-requests)."<br /> - If you upload to a branch, for example `--ref refs/heads/my-branch`, then the results appear in the **Security** tab for your repository. For more information, see "[Managing code scanning alerts for your repository](/code-security/secure-coding/managing-code-scanning-alerts-for-your-repository#viewing-the-alerts-for-a-repository)."<br /><br />You must compress the SARIF-formatted analysis data that you want to upload, using `gzip`, and then encode it as a Base64 format string. For example:<br /><br />```<br />gzip -c analysis-data.sarif \| base64 -w0<br />```<br />&lt;br&gt;<br />SARIF upload supports a maximum number of entries per the following data objects, and an analysis will be rejected if any of these objects is above its maximum value. For some objects, there are additional values over which the entries will be ignored while keeping the most important entries whenever applicable.<br />To get the most out of your analysis when it includes data above the supported limits, try to optimize the analysis configuration. For example, for the CodeQL tool, identify and remove the most noisy queries. For more information, see "[SARIF results exceed one or more limits](https://docs.github.com/code-security/code-scanning/troubleshooting-sarif/results-exceed-limit)."<br /><br /><br />\| **SARIF data**                   \| **Maximum values** \| **Additional limits**                                                            \|<br />\|----------------------------------\|:------------------:\|----------------------------------------------------------------------------------\|<br />\| Runs per file                    \|         20         \|                                                                                  \|<br />\| Results per run                  \|       25,000       \| Only the top 5,000 results will be included, prioritized by severity.            \|<br />\| Rules per run                    \|       25,000       \|                                                                                  \|<br />\| Tool extensions per run          \|        100         \|                                                                                  \|<br />\| Thread Flow Locations per result \|       10,000       \| Only the top 1,000 Thread Flow Locations will be included, using prioritization. \|<br />\| Location per result	             \|       1,000        \| Only 100 locations will be included.                                             \|<br />\| Tags per rule	                   \|         20         \| Only 10 tags will be included.                                                   \|<br /><br /><br />The `202 Accepted` response includes an `id` value.<br />You can use this ID to check the status of the upload by using it in the `/sarifs/&#123;sarif_id&#125;` endpoint.<br />For more information, see "[Get information about a SARIF upload](/rest/code-scanning/code-scanning#get-information-about-a-sarif-upload)." |
