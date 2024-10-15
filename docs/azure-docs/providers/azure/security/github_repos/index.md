---
title: github_repos
hide_title: false
hide_table_of_contents: false
keywords:
  - github_repos
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

Creates, updates, deletes, gets or lists a <code>github_repos</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>github_repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.github_repos" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_github_repos', value: 'view', },
        { label: 'github_repos', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="onboarding_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="ownerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="parent_owner_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_status_update_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="repoName" /> | `text` | field from the `properties` object |
| <CopyableCode code="repo_full_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="repo_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="repo_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="repo_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="securityConnectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | GitHub Repository properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ownerName, repoName, resourceGroupName, securityConnectorName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="ownerName, resourceGroupName, securityConnectorName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_github_repos', value: 'view', },
        { label: 'github_repos', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
onboarding_state,
ownerName,
parent_owner_name,
provisioning_state,
provisioning_status_message,
provisioning_status_update_time_utc,
repoName,
repo_full_name,
repo_id,
repo_name,
repo_url,
resourceGroupName,
securityConnectorName,
subscriptionId,
system_data
FROM azure.security.vw_github_repos
WHERE ownerName = '{{ ownerName }}'
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
FROM azure.security.github_repos
WHERE ownerName = '{{ ownerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND securityConnectorName = '{{ securityConnectorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

