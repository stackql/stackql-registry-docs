---
title: issues
hide_title: false
hide_table_of_contents: false
keywords:
  - issues
  - contactcenterinsights
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>issues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contactcenterinsights.issues</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name of the issue. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/issueModels/&#123;issue_model&#125;/issues/&#123;issue&#125; |
| `updateTime` | `string` | Output only. The most recent time that this issue was updated. |
| `createTime` | `string` | Output only. The time at which this issue was created. |
| `displayName` | `string` | The representative name for the issue. |
| `sampleUtterances` | `array` | Output only. Resource names of the sample representative utterances that match to this issue. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `issueModelsId, issuesId, locationsId, projectsId` | Gets an issue. |
| `list` | `SELECT` | `issueModelsId, locationsId, projectsId` | Lists issues. |
| `delete` | `DELETE` | `issueModelsId, issuesId, locationsId, projectsId` | Deletes an issue. |
| `patch` | `EXEC` | `issueModelsId, issuesId, locationsId, projectsId` | Updates an issue. |
