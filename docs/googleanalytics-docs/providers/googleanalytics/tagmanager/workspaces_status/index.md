---
title: workspaces_status
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces_status
  - tagmanager
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.tagmanager.workspaces_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `mergeConflict` | `array` | The merge conflict after sync. |
| `workspaceChange` | `array` | Entities that have been changed in the workspace. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `accounts_containers_workspaces_getStatus` | `SELECT` | `accountsId, containersId, workspacesId` |
