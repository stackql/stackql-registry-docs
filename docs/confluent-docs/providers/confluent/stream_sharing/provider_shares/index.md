---
title: provider_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_shares
  - stream_sharing
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

Creates, updates, deletes, gets or lists a <code>provider_shares</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_shares</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.stream_sharing.provider_shares" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="_cloud_cluster" /> | `` |  |
| <CopyableCode code="_service_account" /> | `` |  |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="cloud_cluster" /> | `object` | The cloud cluster to which this belongs. |
| <CopyableCode code="consumer_organization_name" /> | `string` | Consumer organization name |
| <CopyableCode code="consumer_restriction" /> | `` | Restrictions on the consumer that can redeem this token |
| <CopyableCode code="consumer_user_name" /> | `string` | Name of the consumer |
| <CopyableCode code="delivery_method" /> | `string` | Method by which the invite will be delivered |
| <CopyableCode code="invite_expires_at" /> | `string` | The date and time at which the invitation will expire. Only for invited shares |
| <CopyableCode code="invited_at" /> | `string` | The date and time at which consumer was invited |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="provider_user" /> | `object` | The provider user/inviter |
| <CopyableCode code="provider_user_name" /> | `string` | Name or email of the provider user. Deprecated |
| <CopyableCode code="redeemed_at" /> | `string` | The date and time at which the invite was redeemed |
| <CopyableCode code="service_account" /> | `object` | The service account associated with this object. |
| <CopyableCode code="status" /> | `object` | The status of the Provider Share |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_cdx_v1provider_share" /> | `SELECT` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to read a provider share. |
| <CopyableCode code="list_cdx_v1provider_shares" /> | `SELECT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all provider shares. |
| <CopyableCode code="create_cdx_v1provider_share" /> | `INSERT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Creates a share based on delivery method. |
| <CopyableCode code="delete_cdx_v1provider_share" /> | `DELETE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to delete a provider share. |
| <CopyableCode code="resend_cdx_v1provider_share" /> | `EXEC` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Resend provider share |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all provider shares.


```sql
SELECT
id,
_cloud_cluster,
_service_account,
api_version,
cloud_cluster,
consumer_organization_name,
consumer_restriction,
consumer_user_name,
delivery_method,
invite_expires_at,
invited_at,
kind,
metadata,
provider_user,
provider_user_name,
redeemed_at,
service_account,
status
FROM confluent.stream_sharing.provider_shares
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>provider_shares</code> resource.

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
INSERT INTO confluent.stream_sharing.provider_shares (
data__delivery_method,
data__consumer_restriction,
data__resources
)
SELECT 
'{{ delivery_method }}',
'{{ consumer_restriction }}',
'{{ resources }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: provider_shares
  props:
    - name: delivery_method
      value: string
    - name: consumer_restriction
      props:
        - name: kind
          value: string
        - name: email
          value: string
    - name: resources
      value: array

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>provider_shares</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.stream_sharing.provider_shares
WHERE id = '{{ id }}';
```
