---
title: compliances
hide_title: false
hide_table_of_contents: false
keywords:
  - compliances
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

Creates, updates, deletes, gets or lists a <code>compliances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>compliances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.compliances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_compliances', value: 'view', },
        { label: 'compliances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="assessment_result" /> | `text` | field from the `properties` object |
| <CopyableCode code="assessment_timestamp_utc_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="complianceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | The Compliance score (percentage) of a Subscription is a sum of all Resources' Compliances under the given Subscription. A Resource Compliance is defined as the compliant ('healthy') Policy Definitions out of all Policy Definitions applicable to a given resource. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="complianceName, scope" /> | Details of a specific Compliance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | The Compliance scores of the specific management group. |

## `SELECT` examples

The Compliance scores of the specific management group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_compliances', value: 'view', },
        { label: 'compliances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
assessment_result,
assessment_timestamp_utc_date,
complianceName,
resource_count,
scope,
type
FROM azure.security.vw_compliances
WHERE scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.compliances
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>

