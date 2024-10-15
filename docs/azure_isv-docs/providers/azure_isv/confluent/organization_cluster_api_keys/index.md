---
title: organization_cluster_api_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - organization_cluster_api_keys
  - confluent
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

Creates, updates, deletes, gets or lists a <code>organization_cluster_api_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organization_cluster_api_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.confluent.organization_cluster_api_keys" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_organization_cluster_api_keys', value: 'view', },
        { label: 'organization_cluster_api_keys', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Id of the api key |
| <CopyableCode code="apiKeyId" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Type of api key |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="organizationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="spec" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the api key |
| <CopyableCode code="kind" /> | `string` | Type of api key |
| <CopyableCode code="properties" /> | `object` | API Key Properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiKeyId, organizationName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apiKeyId, organizationName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_organization_cluster_api_keys', value: 'view', },
        { label: 'organization_cluster_api_keys', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
apiKeyId,
kind,
metadata,
organizationName,
resourceGroupName,
spec,
subscriptionId
FROM azure_isv.confluent.vw_organization_cluster_api_keys
WHERE apiKeyId = '{{ apiKeyId }}'
AND organizationName = '{{ organizationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
kind,
properties
FROM azure_isv.confluent.organization_cluster_api_keys
WHERE apiKeyId = '{{ apiKeyId }}'
AND organizationName = '{{ organizationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>organization_cluster_api_keys</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.confluent.organization_cluster_api_keys
WHERE apiKeyId = '{{ apiKeyId }}'
AND organizationName = '{{ organizationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
