---
title: releases_executable
hide_title: false
hide_table_of_contents: false
keywords:
  - releases_executable
  - firebaserules
  - firebase    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>releases_executable</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>firebase.firebaserules.releases_executable</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `executableVersion` | `string` | The Rules runtime version of the executable. |
| `language` | `string` | `Language` used to generate the executable bytes. |
| `rulesetName` | `string` | `Ruleset` name associated with the `Release` executable. |
| `syncTime` | `string` | Optional, indicates the freshness of the result. The response is guaranteed to be the latest within an interval up to the sync_time (inclusive). |
| `updateTime` | `string` | Timestamp for the most recent `Release.update_time`. |
| `executable` | `string` | Executable view of the `Ruleset` referenced by the `Release`. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_releases_getExecutable` | `SELECT` | `projectsId, releasesId:getExecutable` |
