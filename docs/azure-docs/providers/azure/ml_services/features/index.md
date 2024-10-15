---
title: features
hide_title: false
hide_table_of_contents: false
keywords:
  - features
  - ml_services
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

Creates, updates, deletes, gets or lists a <code>features</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>features</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.features" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_features', value: 'view', },
        { label: 'features', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="featureName" /> | `text` | field from the `properties` object |
| <CopyableCode code="feature_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="featuresetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="featuresetVersion" /> | `text` | field from the `properties` object |
| <CopyableCode code="properties" /> | `text` | DTO object representing feature |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | DTO object representing feature |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="featureName, featuresetName, featuresetVersion, resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="featuresetName, featuresetVersion, resourceGroupName, subscriptionId, workspaceName" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_features', value: 'view', },
        { label: 'features', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
data_type,
featureName,
feature_name,
featuresetName,
featuresetVersion,
properties,
resourceGroupName,
subscriptionId,
tags,
workspaceName
FROM azure.ml_services.vw_features
WHERE featuresetName = '{{ featuresetName }}'
AND featuresetVersion = '{{ featuresetVersion }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.ml_services.features
WHERE featuresetName = '{{ featuresetName }}'
AND featuresetVersion = '{{ featuresetVersion }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>

