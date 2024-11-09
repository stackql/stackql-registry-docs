---
title: ip_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_groups
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

Creates, updates, deletes, gets or lists a <code>ip_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.iam.ip_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="cidr_blocks" /> | `array` | A list of CIDRs. |
| <CopyableCode code="group_name" /> | `string` | A human readable name for an IP Group. Can contain any unicode letter or number, the ASCII space character, or
any of the following special characters: `[`, `]`, `\|`, `&`, `+`, `-`, `_`, `/`, `.`, `,`. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_iam_v2ip_group" /> | `SELECT` | <CopyableCode code="id" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Groups API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Groups%20API-%23bc8540)](mailto:cloud-support@confluent.io?subject=Request%20to%20join%20IP%20Filtering%20API%20Limited%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Access%20for%20IP%20Filtering.%0AMy%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.%0A)

Make a request to read an IP group. |
| <CopyableCode code="list_iam_v2ip_groups" /> | `SELECT` | <CopyableCode code="" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Groups API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Groups%20API-%23bc8540)](mailto:cloud-support@confluent.io?subject=Request%20to%20join%20IP%20Filtering%20API%20Limited%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Access%20for%20IP%20Filtering.%0AMy%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.%0A)

Retrieve a sorted, filtered, paginated list of all IP groups. |
| <CopyableCode code="create_iam_v2ip_group" /> | `INSERT` | <CopyableCode code="" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Groups API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Groups%20API-%23bc8540)](mailto:cloud-support@confluent.io?subject=Request%20to%20join%20IP%20Filtering%20API%20Limited%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Access%20for%20IP%20Filtering.%0AMy%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.%0A)

Make a request to create an IP group. |
| <CopyableCode code="delete_iam_v2ip_group" /> | `DELETE` | <CopyableCode code="id" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Groups API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Groups%20API-%23bc8540)](mailto:cloud-support@confluent.io?subject=Request%20to%20join%20IP%20Filtering%20API%20Limited%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Access%20for%20IP%20Filtering.%0AMy%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.%0A)

Make a request to delete an IP group. |
| <CopyableCode code="update_iam_v2ip_group" /> | `UPDATE` | <CopyableCode code="id" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Groups API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Groups%20API-%23bc8540)](mailto:cloud-support@confluent.io?subject=Request%20to%20join%20IP%20Filtering%20API%20Limited%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Access%20for%20IP%20Filtering.%0AMy%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.%0A)

Make a request to update an IP group. |

## `SELECT` examples

[![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Groups API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Groups%20API-%23bc8540)](mailto:cloud-support@confluent.io?subject=Request%20to%20join%20IP%20Filtering%20API%20Limited%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Access%20for%20IP%20Filtering.%0AMy%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.%0A)

Retrieve a sorted, filtered, paginated list of all IP groups.


```sql
SELECT
id,
api_version,
cidr_blocks,
group_name,
kind,
metadata
FROM confluent.iam.ip_groups
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ip_groups</code> resource.

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
INSERT INTO confluent.iam.ip_groups (
data__group_name,
data__cidr_blocks
)
SELECT 
'{{ group_name }}',
'{{ cidr_blocks }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: ip_groups
  props:
    - name: group_name
      value: string
    - name: cidr_blocks
      value: array

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>ip_groups</code> resource.

```sql
/*+ update */
UPDATE confluent.iam.ip_groups
SET 
metadata = '{{ metadata }}',
group_name = '{{ group_name }}',
cidr_blocks = '{{ cidr_blocks }}'
WHERE 
id = '{{ id }}';
```

## `DELETE` example

Deletes the specified <code>ip_groups</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.iam.ip_groups
WHERE id = '{{ id }}';
```
