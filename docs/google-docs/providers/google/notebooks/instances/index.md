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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.notebooks.instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Output only. Unique ID of the resource. |
| <CopyableCode code="name" /> | `string` | Output only. The name of this notebook instance. Format: `projects/{project_id}/locations/{location}/instances/{instance_id}` |
| <CopyableCode code="createTime" /> | `string` | Output only. Instance creation time. |
| <CopyableCode code="creator" /> | `string` | Output only. Email address of entity that sent original CreateInstance request. |
| <CopyableCode code="disableProxyAccess" /> | `boolean` | Optional. If true, the notebook instance will not register with the proxy. |
| <CopyableCode code="gceSetup" /> | `object` | The definition of how to configure a VM instance outside of Resources and Identity. |
| <CopyableCode code="healthInfo" /> | `object` | Output only. Additional information about instance health. Example: healthInfo": { "docker_proxy_agent_status": "1", "docker_status": "1", "jupyterlab_api_status": "-1", "jupyterlab_status": "-1", "updated": "2020-10-18 09:40:03.573409" } |
| <CopyableCode code="healthState" /> | `string` | Output only. Instance health_state. |
| <CopyableCode code="instanceOwners" /> | `array` | Optional. Input only. The owner of this instance after creation. Format: `alias@example.com` Currently supports one owner only. If not specified, all of the service account users of your VM instance's service account can use the instance. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels to apply to this instance. These can be later modified by the UpdateInstance method. |
| <CopyableCode code="proxyUri" /> | `string` | Output only. The proxy endpoint that is used to access the Jupyter notebook. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use for Zone Isolation. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use for Zone Separation. |
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
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="instancesId, locationsId, projectsId" /> | UpdateInstance updates an Instance. |
| <CopyableCode code="check_upgradability" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Checks whether a notebook instance is upgradable. |
| <CopyableCode code="diagnose" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Creates a Diagnostic File and runs Diagnostic Tool given an Instance. |
| <CopyableCode code="report_info_system" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Allows notebook instances to report their latest instance information to the Notebooks API server. The server will merge the reported information to the instance metadata store. Do not use this method directly. |
| <CopyableCode code="reset" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Resets a notebook instance. |
| <CopyableCode code="resize_disk" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Resize a notebook instance disk to a higher capacity. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | RestoreInstance restores an Instance from a BackupSource. |
| <CopyableCode code="rollback" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Rollbacks a notebook instance to the previous version. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Starts a notebook instance. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Stops a notebook instance. |
| <CopyableCode code="upgrade" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Upgrades a notebook instance to the latest version. |
| <CopyableCode code="upgrade_system" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Allows notebook instances to upgrade themselves. Do not use this method directly. |

## `SELECT` examples

Lists instances in a given project and location.

```sql
SELECT
id,
name,
createTime,
creator,
disableProxyAccess,
gceSetup,
healthInfo,
healthState,
instanceOwners,
labels,
proxyUri,
satisfiesPzi,
satisfiesPzs,
state,
thirdPartyProxyUrl,
updateTime,
upgradeHistory
FROM google.notebooks.instances
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instances</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.notebooks.instances (
locationsId,
projectsId,
gceSetup,
instanceOwners,
disableProxyAccess,
labels
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ gceSetup }}',
'{{ instanceOwners }}',
true|false,
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: gceSetup
      value:
        - name: machineType
          value: '{{ machineType }}'
        - name: minCpuPlatform
          value: '{{ minCpuPlatform }}'
        - name: acceleratorConfigs
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: serviceAccounts
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: vmImage
          value:
            - name: project
              value: '{{ project }}'
            - name: name
              value: '{{ name }}'
            - name: family
              value: '{{ family }}'
        - name: containerImage
          value:
            - name: repository
              value: '{{ repository }}'
            - name: tag
              value: '{{ tag }}'
        - name: bootDisk
          value:
            - name: diskSizeGb
              value: '{{ diskSizeGb }}'
            - name: diskType
              value: '{{ diskType }}'
            - name: diskEncryption
              value: '{{ diskEncryption }}'
            - name: kmsKey
              value: '{{ kmsKey }}'
        - name: dataDisks
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: shieldedInstanceConfig
          value:
            - name: enableSecureBoot
              value: '{{ enableSecureBoot }}'
            - name: enableVtpm
              value: '{{ enableVtpm }}'
            - name: enableIntegrityMonitoring
              value: '{{ enableIntegrityMonitoring }}'
        - name: networkInterfaces
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: disablePublicIp
          value: '{{ disablePublicIp }}'
        - name: tags
          value:
            - name: type
              value: '{{ type }}'
        - name: metadata
          value: '{{ metadata }}'
        - name: enableIpForwarding
          value: '{{ enableIpForwarding }}'
        - name: gpuDriverConfig
          value:
            - name: enableGpuDriver
              value: '{{ enableGpuDriver }}'
            - name: customGpuDriverPath
              value: '{{ customGpuDriverPath }}'
    - name: instanceOwners
      value:
        - name: type
          value: '{{ type }}'
    - name: disableProxyAccess
      value: '{{ disableProxyAccess }}'
    - name: labels
      value: '{{ labels }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>instances</code> resource.

```sql
/*+ update */
UPDATE google.notebooks.instances
SET 
gceSetup = '{{ gceSetup }}',
instanceOwners = '{{ instanceOwners }}',
disableProxyAccess = true|false,
labels = '{{ labels }}'
WHERE 
instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>instances</code> resource.

```sql
/*+ delete */
DELETE FROM google.notebooks.instances
WHERE instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
