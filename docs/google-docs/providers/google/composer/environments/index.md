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
| `name` | `string` | The resource name of the environment, in the form: "projects/&#123;projectId&#125;/locations/&#123;locationId&#125;/environments/&#123;environmentId&#125;" EnvironmentId must start with a lowercase letter followed by up to 63 lowercase letters, numbers, or hyphens, and cannot end with a hyphen. |
| `createTime` | `string` | Output only. The time at which this environment was created. |
| `labels` | `object` | Optional. User-defined labels for this environment. The labels map can contain no more than 64 entries. Entries of the labels map are UTF8 strings that comply with the following restrictions: * Keys must conform to regexp: \p&#123;Ll&#125;\p&#123;Lo&#125;&#123;0,62&#125; * Values must conform to regexp: [\p&#123;Ll&#125;\p&#123;Lo&#125;\p&#123;N&#125;_-]&#123;0,63&#125; * Both keys and values are additionally constrained to be &lt;= 128 bytes in size. |
| `state` | `string` | The current state of the environment. |
| `updateTime` | `string` | Output only. The time at which this environment was last modified. |
| `uuid` | `string` | Output only. The UUID (Universally Unique IDentifier) associated with this environment. This value is generated when the environment is created. |
| `config` | `object` | Configuration information for an environment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `environmentsId, locationsId, projectsId` | Get an existing environment. |
| `list` | `SELECT` | `locationsId, projectsId` | List environments. |
| `create` | `INSERT` | `locationsId, projectsId` | Create a new environment. |
| `delete` | `DELETE` | `environmentsId, locationsId, projectsId` | Delete an environment. |
| `_list` | `EXEC` | `locationsId, projectsId` | List environments. |
| `database_failover` | `EXEC` | `environmentsId, locationsId, projectsId` | Triggers database failover (only for highly resilient environments). |
| `execute_airflow_command` | `EXEC` | `environmentsId, locationsId, projectsId` | Executes Airflow CLI command. |
| `load_snapshot` | `EXEC` | `environmentsId, locationsId, projectsId` | Loads a snapshot of a Cloud Composer environment. As a result of this operation, a snapshot of environment's specified in LoadSnapshotRequest is loaded into the environment. |
| `patch` | `EXEC` | `environmentsId, locationsId, projectsId` | Update an environment. |
| `poll_airflow_command` | `EXEC` | `environmentsId, locationsId, projectsId` | Polls Airflow CLI command execution and fetches logs. |
| `save_snapshot` | `EXEC` | `environmentsId, locationsId, projectsId` | Creates a snapshots of a Cloud Composer environment. As a result of this operation, snapshot of environment's state is stored in a location specified in the SaveSnapshotRequest. |
| `stop_airflow_command` | `EXEC` | `environmentsId, locationsId, projectsId` | Stops Airflow CLI command execution. |
