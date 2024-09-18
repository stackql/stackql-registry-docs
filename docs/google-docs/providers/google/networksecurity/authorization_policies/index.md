---
title: authorization_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_policies
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

Creates, updates, deletes, gets or lists a <code>authorization_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorization_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networksecurity.authorization_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Name of the AuthorizationPolicy resource. It matches pattern `projects/{project}/locations/{location}/authorizationPolicies/`. |
| <CopyableCode code="description" /> | `string` | Optional. Free-text description of the resource. |
| <CopyableCode code="action" /> | `string` | Required. The action to take when a rule match is found. Possible values are "ALLOW" or "DENY". |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the resource was created. |
| <CopyableCode code="labels" /> | `object` | Optional. Set of label tags associated with the AuthorizationPolicy resource. |
| <CopyableCode code="rules" /> | `array` | Optional. List of rules to match. Note that at least one of the rules must match in order for the action specified in the 'action' field to be taken. A rule is a match if there is a matching source and destination. If left blank, the action specified in the `action` field will be applied on every request. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the resource was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_authorization_policies_get" /> | `SELECT` | <CopyableCode code="authorizationPoliciesId, locationsId, projectsId" /> | Gets details of a single AuthorizationPolicy. |
| <CopyableCode code="projects_locations_authorization_policies_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists AuthorizationPolicies in a given project and location. |
| <CopyableCode code="projects_locations_authorization_policies_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new AuthorizationPolicy in a given project and location. |
| <CopyableCode code="projects_locations_authorization_policies_delete" /> | `DELETE` | <CopyableCode code="authorizationPoliciesId, locationsId, projectsId" /> | Deletes a single AuthorizationPolicy. |
| <CopyableCode code="projects_locations_authorization_policies_patch" /> | `UPDATE` | <CopyableCode code="authorizationPoliciesId, locationsId, projectsId" /> | Updates the parameters of a single AuthorizationPolicy. |

## `SELECT` examples

Lists AuthorizationPolicies in a given project and location.

```sql
SELECT
name,
description,
action,
createTime,
labels,
rules,
updateTime
FROM google.networksecurity.authorization_policies
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>authorization_policies</code> resource.

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
INSERT INTO google.networksecurity.authorization_policies (
locationsId,
projectsId,
name,
description,
labels,
action,
rules
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ labels }}',
'{{ action }}',
'{{ rules }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
description: string
createTime: string
updateTime: string
labels: object
action: string
rules:
  - sources:
      - principals:
          - type: string
        ipBlocks:
          - type: string
    destinations:
      - hosts:
          - type: string
        ports:
          - type: string
            format: string
        methods:
          - type: string
        httpHeaderMatch:
          regexMatch: string
          headerName: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>authorization_policies</code> resource.

```sql
/*+ update */
UPDATE google.networksecurity.authorization_policies
SET 
name = '{{ name }}',
description = '{{ description }}',
labels = '{{ labels }}',
action = '{{ action }}',
rules = '{{ rules }}'
WHERE 
authorizationPoliciesId = '{{ authorizationPoliciesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>authorization_policies</code> resource.

```sql
/*+ delete */
DELETE FROM google.networksecurity.authorization_policies
WHERE authorizationPoliciesId = '{{ authorizationPoliciesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
