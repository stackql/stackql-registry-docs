---
title: identity_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_pools
  - iam
  - confluent
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage confluent resources using SQL
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>identity_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.iam.identity_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="description" /> | `string` | A description of how this `IdentityPool` is used |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="display_name" /> | `string` | The name of the `IdentityPool`. |
| <CopyableCode code="filter" /> | `string` | A filter expression in [Supported Common Expression Language (CEL)](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/identity-pools.html#supported-common-expression-language-cel-filters) that specifies which identities can authenticate using your identity pool (see [Set identity pool filters](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/identity-pools.html#set-identity-pool-filters) for more details). |
| <CopyableCode code="identity_claim" /> | `string` | The JSON Web Token (JWT) claim to extract the authenticating identity to Confluent resources from (see [Registered Claim Names](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1) for more details). This appears in the audit log records, showing, for example, that "identity Z used identity pool X to access topic A". |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="principal" /> | `string` | Represents the federated identity associated with this pool. |
| <CopyableCode code="state" /> | `string` | The current state of the identity pool |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_iam_v2identity_pool" /> | `SELECT` | <CopyableCode code="id, provider_id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to read an identity pool. |
| <CopyableCode code="list_iam_v2identity_pools" /> | `SELECT` | <CopyableCode code="provider_id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all identity pools. |
| <CopyableCode code="create_iam_v2identity_pool" /> | `INSERT` | <CopyableCode code="provider_id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to create an identity pool. |
| <CopyableCode code="delete_iam_v2identity_pool" /> | `DELETE` | <CopyableCode code="id, provider_id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to delete an identity pool. |
| <CopyableCode code="update_iam_v2identity_pool" /> | `UPDATE` | <CopyableCode code="id, provider_id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to update an identity pool. |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all identity pools.


```sql
SELECT
id,
description,
api_version,
display_name,
filter,
identity_claim,
kind,
metadata,
principal,
state
FROM confluent.iam.identity_pools
WHERE provider_id = '{{ provider_id }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>identity_pools</code> resource.

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
INSERT INTO confluent.iam.identity_pools (
data__display_name,
data__description,
data__identity_claim,
data__filter,
provider_id
)
SELECT 
'{{ display_name }}',
'{{ description }}',
'{{ identity_claim }}',
'{{ filter }}',
'{{ provider_id }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: identity_pools
  props:
    - name: provider_id
      value: string
    - name: display_name
      value: string
    - name: description
      value: string
    - name: identity_claim
      value: string
    - name: filter
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>identity_pools</code> resource.

```sql
/*+ update */
UPDATE confluent.iam.identity_pools
SET 

WHERE 
id = '{{ id }}'
AND provider_id = '{{ provider_id }}';
```

## `DELETE` example

Deletes the specified <code>identity_pools</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.iam.identity_pools
WHERE id = '{{ id }}'
AND provider_id = '{{ provider_id }}';
```
