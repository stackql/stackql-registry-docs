---
title: compliance_results
hide_title: false
hide_table_of_contents: false
keywords:
  - compliance_results
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

Creates, updates, deletes, gets or lists a <code>compliance_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>compliance_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.compliance_results" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_compliance_results', value: 'view', },
        { label: 'compliance_results', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="complianceResultName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Compliance result data |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="complianceResultName, resourceId" /> | Security Compliance Result |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Security compliance results in the subscription |

## `SELECT` examples

Security compliance results in the subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_compliance_results', value: 'view', },
        { label: 'compliance_results', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
complianceResultName,
resourceId,
resource_status,
scope,
type
FROM azure.security.vw_compliance_results
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
FROM azure.security.compliance_results
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>

