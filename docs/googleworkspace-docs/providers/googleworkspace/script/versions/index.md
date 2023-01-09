---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
  - script
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.script.versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The description for this version. |
| `createTime` | `string` | When the version was created. |
| `scriptId` | `string` | The script project's Drive ID. |
| `versionNumber` | `integer` | The incremental ID that is created by Apps Script when a version is created. This is system assigned number and is immutable once created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_versions_get` | `SELECT` | `scriptId, versionNumber` | Gets a version of a script project. |
| `projects_versions_list` | `SELECT` | `scriptId` | List the versions of a script project. |
| `projects_versions_create` | `INSERT` | `scriptId` | Creates a new immutable version using the current code, with a unique version number. |
