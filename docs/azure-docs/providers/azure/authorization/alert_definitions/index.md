---
title: alert_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_definitions
  - authorization
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

Creates, updates, deletes, gets or lists a <code>alert_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alert_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.alert_definitions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alert_definitions', value: 'view', },
        { label: 'alert_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The alert definition ID. |
| <CopyableCode code="name" /> | `text` | The alert definition name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="alertDefinitionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="how_to_prevent" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_configurable" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_remediatable" /> | `text` | field from the `properties` object |
| <CopyableCode code="mitigation_steps" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_impact" /> | `text` | field from the `properties` object |
| <CopyableCode code="severity_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The alert definition type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The alert definition ID. |
| <CopyableCode code="name" /> | `string` | The alert definition name. |
| <CopyableCode code="properties" /> | `object` | Alert definition properties. |
| <CopyableCode code="type" /> | `string` | The alert definition type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="alertDefinitionId, scope" /> | Get the specified alert definition. |
| <CopyableCode code="list_for_scope" /> | `SELECT` | <CopyableCode code="scope" /> | Gets alert definitions for a resource scope. |

## `SELECT` examples

Gets alert definitions for a resource scope.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_alert_definitions', value: 'view', },
        { label: 'alert_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
alertDefinitionId,
display_name,
how_to_prevent,
is_configurable,
is_remediatable,
mitigation_steps,
scope,
security_impact,
severity_level,
type
FROM azure.authorization.vw_alert_definitions
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
FROM azure.authorization.alert_definitions
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>

