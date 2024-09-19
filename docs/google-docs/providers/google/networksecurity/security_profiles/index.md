---
title: security_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - security_profiles
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

Creates, updates, deletes, gets or lists a <code>security_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networksecurity.security_profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Identifier. Name of the SecurityProfile resource. It matches pattern `projects|organizations/*/locations/{location}/securityProfiles/{security_profile}`. |
| <CopyableCode code="description" /> | `string` | Optional. An optional description of the profile. Max length 512 characters. |
| <CopyableCode code="createTime" /> | `string` | Output only. Resource creation timestamp. |
| <CopyableCode code="etag" /> | `string` | Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels as key value pairs. |
| <CopyableCode code="threatPreventionProfile" /> | `object` | ThreatPreventionProfile defines an action for specific threat signatures or severity levels. |
| <CopyableCode code="type" /> | `string` | Immutable. The single ProfileType that the SecurityProfile resource configures. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last resource update timestamp. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_security_profiles_get" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId, securityProfilesId" /> | Gets details of a single SecurityProfile. |
| <CopyableCode code="organizations_locations_security_profiles_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists SecurityProfiles in a given organization and location. |
| <CopyableCode code="organizations_locations_security_profiles_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates a new SecurityProfile in a given organization and location. |
| <CopyableCode code="organizations_locations_security_profiles_delete" /> | `DELETE` | <CopyableCode code="locationsId, organizationsId, securityProfilesId" /> | Deletes a single SecurityProfile. |
| <CopyableCode code="organizations_locations_security_profiles_patch" /> | `UPDATE` | <CopyableCode code="locationsId, organizationsId, securityProfilesId" /> | Updates the parameters of a single SecurityProfile. |

## `SELECT` examples

Lists SecurityProfiles in a given organization and location.

```sql
SELECT
name,
description,
createTime,
etag,
labels,
threatPreventionProfile,
type,
updateTime
FROM google.networksecurity.security_profiles
WHERE locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_profiles</code> resource.

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
INSERT INTO google.networksecurity.security_profiles (
locationsId,
organizationsId,
threatPreventionProfile,
name,
description,
labels,
type
)
SELECT 
'{{ locationsId }}',
'{{ organizationsId }}',
'{{ threatPreventionProfile }}',
'{{ name }}',
'{{ description }}',
'{{ labels }}',
'{{ type }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: threatPreventionProfile
      value:
        - name: severityOverrides
          value:
            - - name: severity
                value: string
              - name: action
                value: string
        - name: threatOverrides
          value:
            - - name: threatId
                value: string
              - name: type
                value: string
              - name: action
                value: string
    - name: name
      value: string
    - name: description
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: etag
      value: string
    - name: labels
      value: object
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>security_profiles</code> resource.

```sql
/*+ update */
UPDATE google.networksecurity.security_profiles
SET 
threatPreventionProfile = '{{ threatPreventionProfile }}',
name = '{{ name }}',
description = '{{ description }}',
labels = '{{ labels }}',
type = '{{ type }}'
WHERE 
locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}'
AND securityProfilesId = '{{ securityProfilesId }}';
```

## `DELETE` example

Deletes the specified <code>security_profiles</code> resource.

```sql
/*+ delete */
DELETE FROM google.networksecurity.security_profiles
WHERE locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}'
AND securityProfilesId = '{{ securityProfilesId }}';
```
