---
title: access_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - access_policies
  - accesscontextmanager
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

Creates, updates, deletes, gets or lists a <code>access_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.accesscontextmanager.access_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Identifier. Resource name of the `AccessPolicy`. Format: `accessPolicies/{access_policy}` |
| <CopyableCode code="etag" /> | `string` | Output only. An opaque identifier for the current version of the `AccessPolicy`. This will always be a strongly validated etag, meaning that two Access Policies will be identical if and only if their etags are identical. Clients should not expect this to be in any specific format. |
| <CopyableCode code="parent" /> | `string` | Required. The parent of this `AccessPolicy` in the Cloud Resource Hierarchy. Currently immutable once created. Format: `organizations/{organization_id}` |
| <CopyableCode code="scopes" /> | `array` | The scopes of the AccessPolicy. Scopes define which resources a policy can restrict and where its resources can be referenced. For example, policy A with `scopes=["folders/123"]` has the following behavior: - ServicePerimeter can only restrict projects within `folders/123`. - ServicePerimeter within policy A can only reference access levels defined within policy A. - Only one policy can include a given scope; thus, attempting to create a second policy which includes `folders/123` will result in an error. If no scopes are provided, then any resource within the organization can be restricted. Scopes cannot be modified after a policy is created. Policies can only have a single scope. Format: list of `folders/{folder_number}` or `projects/{project_number}` |
| <CopyableCode code="title" /> | `string` | Required. Human readable title. Does not affect behavior. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accessPoliciesId" /> | Returns an access policy based on the name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all access policies in an organization. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="" /> | Creates an access policy. This method fails if the organization already has an access policy. The long-running operation has a successful status after the access policy propagates to long-lasting storage. Syntactic and basic semantic errors are returned in `metadata` as a BadRequest proto. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accessPoliciesId" /> | Deletes an access policy based on the resource name. The long-running operation has a successful status after the access policy is removed from long-lasting storage. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="accessPoliciesId" /> | Updates an access policy. The long-running operation from this RPC has a successful status after the changes to the access policy propagate to long-lasting storage. |

## `SELECT` examples

Lists all access policies in an organization.

```sql
SELECT
name,
etag,
parent,
scopes,
title
FROM google.accesscontextmanager.access_policies
;
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>access_policies</code> resource.

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
INSERT INTO google.accesscontextmanager.access_policies (
name,
parent,
title,
scopes
)
SELECT 
'{{ name }}',
'{{ parent }}',
'{{ title }}',
'{{ scopes }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: parent
      value: string
    - name: title
      value: string
    - name: scopes
      value:
        - string
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>access_policies</code> resource.

```sql
/*+ update */
UPDATE google.accesscontextmanager.access_policies
SET 
name = '{{ name }}',
parent = '{{ parent }}',
title = '{{ title }}',
scopes = '{{ scopes }}'
WHERE 
accessPoliciesId = '{{ accessPoliciesId }}';
```

## `DELETE` example

Deletes the specified <code>access_policies</code> resource.

```sql
/*+ delete */
DELETE FROM google.accesscontextmanager.access_policies
WHERE accessPoliciesId = '{{ accessPoliciesId }}';
```
