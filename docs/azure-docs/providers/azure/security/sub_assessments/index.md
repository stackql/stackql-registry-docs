---
title: sub_assessments
hide_title: false
hide_table_of_contents: false
keywords:
  - sub_assessments
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

Creates, updates, deletes, gets or lists a <code>sub_assessments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sub_assessments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.sub_assessments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sub_assessments', value: 'view', },
        { label: 'sub_assessments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="additional_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="assessmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="category" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="impact" /> | `text` | field from the `properties` object |
| <CopyableCode code="remediation" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subAssessmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_generated" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Describes properties of an sub-assessment. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="assessmentName, scope, subAssessmentName" /> | Get a security sub-assessment on your scanned resource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="assessmentName, scope" /> | Get security sub-assessments on all your scanned resources inside a scope |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="scope" /> | Get security sub-assessments on all your scanned resources inside a subscription scope |

## `SELECT` examples

Get security sub-assessments on all your scanned resources inside a subscription scope

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sub_assessments', value: 'view', },
        { label: 'sub_assessments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
additional_data,
assessmentName,
category,
display_name,
impact,
remediation,
resource_details,
scope,
status,
subAssessmentName,
time_generated,
type
FROM azure.security.vw_sub_assessments
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
FROM azure.security.sub_assessments
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>

