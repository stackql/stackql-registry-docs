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
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `issueModelsId, issuesId, locationsId, projectsId` | Gets an issue. |
| `list` | `SELECT` | `issueModelsId, locationsId, projectsId` | Lists issues. |
| `delete` | `DELETE` | `issueModelsId, issuesId, locationsId, projectsId` | Deletes an issue. |
| `patch` | `EXEC` | `issueModelsId, issuesId, locationsId, projectsId` | Updates an issue. |
