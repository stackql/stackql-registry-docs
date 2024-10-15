---
title: workflows
hide_title: false
hide_table_of_contents: false
keywords:
  - workflows
  - developer_hub
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

Creates, updates, deletes, gets or lists a <code>workflows</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.developer_hub.workflows" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workflows', value: 'view', },
        { label: 'workflows', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="artifact_generation_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_pipeline_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="github_workflow_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="workflowName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Workflow properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workflowName" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, workflowName" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, workflowName" /> |  |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workflowName" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workflows', value: 'view', },
        { label: 'workflows', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
artifact_generation_properties,
azure_pipeline_profile,
github_workflow_profile,
location,
resourceGroupName,
subscriptionId,
tags,
workflowName
FROM azure_extras.developer_hub.vw_workflows
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure_extras.developer_hub.workflows
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workflows</code> resource.

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
INSERT INTO azure_extras.developer_hub.workflows (
resourceGroupName,
subscriptionId,
workflowName,
tags,
location,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workflowName }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: githubWorkflowProfile
          value:
            - name: repositoryOwner
              value: string
            - name: repositoryName
              value: string
            - name: branchName
              value: string
            - name: dockerfile
              value: string
            - name: dockerBuildContext
              value: string
            - name: deploymentProperties
              value:
                - name: manifestType
                  value: []
                - name: kubeManifestLocations
                  value:
                    - string
                - name: helmChartPath
                  value: string
                - name: helmValues
                  value: string
                - name: overrides
                  value: object
            - name: namespace
              value: string
            - name: acr
              value:
                - name: acrSubscriptionId
                  value: string
                - name: acrResourceGroup
                  value: string
                - name: acrRegistryName
                  value: string
                - name: acrRepositoryName
                  value: string
            - name: oidcCredentials
              value:
                - name: azureClientId
                  value: string
                - name: azureTenantId
                  value: string
            - name: aksResourceId
              value: string
            - name: prURL
              value: string
            - name: pullNumber
              value: integer
            - name: prStatus
              value: []
            - name: lastWorkflowRun
              value:
                - name: succeeded
                  value: boolean
                - name: workflowRunURL
                  value: string
                - name: lastRunAt
                  value: string
                - name: workflowRunStatus
                  value: []
            - name: authStatus
              value: []
        - name: artifactGenerationProperties
          value:
            - name: generationLanguage
              value: []
            - name: languageVersion
              value: string
            - name: builderVersion
              value: string
            - name: port
              value: string
            - name: appName
              value: string
            - name: dockerfileOutputDirectory
              value: string
            - name: manifestOutputDirectory
              value: string
            - name: dockerfileGenerationMode
              value: []
            - name: manifestGenerationMode
              value: []
            - name: manifestType
              value: []
            - name: imageName
              value: string
            - name: namespace
              value: string
            - name: imageTag
              value: string
        - name: azurePipelineProfile
          value:
            - name: repository
              value:
                - name: repositoryOwner
                  value: string
                - name: repositoryName
                  value: string
                - name: branchName
                  value: string
                - name: adoOrganization
                  value: string
                - name: projectName
                  value: string
            - name: armServiceConnection
              value: string
            - name: build
              value:
                - name: dockerfile
                  value: string
                - name: dockerBuildContext
                  value: string
            - name: namespace
              value: string
            - name: acr
              value: string
            - name: clusterId
              value: string
            - name: pullRequest
              value:
                - name: prURL
                  value: string
                - name: pullNumber
                  value: integer

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>workflows</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.developer_hub.workflows
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workflowName = '{{ workflowName }}';
```
