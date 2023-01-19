---
title: locations_config
hide_title: false
hide_table_of_contents: false
keywords:
  - locations_config
  - clouddeploy
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
<tr><td><b>Name</b></td><td><code>locations_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.clouddeploy.locations_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the configuration. |
| `supportedVersions` | `array` | All supported versions of Skaffold. |
| `defaultSkaffoldVersion` | `string` | Default Skaffold version that is assigned when a Release is created without specifying a Skaffold version. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_getConfig` | `SELECT` | `locationsId, projectsId` |
