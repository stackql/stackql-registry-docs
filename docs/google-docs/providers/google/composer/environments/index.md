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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.composer.environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the environment, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}" EnvironmentId must start with a lowercase letter followed by up to 63 lowercase letters, numbers, or hyphens, and cannot end with a hyphen. |
| <CopyableCode code="config" /> | `object` | Configuration information for an environment. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which this environment was created. |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels for this environment. The labels map can contain no more than 64 entries. Entries of the labels map are UTF8 strings that comply with the following restrictions: * Keys must conform to regexp: \p{Ll}\p{Lo}{0,62} * Values must conform to regexp: [\p{Ll}\p{Lo}\p{N}_-]{0,63} * Both keys and values are additionally constrained to be <= 128 bytes in size. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="state" /> | `string` | The current state of the environment. |
| <CopyableCode code="storageConfig" /> | `object` | The configuration for data storage in the environment. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time at which this environment was last modified. |
| <CopyableCode code="uuid" /> | `string` | Output only. The UUID (Universally Unique IDentifier) associated with this environment. This value is generated when the environment is created. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Get an existing environment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List environments. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a new environment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Delete an environment. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Update an environment. |
| <CopyableCode code="check_upgrade" /> | `EXEC` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Check if an upgrade operation on the environment will succeed. In case of problems detailed info can be found in the returned Operation. |
| <CopyableCode code="database_failover" /> | `EXEC` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Triggers database failover (only for highly resilient environments). |
| <CopyableCode code="execute_airflow_command" /> | `EXEC` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Executes Airflow CLI command. |
| <CopyableCode code="load_snapshot" /> | `EXEC` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Loads a snapshot of a Cloud Composer environment. As a result of this operation, a snapshot of environment's specified in LoadSnapshotRequest is loaded into the environment. |
| <CopyableCode code="poll_airflow_command" /> | `EXEC` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Polls Airflow CLI command execution and fetches logs. |
| <CopyableCode code="save_snapshot" /> | `EXEC` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Creates a snapshots of a Cloud Composer environment. As a result of this operation, snapshot of environment's state is stored in a location specified in the SaveSnapshotRequest. |
| <CopyableCode code="stop_airflow_command" /> | `EXEC` | <CopyableCode code="environmentsId, locationsId, projectsId" /> | Stops Airflow CLI command execution. |

## `SELECT` examples

List environments.

