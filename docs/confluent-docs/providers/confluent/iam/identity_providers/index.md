---
title: identity_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_providers
  - iam
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>identity_providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>identity_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.iam.identity_providers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="description" /> | `string` | A description of the identity provider. |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="display_name" /> | `string` | The human-readable name of the OAuth identity provider. |
| <CopyableCode code="issuer" /> | `string` | A publicly accessible URL uniquely identifying the OAuth
identity provider authorized to issue access tokens. |
| <CopyableCode code="jwks_uri" /> | `string` | A publicly accessible JSON Web Key Set (JWKS) URI for the OAuth
identity provider. JWKS provides a set of crypotgraphic keys
used to verify the authenticity and integrity of JSON Web
Tokens (JWTs) issued by the OAuth identity provider. |
| <CopyableCode code="keys" /> | `array` | The JWKS issued by the OAuth identity provider. Only `kid` (key ID)
and `alg` (algorithm) properties for each key set are included. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="state" /> | `string` | The current state of the identity provider. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_iam_v2identity_provider" /> | `SELECT` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Make a request to read an identity provider. |
| <CopyableCode code="list_iam_v2identity_providers" /> | `SELECT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Retrieve a sorted, filtered, paginated list of all identity providers. |
| <CopyableCode code="create_iam_v2identity_provider" /> | `INSERT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Make a request to create an identity provider. |
| <CopyableCode code="delete_iam_v2identity_provider" /> | `DELETE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Make a request to delete an identity provider. |
| <CopyableCode code="update_iam_v2identity_provider" /> | `UPDATE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Make a request to update an identity provider. |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Retrieve a sorted, filtered, paginated list of all identity providers.


```sql
SELECT
id,
description,
api_version,
display_name,
issuer,
jwks_uri,
keys,
kind,
metadata,
state
FROM confluent.iam.identity_providers
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>identity_providers</code> resource.

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
INSERT INTO confluent.iam.identity_providers (
data__display_name,
data__description,
data__issuer,
data__jwks_uri
)
SELECT 
'{{ display_name }}',
'{{ description }}',
'{{ issuer }}',
'{{ jwks_uri }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: identity_providers
  props:
    - name: display_name
      value: string
    - name: description
      value: string
    - name: issuer
      value: string
    - name: jwks_uri
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>identity_providers</code> resource.

```sql
/*+ update */
UPDATE confluent.iam.identity_providers
SET 
metadata = '{{ metadata }}',
display_name = '{{ display_name }}',
description = '{{ description }}',
issuer = '{{ issuer }}',
jwks_uri = '{{ jwks_uri }}'
WHERE 
id = '{{ id }}';
```

## `DELETE` example

Deletes the specified <code>identity_providers</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.iam.identity_providers
WHERE id = '{{ id }}';
```
