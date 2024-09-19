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
      value: string
    - name: config
      value:
        - name: gkeCluster
          value: string
        - name: dagGcsPrefix
          value: string
        - name: nodeCount
          value: integer
        - name: softwareConfig
          value:
            - name: imageVersion
              value: string
            - name: airflowConfigOverrides
              value: object
            - name: pypiPackages
              value: object
            - name: envVariables
              value: object
            - name: pythonVersion
              value: string
            - name: schedulerCount
              value: integer
            - name: cloudDataLineageIntegration
              value:
                - name: enabled
                  value: boolean
            - name: webServerPluginsMode
              value: string
        - name: nodeConfig
          value:
            - name: location
              value: string
            - name: machineType
              value: string
            - name: network
              value: string
            - name: subnetwork
              value: string
            - name: diskSizeGb
              value: integer
            - name: oauthScopes
              value:
                - string
            - name: serviceAccount
              value: string
            - name: tags
              value:
                - string
            - name: ipAllocationPolicy
              value:
                - name: useIpAliases
                  value: boolean
                - name: clusterSecondaryRangeName
                  value: string
                - name: clusterIpv4CidrBlock
                  value: string
                - name: servicesSecondaryRangeName
                  value: string
                - name: servicesIpv4CidrBlock
                  value: string
            - name: enableIpMasqAgent
              value: boolean
            - name: composerNetworkAttachment
              value: string
            - name: composerInternalIpv4CidrBlock
              value: string
        - name: privateEnvironmentConfig
          value:
            - name: enablePrivateEnvironment
              value: boolean
            - name: enablePrivateBuildsOnly
              value: boolean
            - name: privateClusterConfig
              value:
                - name: enablePrivateEndpoint
                  value: boolean
                - name: masterIpv4CidrBlock
                  value: string
                - name: masterIpv4ReservedRange
                  value: string
            - name: webServerIpv4CidrBlock
              value: string
            - name: cloudSqlIpv4CidrBlock
              value: string
            - name: webServerIpv4ReservedRange
              value: string
            - name: cloudComposerNetworkIpv4CidrBlock
              value: string
            - name: cloudComposerNetworkIpv4ReservedRange
              value: string
            - name: enablePrivatelyUsedPublicIps
              value: boolean
            - name: cloudComposerConnectionSubnetwork
              value: string
            - name: networkingConfig
              value:
                - name: connectionType
                  value: string
        - name: webServerNetworkAccessControl
          value:
            - name: allowedIpRanges
              value:
                - - name: value
                    value: string
                  - name: description
                    value: string
        - name: databaseConfig
          value:
            - name: machineType
              value: string
            - name: zone
              value: string
        - name: webServerConfig
          value:
            - name: machineType
              value: string
        - name: encryptionConfig
          value:
            - name: kmsKeyName
              value: string
        - name: maintenanceWindow
          value:
            - name: startTime
              value: string
            - name: endTime
              value: string
            - name: recurrence
              value: string
        - name: workloadsConfig
          value:
            - name: scheduler
              value:
                - name: cpu
                  value: number
                - name: memoryGb
                  value: number
                - name: storageGb
                  value: number
                - name: count
                  value: integer
            - name: webServer
              value:
                - name: cpu
                  value: number
                - name: memoryGb
                  value: number
                - name: storageGb
                  value: number
            - name: worker
              value:
                - name: cpu
                  value: number
                - name: memoryGb
                  value: number
                - name: storageGb
                  value: number
                - name: minCount
                  value: integer
                - name: maxCount
                  value: integer
            - name: triggerer
              value:
                - name: count
                  value: integer
                - name: cpu
                  value: number
                - name: memoryGb
                  value: number
            - name: dagProcessor
              value:
                - name: cpu
                  value: number
                - name: memoryGb
                  value: number
                - name: storageGb
                  value: number
                - name: count
                  value: integer
        - name: environmentSize
          value: string
        - name: airflowUri
          value: string
        - name: airflowByoidUri
          value: string
        - name: masterAuthorizedNetworksConfig
          value:
            - name: enabled
              value: boolean
            - name: cidrBlocks
              value:
                - - name: displayName
                    value: string
                  - name: cidrBlock
                    value: string
        - name: recoveryConfig
          value:
            - name: scheduledSnapshotsConfig
              value:
                - name: enabled
                  value: boolean
                - name: snapshotLocation
                  value: string
                - name: snapshotCreationSchedule
                  value: string
                - name: timeZone
                  value: string
        - name: resilienceMode
          value: string
        - name: dataRetentionConfig
          value:
            - name: airflowMetadataRetentionConfig
              value:
                - name: retentionMode
                  value: string
                - name: retentionDays
                  value: integer
            - name: taskLogsRetentionConfig
              value:
                - name: storageMode
                  value: string
    - name: uuid
      value: string
    - name: state
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: labels
      value: object
    - name: satisfiesPzs
      value: boolean
    - name: satisfiesPzi
      value: boolean
    - name: storageConfig
      value:
        - name: bucket
          value: string

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
