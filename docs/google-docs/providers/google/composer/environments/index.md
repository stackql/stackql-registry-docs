---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - composer
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
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.composer.environments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `environments` | `array` | The list of environments returned by a ListEnvironmentsRequest. |
| `nextPageToken` | `string` | The page token used to query for the next page if one exists. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `environmentsId, locationsId, projectsId` | Get an existing environment. |
| `list` | `SELECT` | `locationsId, projectsId` | List environments. |
| `create` | `INSERT` | `locationsId, projectsId` | Create a new environment. |
| `delete` | `DELETE` | `environmentsId, locationsId, projectsId` | Delete an environment. |
| `database_failover` | `EXEC` | `environmentsId, locationsId, projectsId` | Triggers database failover (only for highly resilient environments). |
| `execute_airflow_command` | `EXEC` | `environmentsId, locationsId, projectsId` | Executes Airflow CLI command. |
| `load_snapshot` | `EXEC` | `environmentsId, locationsId, projectsId` | Loads a snapshot of a Cloud Composer environment. As a result of this operation, a snapshot of environment's specified in LoadSnapshotRequest is loaded into the environment. |
| `patch` | `EXEC` | `environmentsId, locationsId, projectsId` | Update an environment. |
| `poll_airflow_command` | `EXEC` | `environmentsId, locationsId, projectsId` | Polls Airflow CLI command execution and fetches logs. |
| `save_snapshot` | `EXEC` | `environmentsId, locationsId, projectsId` | Creates a snapshots of a Cloud Composer environment. As a result of this operation, snapshot of environment's state is stored in a location specified in the SaveSnapshotRequest. |
| `stop_airflow_command` | `EXEC` | `environmentsId, locationsId, projectsId` | Stops Airflow CLI command execution. |
