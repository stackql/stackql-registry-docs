---
title: inbound_sso_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - inbound_sso_assignments
  - cloudidentity
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

Creates, updates, deletes, gets or lists a <code>inbound_sso_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inbound_sso_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudidentity.inbound_sso_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Inbound SSO Assignment. |
| <CopyableCode code="customer" /> | `string` | Immutable. The customer. For example: `customers/C0123abc`. |
| <CopyableCode code="rank" /> | `integer` | Must be zero (which is the default value so it can be omitted) for assignments with `target_org_unit` set and must be greater-than-or-equal-to one for assignments with `target_group` set. |
| <CopyableCode code="samlSsoInfo" /> | `object` | Details that are applicable when `sso_mode` == `SAML_SSO`. |
| <CopyableCode code="signInBehavior" /> | `object` | Controls sign-in behavior. |
| <CopyableCode code="ssoMode" /> | `string` | Inbound SSO behavior. |
| <CopyableCode code="targetGroup" /> | `string` | Immutable. Must be of the form `groups/{group}`. |
| <CopyableCode code="targetOrgUnit" /> | `string` | Immutable. Must be of the form `orgUnits/{org_unit}`. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="inboundSsoAssignmentsId" /> | Gets an InboundSsoAssignment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists the InboundSsoAssignments for a `Customer`. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="" /> | Creates an InboundSsoAssignment for users and devices in a `Customer` under a given `Group` or `OrgUnit`. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="inboundSsoAssignmentsId" /> | Deletes an InboundSsoAssignment. To disable SSO, Create (or Update) an assignment that has `sso_mode` == `SSO_OFF`. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="inboundSsoAssignmentsId" /> | Updates an InboundSsoAssignment. The body of this request is the `inbound_sso_assignment` field and the `update_mask` is relative to that. For example: a PATCH to `/v1/inboundSsoAssignments/0abcdefg1234567&update_mask=rank` with a body of `{ "rank": 1 }` moves that (presumably group-targeted) SSO assignment to the highest priority and shifts any other group-targeted assignments down in priority. |

## `SELECT` examples

Lists the InboundSsoAssignments for a `Customer`.

```sql
SELECT
name,
customer,
rank,
samlSsoInfo,
signInBehavior,
ssoMode,
targetGroup,
targetOrgUnit
FROM google.cloudidentity.inbound_sso_assignments
WHERE  = '{{  }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>inbound_sso_assignments</code> resource.

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
INSERT INTO google.cloudidentity.inbound_sso_assignments (
,
targetGroup,
targetOrgUnit,
name,
customer,
rank,
ssoMode,
samlSsoInfo,
signInBehavior
)
SELECT 
'{{  }}',
'{{ targetGroup }}',
'{{ targetOrgUnit }}',
'{{ name }}',
'{{ customer }}',
'{{ rank }}',
'{{ ssoMode }}',
'{{ samlSsoInfo }}',
'{{ signInBehavior }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: targetGroup
        value: '{{ targetGroup }}'
      - name: targetOrgUnit
        value: '{{ targetOrgUnit }}'
      - name: name
        value: '{{ name }}'
      - name: customer
        value: '{{ customer }}'
      - name: rank
        value: '{{ rank }}'
      - name: ssoMode
        value: '{{ ssoMode }}'
      - name: samlSsoInfo
        value: '{{ samlSsoInfo }}'
      - name: signInBehavior
        value: '{{ signInBehavior }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>inbound_sso_assignments</code> resource.

```sql
/*+ update */
UPDATE google.cloudidentity.inbound_sso_assignments
SET 
targetGroup = '{{ targetGroup }}',
targetOrgUnit = '{{ targetOrgUnit }}',
name = '{{ name }}',
customer = '{{ customer }}',
rank = '{{ rank }}',
ssoMode = '{{ ssoMode }}',
samlSsoInfo = '{{ samlSsoInfo }}',
signInBehavior = '{{ signInBehavior }}'
WHERE 
inboundSsoAssignmentsId = '{{ inboundSsoAssignmentsId }}';
```

## `DELETE` example

Deletes the specified <code>inbound_sso_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM google.cloudidentity.inbound_sso_assignments
WHERE inboundSsoAssignmentsId = '{{ inboundSsoAssignmentsId }}';
```
