---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
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

Creates, updates, deletes, gets or lists a <code>rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networksecurity.rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Immutable. Name of the resource. ame is the full resource name so projects/{project}/locations/{location}/gatewaySecurityPolicies/{gateway_security_policy}/rules/{rule} rule should match the pattern: (^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$). |
| <CopyableCode code="description" /> | `string` | Optional. Free-text description of the resource. |
| <CopyableCode code="applicationMatcher" /> | `string` | Optional. CEL expression for matching on L7/application level criteria. |
| <CopyableCode code="basicProfile" /> | `string` | Required. Profile which tells what the primitive action should be. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the rule was created. |
| <CopyableCode code="enabled" /> | `boolean` | Required. Whether the rule is enforced. |
| <CopyableCode code="priority" /> | `integer` | Required. Priority of the rule. Lower number corresponds to higher precedence. |
| <CopyableCode code="sessionMatcher" /> | `string` | Required. CEL expression for matching on session criteria. |
| <CopyableCode code="tlsInspectionEnabled" /> | `boolean` | Optional. Flag to enable TLS inspection of traffic matching on , can only be true if the parent GatewaySecurityPolicy references a TLSInspectionConfig. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the rule was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_gateway_security_policies_rules_get" /> | `SELECT` | <CopyableCode code="gatewaySecurityPoliciesId, locationsId, projectsId, rulesId" /> | Gets details of a single GatewaySecurityPolicyRule. |
| <CopyableCode code="projects_locations_gateway_security_policies_rules_list" /> | `SELECT` | <CopyableCode code="gatewaySecurityPoliciesId, locationsId, projectsId" /> | Lists GatewaySecurityPolicyRules in a given project and location. |
| <CopyableCode code="projects_locations_gateway_security_policies_rules_create" /> | `INSERT` | <CopyableCode code="gatewaySecurityPoliciesId, locationsId, projectsId" /> | Creates a new GatewaySecurityPolicy in a given project and location. |
| <CopyableCode code="projects_locations_gateway_security_policies_rules_delete" /> | `DELETE` | <CopyableCode code="gatewaySecurityPoliciesId, locationsId, projectsId, rulesId" /> | Deletes a single GatewaySecurityPolicyRule. |
| <CopyableCode code="projects_locations_gateway_security_policies_rules_patch" /> | `UPDATE` | <CopyableCode code="gatewaySecurityPoliciesId, locationsId, projectsId, rulesId" /> | Updates the parameters of a single GatewaySecurityPolicyRule. |

## `SELECT` examples

Lists GatewaySecurityPolicyRules in a given project and location.

```sql
SELECT
name,
description,
applicationMatcher,
basicProfile,
createTime,
enabled,
priority,
sessionMatcher,
tlsInspectionEnabled,
updateTime
FROM google.networksecurity.rules
WHERE gatewaySecurityPoliciesId = '{{ gatewaySecurityPoliciesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>rules</code> resource.

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
INSERT INTO google.networksecurity.rules (
gatewaySecurityPoliciesId,
locationsId,
projectsId,
basicProfile,
name,
enabled,
priority,
description,
sessionMatcher,
applicationMatcher,
tlsInspectionEnabled
)
SELECT 
'{{ gatewaySecurityPoliciesId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ basicProfile }}',
'{{ name }}',
{{ enabled }},
'{{ priority }}',
'{{ description }}',
'{{ sessionMatcher }}',
'{{ applicationMatcher }}',
{{ tlsInspectionEnabled }}
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: basicProfile
      value: string
    - name: name
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: enabled
      value: boolean
    - name: priority
      value: integer
    - name: description
      value: string
    - name: sessionMatcher
      value: string
    - name: applicationMatcher
      value: string
    - name: tlsInspectionEnabled
      value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>rules</code> resource.

```sql
/*+ update */
UPDATE google.networksecurity.rules
SET 
basicProfile = '{{ basicProfile }}',
name = '{{ name }}',
enabled = true|false,
priority = '{{ priority }}',
description = '{{ description }}',
sessionMatcher = '{{ sessionMatcher }}',
applicationMatcher = '{{ applicationMatcher }}',
tlsInspectionEnabled = true|false
WHERE 
gatewaySecurityPoliciesId = '{{ gatewaySecurityPoliciesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND rulesId = '{{ rulesId }}';
```

## `DELETE` example

Deletes the specified <code>rules</code> resource.

```sql
/*+ delete */
DELETE FROM google.networksecurity.rules
WHERE gatewaySecurityPoliciesId = '{{ gatewaySecurityPoliciesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND rulesId = '{{ rulesId }}';
```