```sql
SELECT
name,
config,
createTime,
labels,
satisfiesPzi,
satisfiesPzs,
state,
storageConfig,
updateTime,
uuid
FROM google.composer.environments
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>environments</code> resource.

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
INSERT INTO google.composer.environments (
locationsId,
projectsId,
name,
config,
uuid,
state,
labels,
storageConfig
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ config }}',
'{{ uuid }}',
'{{ state }}',
'{{ labels }}',
'{{ storageConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: config
      value:
        - name: gkeCluster
          value: '{{ gkeCluster }}'
        - name: dagGcsPrefix
          value: '{{ dagGcsPrefix }}'
        - name: nodeCount
          value: '{{ nodeCount }}'
        - name: softwareConfig
          value:
            - name: imageVersion
              value: '{{ imageVersion }}'
            - name: airflowConfigOverrides
              value: '{{ airflowConfigOverrides }}'
            - name: pypiPackages
              value: '{{ pypiPackages }}'
            - name: envVariables
              value: '{{ envVariables }}'
            - name: pythonVersion
              value: '{{ pythonVersion }}'
            - name: schedulerCount
              value: '{{ schedulerCount }}'
            - name: cloudDataLineageIntegration
              value:
                - name: enabled
                  value: '{{ enabled }}'
            - name: webServerPluginsMode
              value: '{{ webServerPluginsMode }}'
        - name: nodeConfig
          value:
            - name: location
              value: '{{ location }}'
            - name: machineType
              value: '{{ machineType }}'
            - name: network
              value: '{{ network }}'
            - name: subnetwork
              value: '{{ subnetwork }}'
            - name: diskSizeGb
              value: '{{ diskSizeGb }}'
            - name: oauthScopes
              value:
                - name: type
                  value: '{{ type }}'
            - name: serviceAccount
              value: '{{ serviceAccount }}'
            - name: tags
              value:
                - name: type
                  value: '{{ type }}'
            - name: ipAllocationPolicy
              value:
                - name: useIpAliases
                  value: '{{ useIpAliases }}'
                - name: clusterSecondaryRangeName
                  value: '{{ clusterSecondaryRangeName }}'
                - name: clusterIpv4CidrBlock
                  value: '{{ clusterIpv4CidrBlock }}'
                - name: servicesSecondaryRangeName
                  value: '{{ servicesSecondaryRangeName }}'
                - name: servicesIpv4CidrBlock
                  value: '{{ servicesIpv4CidrBlock }}'
            - name: enableIpMasqAgent
              value: '{{ enableIpMasqAgent }}'
            - name: composerNetworkAttachment
              value: '{{ composerNetworkAttachment }}'
            - name: composerInternalIpv4CidrBlock
              value: '{{ composerInternalIpv4CidrBlock }}'
        - name: privateEnvironmentConfig
          value:
            - name: enablePrivateEnvironment
              value: '{{ enablePrivateEnvironment }}'
            - name: enablePrivateBuildsOnly
              value: '{{ enablePrivateBuildsOnly }}'
            - name: privateClusterConfig
              value:
                - name: enablePrivateEndpoint
                  value: '{{ enablePrivateEndpoint }}'
                - name: masterIpv4CidrBlock
                  value: '{{ masterIpv4CidrBlock }}'
            - name: webServerIpv4CidrBlock
              value: '{{ webServerIpv4CidrBlock }}'
            - name: cloudSqlIpv4CidrBlock
              value: '{{ cloudSqlIpv4CidrBlock }}'
            - name: cloudComposerNetworkIpv4CidrBlock
              value: '{{ cloudComposerNetworkIpv4CidrBlock }}'
            - name: enablePrivatelyUsedPublicIps
              value: '{{ enablePrivatelyUsedPublicIps }}'
            - name: cloudComposerConnectionSubnetwork
              value: '{{ cloudComposerConnectionSubnetwork }}'
            - name: networkingConfig
              value:
                - name: connectionType
                  value: '{{ connectionType }}'
        - name: webServerNetworkAccessControl
          value:
            - name: allowedIpRanges
              value:
                - name: $ref
                  value: '{{ $ref }}'
        - name: databaseConfig
          value:
            - name: machineType
              value: '{{ machineType }}'
            - name: zone
              value: '{{ zone }}'
        - name: webServerConfig
          value:
            - name: machineType
              value: '{{ machineType }}'
        - name: encryptionConfig
          value:
            - name: kmsKeyName
              value: '{{ kmsKeyName }}'
        - name: maintenanceWindow
          value:
            - name: startTime
              value: '{{ startTime }}'
            - name: endTime
              value: '{{ endTime }}'
            - name: recurrence
              value: '{{ recurrence }}'
        - name: workloadsConfig
          value:
            - name: scheduler
              value:
                - name: cpu
                  value: '{{ cpu }}'
                - name: memoryGb
                  value: '{{ memoryGb }}'
                - name: storageGb
                  value: '{{ storageGb }}'
                - name: count
                  value: '{{ count }}'
            - name: webServer
              value:
                - name: cpu
                  value: '{{ cpu }}'
                - name: memoryGb
                  value: '{{ memoryGb }}'
                - name: storageGb
                  value: '{{ storageGb }}'
            - name: worker
              value:
                - name: cpu
                  value: '{{ cpu }}'
                - name: memoryGb
                  value: '{{ memoryGb }}'
                - name: storageGb
                  value: '{{ storageGb }}'
                - name: minCount
                  value: '{{ minCount }}'
                - name: maxCount
                  value: '{{ maxCount }}'
            - name: triggerer
              value:
                - name: count
                  value: '{{ count }}'
                - name: cpu
                  value: '{{ cpu }}'
                - name: memoryGb
                  value: '{{ memoryGb }}'
            - name: dagProcessor
              value:
                - name: cpu
                  value: '{{ cpu }}'
                - name: memoryGb
                  value: '{{ memoryGb }}'
                - name: storageGb
                  value: '{{ storageGb }}'
                - name: count
                  value: '{{ count }}'
        - name: environmentSize
          value: '{{ environmentSize }}'
        - name: airflowUri
          value: '{{ airflowUri }}'
        - name: masterAuthorizedNetworksConfig
          value:
            - name: enabled
              value: '{{ enabled }}'
            - name: cidrBlocks
              value:
                - name: $ref
                  value: '{{ $ref }}'
        - name: recoveryConfig
          value:
            - name: scheduledSnapshotsConfig
              value:
                - name: enabled
                  value: '{{ enabled }}'
                - name: snapshotLocation
                  value: '{{ snapshotLocation }}'
                - name: snapshotCreationSchedule
                  value: '{{ snapshotCreationSchedule }}'
                - name: timeZone
                  value: '{{ timeZone }}'
        - name: resilienceMode
          value: '{{ resilienceMode }}'
        - name: dataRetentionConfig
          value:
            - name: airflowMetadataRetentionConfig
              value:
                - name: retentionMode
                  value: '{{ retentionMode }}'
                - name: retentionDays
                  value: '{{ retentionDays }}'
            - name: taskLogsRetentionConfig
              value:
                - name: storageMode
                  value: '{{ storageMode }}'
    - name: uuid
      value: '{{ uuid }}'
    - name: state
      value: '{{ state }}'
    - name: labels
      value: '{{ labels }}'
    - name: storageConfig
      value:
        - name: bucket
          value: '{{ bucket }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>environments</code> resource.

```sql
/*+ update */
UPDATE google.composer.environments
SET 
name = '{{ name }}',
config = '{{ config }}',
uuid = '{{ uuid }}',
state = '{{ state }}',
labels = '{{ labels }}',
storageConfig = '{{ storageConfig }}'
WHERE 
environmentsId = '{{ environmentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>environments</code> resource.

```sql
/*+ delete */
DELETE FROM google.composer.environments
WHERE environmentsId = '{{ environmentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
