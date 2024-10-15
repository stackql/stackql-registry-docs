---
title: secure_scores
hide_title: false
hide_table_of_contents: false
keywords:
  - secure_scores
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

Creates, updates, deletes, gets or lists a <code>secure_scores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secure_scores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.secure_scores" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_secure_scores', value: 'view', },
        { label: 'secure_scores', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="score" /> | `text` | field from the `properties` object |
| <CopyableCode code="secureScoreName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="weight" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Describes properties of a calculated secure score. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="secureScoreName, subscriptionId" /> | Get secure score for a specific Microsoft Defender for Cloud initiative within your current scope. For the ASC Default initiative, use 'ascScore'. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List secure scores for all your Microsoft Defender for Cloud initiatives within your current scope. |

## `SELECT` examples

List secure scores for all your Microsoft Defender for Cloud initiatives within your current scope.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_secure_scores', value: 'view', },
        { label: 'secure_scores', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
display_name,
score,
secureScoreName,
subscriptionId,
type,
weight
FROM azure.security.vw_secure_scores
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.secure_scores
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

