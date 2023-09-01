---
title: preference_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - preference_sets
  - migrationcenter
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
<tr><td><b>Name</b></td><td><code>preference_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.migrationcenter.preference_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the preference set. |
| `description` | `string` | A description of the preference set. |
| `updateTime` | `string` | Output only. The timestamp when the preference set was last updated. |
| `virtualMachinePreferences` | `object` | VirtualMachinePreferences enables you to create sets of assumptions, for example, a geographical location and pricing track, for your migrated virtual machines. The set of preferences influence recommendations for migrating virtual machine assets. |
| `createTime` | `string` | Output only. The timestamp when the preference set was created. |
| `displayName` | `string` | User-friendly display name. Maximum length is 63 characters. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, preferenceSetsId, projectsId` | Gets the details of a preference set. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists all the preference sets in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new preference set in a given project and location. |
| `delete` | `DELETE` | `locationsId, preferenceSetsId, projectsId` | Deletes a preference set. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists all the preference sets in a given project and location. |
| `patch` | `EXEC` | `locationsId, preferenceSetsId, projectsId` | Updates the parameters of a preference set. |
