
---
title: reports
hide_title: false
hide_table_of_contents: false
keywords:
  - reports
  - migrationcenter
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

Creates, updates, deletes or gets an <code>report</code> resource or lists <code>reports</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.migrationcenter.reports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of resource. |
| <CopyableCode code="description" /> | `string` | Free-text description. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation timestamp. |
| <CopyableCode code="displayName" /> | `string` | User-friendly display name. Maximum length is 63 characters. |
| <CopyableCode code="state" /> | `string` | Report creation state. |
| <CopyableCode code="summary" /> | `object` | Describes the Summary view of a Report, which contains aggregated values for all the groups and preference sets included in this Report. |
| <CopyableCode code="type" /> | `string` | Report type. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update timestamp. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, reportConfigsId, reportsId" /> | Gets details of a single Report. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, reportConfigsId" /> | Lists Reports in a given ReportConfig. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, reportConfigsId" /> | Creates a report. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, reportConfigsId, reportsId" /> | Deletes a Report. |

## `SELECT` examples

Lists Reports in a given ReportConfig.

```sql
SELECT
name,
description,
createTime,
displayName,
state,
summary,
type,
updateTime
FROM google.migrationcenter.reports
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND reportConfigsId = '{{ reportConfigsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>reports</code> resource.

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
INSERT INTO google.migrationcenter.reports (
locationsId,
projectsId,
reportConfigsId,
name,
createTime,
updateTime,
displayName,
description,
type,
state,
summary
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ reportConfigsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ displayName }}',
'{{ description }}',
'{{ type }}',
'{{ state }}',
'{{ summary }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: description
        value: '{{ description }}'
      - name: type
        value: '{{ type }}'
      - name: state
        value: '{{ state }}'
      - name: summary
        value: '{{ summary }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified report resource.

```sql
DELETE FROM google.migrationcenter.reports
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND reportConfigsId = '{{ reportConfigsId }}'
AND reportsId = '{{ reportsId }}';
```
