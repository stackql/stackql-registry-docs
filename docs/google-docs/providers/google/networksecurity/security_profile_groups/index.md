---
title: security_profile_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - security_profile_groups
  - networksecurity
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

Creates, updates, deletes, gets or lists a <code>security_profile_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_profile_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networksecurity.security_profile_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Identifier. Name of the SecurityProfileGroup resource. It matches pattern `projects|organizations/*/locations/{location}/securityProfileGroups/{security_profile_group}`. |
| <CopyableCode code="description" /> | `string` | Optional. An optional description of the profile group. Max length 2048 characters. |
| <CopyableCode code="createTime" /> | `string` | Output only. Resource creation timestamp. |
| <CopyableCode code="etag" /> | `string` | Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels as key value pairs. |
| <CopyableCode code="threatPreventionProfile" /> | `string` | Optional. Reference to a SecurityProfile with the ThreatPrevention configuration. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last resource update timestamp. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_security_profile_groups_get" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId, securityProfileGroupsId" /> | Gets details of a single SecurityProfileGroup. |
| <CopyableCode code="organizations_locations_security_profile_groups_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists SecurityProfileGroups in a given organization and location. |
| <CopyableCode code="organizations_locations_security_profile_groups_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates a new SecurityProfileGroup in a given organization and location. |
| <CopyableCode code="organizations_locations_security_profile_groups_delete" /> | `DELETE` | <CopyableCode code="locationsId, organizationsId, securityProfileGroupsId" /> | Deletes a single SecurityProfileGroup. |
| <CopyableCode code="organizations_locations_security_profile_groups_patch" /> | `UPDATE` | <CopyableCode code="locationsId, organizationsId, securityProfileGroupsId" /> | Updates the parameters of a single SecurityProfileGroup. |

## `SELECT` examples

Lists SecurityProfileGroups in a given organization and location.

```sql
SELECT
name,
description,
createTime,
etag,
labels,
threatPreventionProfile,
updateTime
FROM google.networksecurity.security_profile_groups
WHERE locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_profile_groups</code> resource.

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
INSERT INTO google.networksecurity.security_profile_groups (
locationsId,
organizationsId,
name,
description,
createTime,
updateTime,
etag,
labels,
threatPreventionProfile
)
SELECT 
'{{ locationsId }}',
'{{ organizationsId }}',
'{{ name }}',
'{{ description }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ etag }}',
'{{ labels }}',
'{{ threatPreventionProfile }}'
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
      - name: description
        value: '{{ description }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: etag
        value: '{{ etag }}'
      - name: labels
        value: '{{ labels }}'
      - name: threatPreventionProfile
        value: '{{ threatPreventionProfile }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>security_profile_groups</code> resource.

```sql
/*+ update */
UPDATE google.networksecurity.security_profile_groups
SET 
name = '{{ name }}',
description = '{{ description }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
etag = '{{ etag }}',
labels = '{{ labels }}',
threatPreventionProfile = '{{ threatPreventionProfile }}'
WHERE 
locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}'
AND securityProfileGroupsId = '{{ securityProfileGroupsId }}';
```

## `DELETE` example

Deletes the specified <code>security_profile_groups</code> resource.

```sql
/*+ delete */
DELETE FROM google.networksecurity.security_profile_groups
WHERE locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}'
AND securityProfileGroupsId = '{{ securityProfileGroupsId }}';
```
