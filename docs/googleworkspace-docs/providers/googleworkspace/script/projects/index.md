---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
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
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.script.projects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `parentId` | `string` | The parent's Drive ID that the script will be attached to. This is usually the ID of a Google Document or Google Sheet. This filed is optional, and if not set, a stand-alone script will be created. |
| `scriptId` | `string` | The script project's Drive ID. |
| `title` | `string` | The title for the project. |
| `updateTime` | `string` | When the script was last updated. |
| `createTime` | `string` | When the script was created. |
| `creator` | `object` | A simple user profile resource. |
| `lastModifyUser` | `object` | A simple user profile resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `scriptId` | Gets a script project's metadata. |
| `create` | `INSERT` |  | Creates a new, empty script project with no script files and a base manifest file. |
| `updateContent` | `EXEC` | `scriptId` | Updates the content of the specified script project. This content is stored as the HEAD version, and is used when the script is executed as a trigger, in the script editor, in add-on preview mode, or as a web app or Apps Script API in development mode. This clears all the existing files in the project. |
