---
title: azure_dev_ops_repos
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_dev_ops_repos
  - security
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

Creates, updates, deletes, gets or lists a <code>azure_dev_ops_repos</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>azure_dev_ops_repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.azure_dev_ops_repos" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_azure_dev_ops_repos', value: 'view', },
        { label: 'azure_dev_ops_repos', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="actionable_remediation" /> | `text` | field from the `properties` object |
| <CopyableCode code="onboarding_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="orgName" /> | `text` | field from the `properties` object |
| <CopyableCode code="parent_org_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="parent_project_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="projectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_status_update_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="repoName" /> | `text` | field from the `properties` object |
| <CopyableCode code="repo_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="repo_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="securityConnectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="visibility" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Azure DevOps Repository properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="orgName, projectName, repoName, resourceGroupName, securityConnectorName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="orgName, projectName, resourceGroupName, securityConnectorName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="orgName, projectName, repoName, resourceGroupName, securityConnectorName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="orgName, projectName, repoName, resourceGroupName, securityConnectorName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_azure_dev_ops_repos', value: 'view', },
        { label: 'azure_dev_ops_repos', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
actionable_remediation,
onboarding_state,
orgName,
parent_org_name,
parent_project_name,
projectName,
provisioning_state,
provisioning_status_message,
provisioning_status_update_time_utc,
repoName,
repo_id,
repo_url,
resourceGroupName,
securityConnectorName,
subscriptionId,
system_data,
visibility
FROM azure.security.vw_azure_dev_ops_repos
WHERE orgName = '{{ orgName }}'
AND projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND securityConnectorName = '{{ securityConnectorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.security.azure_dev_ops_repos
WHERE orgName = '{{ orgName }}'
AND projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND securityConnectorName = '{{ securityConnectorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>azure_dev_ops_repos</code> resource.

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
INSERT INTO azure.security.azure_dev_ops_repos (
orgName,
projectName,
repoName,
resourceGroupName,
securityConnectorName,
subscriptionId,
systemData,
properties
)
SELECT 
'{{ orgName }}',
'{{ projectName }}',
'{{ repoName }}',
'{{ resourceGroupName }}',
'{{ securityConnectorName }}',
'{{ subscriptionId }}',
'{{ systemData }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: provisioningStatusMessage
          value: string
        - name: provisioningStatusUpdateTimeUtc
          value: string
        - name: provisioningState
          value: []
        - name: parentOrgName
          value: string
        - name: parentProjectName
          value: string
        - name: repoId
          value: string
        - name: repoUrl
          value: string
        - name: visibility
          value: string
        - name: onboardingState
          value: []
        - name: actionableRemediation
          value:
            - name: state
              value: []
            - name: categoryConfigurations
              value:
                - - name: minimumSeverityLevel
                    value: string
                  - name: category
                    value: []
            - name: branchConfiguration
              value:
                - name: branchNames
                  value:
                    - string
                - name: annotateDefaultBranch
                  value: []
            - name: inheritFromParentState
              value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>azure_dev_ops_repos</code> resource.

```sql
/*+ update */
UPDATE azure.security.azure_dev_ops_repos
SET 
systemData = '{{ systemData }}',
properties = '{{ properties }}'
WHERE 
orgName = '{{ orgName }}'
AND projectName = '{{ projectName }}'
AND repoName = '{{ repoName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND securityConnectorName = '{{ securityConnectorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
