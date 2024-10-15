---
title: iac_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - iac_profiles
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

Creates, updates, deletes, gets or lists a <code>iac_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iac_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.developer_hub.iac_profiles" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_iac_profiles', value: 'view', },
        { label: 'iac_profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="github_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="iacProfileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="stages" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="templates" /> | `text` | field from the `properties` object |
| <CopyableCode code="terraform_profile" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of a IacProfile. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="iacProfileName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="iacProfileName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="iacProfileName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="export" /> | `EXEC` | <CopyableCode code="iacProfileName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="scale" /> | `EXEC` | <CopyableCode code="iacProfileName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="sync" /> | `EXEC` | <CopyableCode code="iacProfileName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="iacProfileName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_iac_profiles', value: 'view', },
        { label: 'iac_profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
etag,
github_profile,
iacProfileName,
location,
resourceGroupName,
stages,
subscriptionId,
tags,
templates,
terraform_profile
FROM azure_extras.developer_hub.vw_iac_profiles
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
location,
properties,
tags
FROM azure_extras.developer_hub.iac_profiles
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>iac_profiles</code> resource.

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
INSERT INTO azure_extras.developer_hub.iac_profiles (
iacProfileName,
resourceGroupName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ iacProfileName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: githubProfile
          value:
            - name: repositoryName
              value: string
            - name: repositoryMainBranch
              value: string
            - name: repositoryOwner
              value: string
            - name: authStatus
              value: []
            - name: pullNumber
              value: integer
            - name: prStatus
              value: []
            - name: branchName
              value: string
        - name: terraformProfile
          value:
            - name: storageAccountSubscription
              value: string
            - name: storageAccountResourceGroup
              value: string
            - name: storageAccountName
              value: string
            - name: storageContainerName
              value: string
        - name: stages
          value:
            - - name: stageName
                value: string
              - name: dependencies
                value:
                  - string
              - name: gitEnvironment
                value: string
        - name: templates
          value:
            - - name: templateName
                value: string
              - name: sourceResourceId
                value: string
              - name: instanceStage
                value: string
              - name: instanceName
                value: string
              - name: templateDetails
                value:
                  - - name: productName
                      value: string
                    - name: count
                      value: integer
                    - name: namingConvention
                      value: string
              - name: quickStartTemplateType
                value: []
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>iac_profiles</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.developer_hub.iac_profiles
WHERE iacProfileName = '{{ iacProfileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
