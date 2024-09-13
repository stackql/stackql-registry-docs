---
title: dest_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - dest_groups
  - iap
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

Creates, updates, deletes, gets or lists a <code>dest_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dest_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.iap.dest_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Identifier for the TunnelDestGroup. Must be unique within the project and contain only lower case letters (a-z) and dashes (-). |
| <CopyableCode code="cidrs" /> | `array` | Optional. Unordered list. List of CIDRs that this group applies to. |
| <CopyableCode code="fqdns" /> | `array` | Optional. Unordered list. List of FQDNs that this group applies to. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="destGroupsId, locationsId, projectsId" /> | Retrieves an existing TunnelDestGroup. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists the existing TunnelDestGroups. To group across all locations, use a `-` as the location ID. For example: `/v1/projects/123/iap_tunnel/locations/-/destGroups` |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new TunnelDestGroup. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="destGroupsId, locationsId, projectsId" /> | Deletes a TunnelDestGroup. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="destGroupsId, locationsId, projectsId" /> | Updates a TunnelDestGroup. |

## `SELECT` examples

Lists the existing TunnelDestGroups. To group across all locations, use a `-` as the location ID. For example: `/v1/projects/123/iap_tunnel/locations/-/destGroups`

```sql
SELECT
name,
cidrs,
fqdns
FROM google.iap.dest_groups
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dest_groups</code> resource.

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
INSERT INTO google.iap.dest_groups (
locationsId,
projectsId,
name,
cidrs,
fqdns
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ cidrs }}',
'{{ fqdns }}'
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
      - name: cidrs
        value: '{{ cidrs }}'
      - name: fqdns
        value: '{{ fqdns }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>dest_groups</code> resource.

```sql
/*+ update */
UPDATE google.iap.dest_groups
SET 
name = '{{ name }}',
cidrs = '{{ cidrs }}',
fqdns = '{{ fqdns }}'
WHERE 
destGroupsId = '{{ destGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>dest_groups</code> resource.

```sql
/*+ delete */
DELETE FROM google.iap.dest_groups
WHERE destGroupsId = '{{ destGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
