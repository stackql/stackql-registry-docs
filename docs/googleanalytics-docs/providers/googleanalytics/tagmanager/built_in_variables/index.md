---
title: built_in_variables
hide_title: false
hide_table_of_contents: false
keywords:
  - built_in_variables
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
<tr><td><b>Name</b></td><td><code>built_in_variables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.tagmanager.built_in_variables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Continuation token for fetching the next page of results. |
| `builtInVariable` | `array` | All GTM BuiltInVariables of a GTM container. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_containers_workspaces_built_in_variables_list` | `SELECT` | `accountsId, containersId, workspacesId` | Lists all the enabled Built-In Variables of a GTM Container. |
| `accounts_containers_workspaces_built_in_variables_delete` | `DELETE` | `accountsId, containersId, workspacesId` | Deletes one or more GTM Built-In Variables. |
| `accounts_containers_workspaces_built_in_variables_create` | `EXEC` | `accountsId, containersId, workspacesId` | Creates one or more GTM Built-In Variables. |
| `accounts_containers_workspaces_built_in_variables_revert` | `EXEC` | `accountsId, containersId, workspacesId` | Reverts changes to a GTM Built-In Variables in a GTM Workspace. |
