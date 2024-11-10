---
title: consumer_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - consumer_shares
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

Creates, updates, deletes, gets or lists a <code>consumer_shares</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consumer_shares</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.stream_sharing.consumer_shares" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="consumer_organization_name" /> | `string` | Consumer organization name. Deprecated |
| <CopyableCode code="consumer_user" /> | `object` | The consumer user/invitee |
| <CopyableCode code="consumer_user_name" /> | `string` | Name of the consumer. Deprecated |
| <CopyableCode code="invite_expires_at" /> | `string` | The date and time at which the invitation will expire. Only for invited shares |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="provider_organization_name" /> | `string` | Provider organization name |
| <CopyableCode code="provider_user_name" /> | `string` | Name or email of the provider user |
| <CopyableCode code="status" /> | `object` | The status of the Consumer Share |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_cdx_v1consumer_share" /> | `SELECT` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to read a consumer share. |
| <CopyableCode code="list_cdx_v1consumer_shares" /> | `SELECT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all consumer shares. |
| <CopyableCode code="delete_cdx_v1consumer_share" /> | `DELETE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to delete a consumer share. |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all consumer shares.


```sql
SELECT
id,
api_version,
consumer_organization_name,
consumer_user,
consumer_user_name,
invite_expires_at,
kind,
metadata,
provider_organization_name,
provider_user_name,
status
FROM confluent.stream_sharing.consumer_shares
;
```
## `DELETE` example

Deletes the specified <code>consumer_shares</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.stream_sharing.consumer_shares
WHERE id = '{{ id }}';
```
