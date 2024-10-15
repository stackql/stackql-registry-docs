---
title: source_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - source_controls
  - sentinel
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

Creates, updates, deletes, gets or lists a <code>source_controls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>source_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.source_controls" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_source_controls', value: 'view', },
        { label: 'source_controls', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | field from the `properties` object |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag of the azure resource |
| <CopyableCode code="last_deployment_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="pull_request" /> | `text` | field from the `properties` object |
| <CopyableCode code="repo_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="repository" /> | `text` | field from the `properties` object |
| <CopyableCode code="repository_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="repository_resource_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_principal" /> | `text` | field from the `properties` object |
| <CopyableCode code="sourceControlId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | Describes source control properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sourceControlId, subscriptionId, workspaceName" /> | Gets a source control byt its identifier. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets all source controls, without source control items. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, sourceControlId, subscriptionId, workspaceName, data__properties" /> | Creates a source control. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sourceControlId, subscriptionId, workspaceName, data__properties" /> | Delete a source control. |

## `SELECT` examples

Gets all source controls, without source control items.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_source_controls', value: 'view', },
        { label: 'source_controls', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
description,
content_types,
display_name,
etag,
last_deployment_info,
pull_request,
repo_type,
repository,
repository_access,
repository_resource_info,
resourceGroupName,
service_principal,
sourceControlId,
subscriptionId,
version,
workspaceName
FROM azure.sentinel.vw_source_controls
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties
FROM azure.sentinel.source_controls
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>source_controls</code> resource.

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
INSERT INTO azure.sentinel.source_controls (
resourceGroupName,
sourceControlId,
subscriptionId,
workspaceName,
data__properties,
etag,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ sourceControlId }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__properties }}',
'{{ etag }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: etag
      value: string
    - name: properties
      value:
        - name: id
          value: string
        - name: version
          value: []
        - name: displayName
          value: string
        - name: description
          value: string
        - name: repoType
          value: []
        - name: contentTypes
          value:
            - []
        - name: repository
          value:
            - name: url
              value: string
            - name: branch
              value: string
            - name: displayUrl
              value: string
            - name: deploymentLogsUrl
              value: string
        - name: servicePrincipal
          value:
            - name: id
              value: string
            - name: tenantId
              value: string
            - name: appId
              value: string
            - name: credentialsExpireOn
              value: string
        - name: repositoryAccess
          value:
            - name: kind
              value: []
            - name: code
              value: string
            - name: state
              value: string
            - name: clientId
              value: string
            - name: token
              value: string
            - name: installationId
              value: string
        - name: repositoryResourceInfo
          value:
            - name: webhook
              value:
                - name: webhookId
                  value: string
                - name: webhookUrl
                  value: string
                - name: webhookSecretUpdateTime
                  value: string
                - name: rotateWebhookSecret
                  value: boolean
            - name: gitHubResourceInfo
              value:
                - name: appInstallationId
                  value: string
            - name: azureDevOpsResourceInfo
              value:
                - name: pipelineId
                  value: string
                - name: serviceConnectionId
                  value: string
        - name: lastDeploymentInfo
          value:
            - name: deploymentFetchStatus
              value: []
            - name: deployment
              value:
                - name: deploymentId
                  value: string
                - name: deploymentState
                  value: []
                - name: deploymentResult
                  value: []
                - name: deploymentTime
                  value: string
                - name: deploymentLogsUrl
                  value: string
            - name: message
              value: string
        - name: pullRequest
          value:
            - name: url
              value: string
            - name: state
              value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>source_controls</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sentinel.source_controls
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sourceControlId = '{{ sourceControlId }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}'
AND data__properties = '{{ data__properties }}';
```
