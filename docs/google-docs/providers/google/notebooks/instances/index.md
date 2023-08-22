---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - notebooks
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
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.notebooks.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Output only. Unique ID of the resource. |
| `name` | `string` | Output only. The name of this notebook instance. Format: `projects/&#123;project_id&#125;/locations/&#123;location&#125;/instances/&#123;instance_id&#125;` |
| `upgradeHistory` | `array` | Output only. The upgrade history of this instance. |
| `updateTime` | `string` | Output only. Instance update time. |
| `proxyUri` | `string` | Output only. The proxy endpoint that is used to access the Jupyter notebook. |
| `healthInfo` | `object` | Output only. Additional information about instance health. Example: healthInfo": &#123; "docker_proxy_agent_status": "1", "docker_status": "1", "jupyterlab_api_status": "-1", "jupyterlab_status": "-1", "updated": "2020-10-18 09:40:03.573409" &#125; |
| `healthState` | `string` | Output only. Instance health_state. |
| `creator` | `string` | Output only. Email address of entity that sent original CreateInstance request. |
| `createTime` | `string` | Output only. Instance creation time. |
| `labels` | `object` | Optional. Labels to apply to this instance. These can be later modified by the UpdateInstance method. |
| `state` | `string` | Output only. The state of this instance. |
| `gceSetup` | `object` | The definition of how to configure a VM instance outside of Resources and Identity. |
| `disableProxyAccess` | `boolean` | Optional. If true, the notebook instance will not register with the proxy. |
| `instanceOwners` | `array` | Optional. Input only. The owner of this instance after creation. Format: `alias@example.com` Currently supports one owner only. If not specified, all of the service account users of your VM instance's service account can use the instance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `instancesId, locationsId, projectsId` | Gets details of a single Instance. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists instances in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new Instance in a given project and location. |
| `delete` | `DELETE` | `instancesId, locationsId, projectsId` | Deletes a single Instance. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists instances in a given project and location. |
| `check_upgradability` | `EXEC` | `instancesId, locationsId, projectsId` | Checks whether a notebook instance is upgradable. |
| `diagnose` | `EXEC` | `instancesId, locationsId, projectsId` | Creates a Diagnostic File and runs Diagnostic Tool given an Instance. |
| `patch` | `EXEC` | `instancesId, locationsId, projectsId` | UpdateInstance updates an Instance. |
| `report_info_system` | `EXEC` | `instancesId, locationsId, projectsId` | Allows notebook instances to report their latest instance information to the Notebooks API server. The server will merge the reported information to the instance metadata store. Do not use this method directly. |
| `reset` | `EXEC` | `instancesId, locationsId, projectsId` | Resets a notebook instance. |
| `rollback` | `EXEC` | `instancesId, locationsId, projectsId` | Rollbacks a notebook instance to the previous version. |
| `start` | `EXEC` | `instancesId, locationsId, projectsId` | Starts a notebook instance. |
| `stop` | `EXEC` | `instancesId, locationsId, projectsId` | Stops a notebook instance. |
| `upgrade` | `EXEC` | `instancesId, locationsId, projectsId` | Upgrades a notebook instance to the latest version. |
| `upgrade_system` | `EXEC` | `instancesId, locationsId, projectsId` | Allows notebook instances to upgrade themselves. Do not use this method directly. |
