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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="notebooks.instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Output only. Unique ID of the resource. |
| <CopyableCode code="name" /> | `string` | Output only. The name of this notebook instance. Format: `projects/&#123;project_id&#125;/locations/&#123;location&#125;/instances/&#123;instance_id&#125;` |
| <CopyableCode code="createTime" /> | `string` | Output only. Instance creation time. |
| <CopyableCode code="creator" /> | `string` | Output only. Email address of entity that sent original CreateInstance request. |
| <CopyableCode code="disableProxyAccess" /> | `boolean` | Optional. If true, the notebook instance will not register with the proxy. |
| <CopyableCode code="gceSetup" /> | `object` | The definition of how to configure a VM instance outside of Resources and Identity. |
| <CopyableCode code="healthInfo" /> | `object` | Output only. Additional information about instance health. Example: healthInfo": &#123; "docker_proxy_agent_status": "1", "docker_status": "1", "jupyterlab_api_status": "-1", "jupyterlab_status": "-1", "updated": "2020-10-18 09:40:03.573409" &#125; |
| <CopyableCode code="healthState" /> | `string` | Output only. Instance health_state. |
| <CopyableCode code="instanceOwners" /> | `array` | Optional. Input only. The owner of this instance after creation. Format: `alias@example.com` Currently supports one owner only. If not specified, all of the service account users of your VM instance's service account can use the instance. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels to apply to this instance. These can be later modified by the UpdateInstance method. |
| <CopyableCode code="proxyUri" /> | `string` | Output only. The proxy endpoint that is used to access the Jupyter notebook. |
| <CopyableCode code="state" /> | `string` | Output only. The state of this instance. |
| <CopyableCode code="thirdPartyProxyUrl" /> | `string` | Output only. The workforce pools proxy endpoint that is used to access the Jupyter notebook. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Instance update time. |
| <CopyableCode code="upgradeHistory" /> | `array` | Output only. The upgrade history of this instance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Gets details of a single Instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists instances in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Instance in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Deletes a single Instance. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists instances in a given project and location. |
| <CopyableCode code="check_upgradability" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Checks whether a notebook instance is upgradable. |
| <CopyableCode code="diagnose" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Creates a Diagnostic File and runs Diagnostic Tool given an Instance. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | UpdateInstance updates an Instance. |
| <CopyableCode code="report_info_system" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Allows notebook instances to report their latest instance information to the Notebooks API server. The server will merge the reported information to the instance metadata store. Do not use this method directly. |
| <CopyableCode code="reset" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Resets a notebook instance. |
| <CopyableCode code="resize_disk" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Resize a notebook instance disk to a higher capacity. |
| <CopyableCode code="rollback" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Rollbacks a notebook instance to the previous version. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Starts a notebook instance. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Stops a notebook instance. |
| <CopyableCode code="upgrade" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Upgrades a notebook instance to the latest version. |
| <CopyableCode code="upgrade_system" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Allows notebook instances to upgrade themselves. Do not use this method directly. |
