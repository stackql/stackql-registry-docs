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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.composer.environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the environment, in the form: "projects/&#123;projectId&#125;/locations/&#123;locationId&#125;/environments/&#123;environmentId&#125;" EnvironmentId must start with a lowercase letter followed by up to 63 lowercase letters, numbers, or hyphens, and cannot end with a hyphen. |
| <CopyableCode code="config" /> | `object` | Configuration information for an environment. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which this environment was created. |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels for this environment. The labels map can contain no more than 64 entries. Entries of the labels map are UTF8 strings that comply with the following restrictions: * Keys must conform to regexp: \p&#123;Ll&#125;\p&#123;Lo&#125;&#123;0,62&#125; * Values must conform to regexp: [\p&#123;Ll&#125;\p&#123;Lo&#125;\p&#123;N&#125;_-]&#123;0,63&#125; * Both keys and values are additionally constrained to be &lt;= 128 bytes in size. |
| <CopyableCode code="state" /> | `string` | The current state of the environment. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time at which this environment was last modified. |
| <CopyableCode code="uuid" /> | `string` | Output only. The UUID (Universally Unique IDentifier) associated with this environment. This value is generated when the environment is created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Get an existing environment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List environments. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a new environment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Delete an environment. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | List environments. |
| <CopyableCode code="database_failover" /> | `EXEC` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Triggers database failover (only for highly resilient environments). |
| <CopyableCode code="execute_airflow_command" /> | `EXEC` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Executes Airflow CLI command. |
| <CopyableCode code="load_snapshot" /> | `EXEC` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Loads a snapshot of a Cloud Composer environment. As a result of this operation, a snapshot of environment's specified in LoadSnapshotRequest is loaded into the environment. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Update an environment. |
| <CopyableCode code="poll_airflow_command" /> | `EXEC` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Polls Airflow CLI command execution and fetches logs. |
| <CopyableCode code="save_snapshot" /> | `EXEC` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Creates a snapshots of a Cloud Composer environment. As a result of this operation, snapshot of environment's state is stored in a location specified in the SaveSnapshotRequest. |
| <CopyableCode code="stop_airflow_command" /> | `EXEC` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Stops Airflow CLI command execution. |
