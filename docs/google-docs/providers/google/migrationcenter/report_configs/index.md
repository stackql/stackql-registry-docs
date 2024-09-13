---
title: report_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - report_configs
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

Creates, updates, deletes, gets or lists a <code>report_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>report_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.migrationcenter.report_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of resource. |
| <CopyableCode code="description" /> | `string` | Free-text description. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the resource was created. |
| <CopyableCode code="displayName" /> | `string` | User-friendly display name. Maximum length is 63 characters. |
| <CopyableCode code="groupPreferencesetAssignments" /> | `array` | Required. Collection of combinations of groups and preference sets. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the resource was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, reportConfigsId" /> | Gets details of a single ReportConfig. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists ReportConfigs in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a report configuration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, reportConfigsId" /> | Deletes a ReportConfig. |

## `SELECT` examples

Lists ReportConfigs in a given project and location.

```sql
SELECT
name,
description,
createTime,
displayName,
groupPreferencesetAssignments,
updateTime
FROM google.migrationcenter.report_configs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>report_configs</code> resource.

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
INSERT INTO google.migrationcenter.report_configs (
locationsId,
projectsId,
name,
createTime,
updateTime,
displayName,
description,
groupPreferencesetAssignments
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ displayName }}',
'{{ description }}',
'{{ groupPreferencesetAssignments }}'
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
      - name: groupPreferencesetAssignments
        value: '{{ groupPreferencesetAssignments }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>report_configs</code> resource.

```sql
/*+ delete */
DELETE FROM google.migrationcenter.report_configs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND reportConfigsId = '{{ reportConfigsId }}';
```
