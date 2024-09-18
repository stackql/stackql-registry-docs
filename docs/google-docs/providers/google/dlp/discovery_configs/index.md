---
title: discovery_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - discovery_configs
  - dlp
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

Creates, updates, deletes, gets or lists a <code>discovery_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>discovery_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dlp.discovery_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Unique resource name for the DiscoveryConfig, assigned by the service when the DiscoveryConfig is created, for example `projects/dlp-test-project/locations/global/discoveryConfigs/53234423`. |
| <CopyableCode code="actions" /> | `array` | Actions to execute at the completion of scanning. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of a DiscoveryConfig. |
| <CopyableCode code="displayName" /> | `string` | Display name (max 100 chars) |
| <CopyableCode code="errors" /> | `array` | Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared. |
| <CopyableCode code="inspectTemplates" /> | `array` | Detection logic for profile generation. Not all template features are used by Discovery. FindingLimits, include_quote and exclude_info_types have no impact on Discovery. Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including "global"). Each region is scanned using the applicable template. If no region-specific template is specified, but a "global" template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region's data will not be scanned. For more information, see https://cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency. |
| <CopyableCode code="lastRunTime" /> | `string` | Output only. The timestamp of the last time this config was executed. |
| <CopyableCode code="orgConfig" /> | `object` | Project and scan location information. Only set when the parent is an org. |
| <CopyableCode code="status" /> | `string` | Required. A status for this configuration. |
| <CopyableCode code="targets" /> | `array` | Target to match against for determining what to scan and how frequently. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp of a DiscoveryConfig. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_discovery_configs_get" /> | `SELECT` | <CopyableCode code="discoveryConfigsId, locationsId, organizationsId" /> | Gets a discovery configuration. |
| <CopyableCode code="organizations_locations_discovery_configs_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists discovery configurations. |
| <CopyableCode code="projects_locations_discovery_configs_get" /> | `SELECT` | <CopyableCode code="discoveryConfigsId, locationsId, projectsId" /> | Gets a discovery configuration. |
| <CopyableCode code="projects_locations_discovery_configs_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists discovery configurations. |
| <CopyableCode code="organizations_locations_discovery_configs_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates a config for discovery to scan and profile storage. |
| <CopyableCode code="projects_locations_discovery_configs_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a config for discovery to scan and profile storage. |
| <CopyableCode code="organizations_locations_discovery_configs_delete" /> | `DELETE` | <CopyableCode code="discoveryConfigsId, locationsId, organizationsId" /> | Deletes a discovery configuration. |
| <CopyableCode code="projects_locations_discovery_configs_delete" /> | `DELETE` | <CopyableCode code="discoveryConfigsId, locationsId, projectsId" /> | Deletes a discovery configuration. |
| <CopyableCode code="organizations_locations_discovery_configs_patch" /> | `UPDATE` | <CopyableCode code="discoveryConfigsId, locationsId, organizationsId" /> | Updates a discovery configuration. |
| <CopyableCode code="projects_locations_discovery_configs_patch" /> | `UPDATE` | <CopyableCode code="discoveryConfigsId, locationsId, projectsId" /> | Updates a discovery configuration. |

## `SELECT` examples

Lists discovery configurations.

```sql
SELECT
name,
actions,
createTime,
displayName,
errors,
inspectTemplates,
lastRunTime,
orgConfig,
status,
targets,
updateTime
FROM google.dlp.discovery_configs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>discovery_configs</code> resource.

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
INSERT INTO google.dlp.discovery_configs (
locationsId,
projectsId,
configId,
discoveryConfig
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ configId }}',
'{{ discoveryConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
configId: string
discoveryConfig:
  targets:
    - secretsTarget: {}
      cloudStorageTarget:
        conditions:
          createdAfter: string
          cloudStorageConditions:
            includedObjectAttributes:
              - type: string
                enum: string
                enumDescriptions: string
            includedBucketAttributes:
              - enum: string
                enumDescriptions: string
                type: string
          minAge: string
        disabled: {}
        filter:
          others: {}
          collection:
            includeRegexes:
              patterns:
                - cloudStorageRegex:
                    bucketNameRegex: string
                    projectIdRegex: string
          cloudStorageResourceReference:
            projectId: string
            bucketName: string
        generationCadence:
          refreshFrequency: string
          inspectTemplateModifiedCadence:
            frequency: string
      cloudSqlTarget:
        filter:
          collection:
            includeRegexes:
              patterns:
                - instanceRegex: string
                  databaseRegex: string
                  projectIdRegex: string
                  databaseResourceNameRegex: string
          databaseResourceReference:
            databaseResource: string
            projectId: string
            database: string
            instance: string
          others: {}
        generationCadence:
          schemaModifiedCadence:
            types:
              - enum: string
                enumDescriptions: string
                type: string
            frequency: string
          refreshFrequency: string
        conditions:
          types:
            - type: string
              enum: string
              enumDescriptions: string
          databaseEngines:
            - type: string
              enum: string
              enumDescriptions: string
      bigQueryTarget:
        filter:
          otherTables: {}
          tableReference:
            tableId: string
            datasetId: string
          tables:
            includeRegexes:
              patterns:
                - tableIdRegex: string
                  projectIdRegex: string
                  datasetIdRegex: string
        conditions:
          createdAfter: string
          orConditions:
            minRowCount: integer
            minAge: string
          typeCollection: string
          types:
            types:
              - enum: string
                enumDescriptions: string
                type: string
        cadence:
          schemaModifiedCadence:
            types:
              - enum: string
                type: string
                enumDescriptions: string
            frequency: string
          tableModifiedCadence:
            types:
              - enum: string
                enumDescriptions: string
                type: string
            frequency: string
          refreshFrequency: string
  status: string
  displayName: string
  updateTime: string
  lastRunTime: string
  inspectTemplates:
    - type: string
  createTime: string
  errors:
    - details:
        message: string
        code: integer
        details:
          - additionalProperties: any
            type: string
      timestamps:
        - format: string
          type: string
      extraInfo: string
  name: string
  actions:
    - tagResources:
        lowerDataRiskToLow: boolean
        tagConditions:
          - sensitivityScore:
              score: string
            tag:
              namespacedValue: string
        profileGenerationsToTag:
          - enumDescriptions: string
            type: string
            enum: string
      pubSubNotification:
        detailOfMessage: string
        event: string
        pubsubCondition:
          expressions:
            conditions:
              - minimumSensitivityScore: string
                minimumRiskScore: string
            logicalOperator: string
        topic: string
      exportData:
        profileTable:
          tableId: string
          projectId: string
          datasetId: string
      publishToScc: {}
      publishToChronicle: {}
  orgConfig:
    projectId: string
    location:
      folderId: string
      organizationId: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>discovery_configs</code> resource.

```sql
/*+ update */
UPDATE google.dlp.discovery_configs
SET 
updateMask = '{{ updateMask }}',
discoveryConfig = '{{ discoveryConfig }}'
WHERE 
discoveryConfigsId = '{{ discoveryConfigsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>discovery_configs</code> resource.

```sql
/*+ delete */
DELETE FROM google.dlp.discovery_configs
WHERE discoveryConfigsId = '{{ discoveryConfigsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
