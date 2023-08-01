---
title: custom_modules_descendant
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_modules_descendant
  - securitycenter
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
<tr><td><b>Name</b></td><td><code>custom_modules_descendant</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.custom_modules_descendant</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | If not empty, indicates that there may be more custom modules to be returned. |
| `securityHealthAnalyticsCustomModules` | `array` | Custom modules belonging to the requested parent and its descendants. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `folders_security_health_analytics_settings_custom_modules_list_descendant` | `SELECT` | `foldersId` |
| `organizations_security_health_analytics_settings_custom_modules_list_descendant` | `SELECT` | `organizationsId` |
| `projects_security_health_analytics_settings_custom_modules_list_descendant` | `SELECT` | `projectsId` |
