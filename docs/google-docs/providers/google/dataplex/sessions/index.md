---
title: sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - sessions
  - dataplex
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
<tr><td><b>Name</b></td><td><code>sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.sessions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The relative resource name of the content, of the form: projects/&#123;project_id&#125;/locations/&#123;location_id&#125;/lakes/&#123;lake_id&#125;/environment/&#123;environment_id&#125;/sessions/&#123;session_id&#125; |
| `state` | `string` | Output only. State of Session |
| `userId` | `string` | Output only. Email of user running the session. |
| `createTime` | `string` | Output only. Session start time. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_lakes_environments_sessions_list` | `SELECT` | `environmentsId, lakesId, locationsId, projectsId` |
| `_projects_locations_lakes_environments_sessions_list` | `EXEC` | `environmentsId, lakesId, locationsId, projectsId` |
