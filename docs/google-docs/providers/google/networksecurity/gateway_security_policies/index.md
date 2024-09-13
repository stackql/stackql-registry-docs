---
title: gateway_security_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_security_policies
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

Creates, updates, deletes or gets an <code>gateway_security_policy</code> resource or lists <code>gateway_security_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateway_security_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networksecurity.gateway_security_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Name of the resource. Name is of the form projects/{project}/locations/{location}/gatewaySecurityPolicies/{gateway_security_policy} gateway_security_policy should match the pattern:(^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$). |
| <CopyableCode code="description" /> | `string` | Optional. Free-text description of the resource. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the resource was created. |
| <CopyableCode code="tlsInspectionPolicy" /> | `string` | Optional. Name of a TLS Inspection Policy resource that defines how TLS inspection will be performed for any rule(s) which enables it. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the resource was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_gateway_security_policies_get" /> | `SELECT` | <CopyableCode code="gatewaySecurityPoliciesId, locationsId, projectsId" /> | Gets details of a single GatewaySecurityPolicy. |
| <CopyableCode code="projects_locations_gateway_security_policies_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists GatewaySecurityPolicies in a given project and location. |
| <CopyableCode code="projects_locations_gateway_security_policies_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new GatewaySecurityPolicy in a given project and location. |
| <CopyableCode code="projects_locations_gateway_security_policies_delete" /> | `DELETE` | <CopyableCode code="gatewaySecurityPoliciesId, locationsId, projectsId" /> | Deletes a single GatewaySecurityPolicy. |
| <CopyableCode code="projects_locations_gateway_security_policies_patch" /> | `UPDATE` | <CopyableCode code="gatewaySecurityPoliciesId, locationsId, projectsId" /> | Updates the parameters of a single GatewaySecurityPolicy. |

## `SELECT` examples

Lists GatewaySecurityPolicies in a given project and location.

```sql
SELECT
name,
description,
createTime,
tlsInspectionPolicy,
updateTime
FROM google.networksecurity.gateway_security_policies
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>gateway_security_policies</code> resource.

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
INSERT INTO google.networksecurity.gateway_security_policies (
locationsId,
projectsId,
name,
createTime,
updateTime,
description,
tlsInspectionPolicy
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ description }}',
'{{ tlsInspectionPolicy }}'
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
      - name: description
        value: '{{ description }}'
      - name: tlsInspectionPolicy
        value: '{{ tlsInspectionPolicy }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a gateway_security_policy only if the necessary resources are available.

```sql
UPDATE google.networksecurity.gateway_security_policies
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
description = '{{ description }}',
tlsInspectionPolicy = '{{ tlsInspectionPolicy }}'
WHERE 
gatewaySecurityPoliciesId = '{{ gatewaySecurityPoliciesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified gateway_security_policy resource.

```sql
DELETE FROM google.networksecurity.gateway_security_policies
WHERE gatewaySecurityPoliciesId = '{{ gatewaySecurityPoliciesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
