---
title: ip_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_filters
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

Creates, updates, deletes, gets or lists a <code>ip_filters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.iam.ip_filters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="filter_name" /> | `string` | A human readable name for an IP Filter. Can contain any unicode letter or number, the ASCII space character,
or any of the following special characters: `[`, `]`, `\|`, `&`, `+`, `-`, `_`, `/`, `.`, `,`. |
| <CopyableCode code="ip_groups" /> | `array` | A list of IP Groups. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="resource_group" /> | `string` | Scope of resources covered by this IP filter. The only resource_group currently available is "management". |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_iam_v2ip_filter" /> | `SELECT` | <CopyableCode code="id" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Filters API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Filters%20API-%23bc8540)](mailto:ccloud-api-access+iam-v2-limited-availability@confluent.io?subject=Request%20to%20join%20iam/v2%20API%20Limited%20Availability&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Availability%20for%20iam/v2%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)

Make a request to read an IP filter. |
| <CopyableCode code="list_iam_v2ip_filters" /> | `SELECT` | <CopyableCode code="" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Filters API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Filters%20API-%23bc8540)](mailto:ccloud-api-access+iam-v2-limited-availability@confluent.io?subject=Request%20to%20join%20iam/v2%20API%20Limited%20Availability&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Availability%20for%20iam/v2%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)

Retrieve a sorted, filtered, paginated list of all IP filters. |
| <CopyableCode code="create_iam_v2ip_filter" /> | `INSERT` | <CopyableCode code="" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Filters API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Filters%20API-%23bc8540)](mailto:ccloud-api-access+iam-v2-limited-availability@confluent.io?subject=Request%20to%20join%20iam/v2%20API%20Limited%20Availability&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Availability%20for%20iam/v2%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)

Make a request to create an IP filter. |
| <CopyableCode code="delete_iam_v2ip_filter" /> | `DELETE` | <CopyableCode code="id" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Filters API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Filters%20API-%23bc8540)](mailto:ccloud-api-access+iam-v2-limited-availability@confluent.io?subject=Request%20to%20join%20iam/v2%20API%20Limited%20Availability&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Availability%20for%20iam/v2%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)

Make a request to delete an IP filter. |
| <CopyableCode code="update_iam_v2ip_filter" /> | `UPDATE` | <CopyableCode code="id" /> | [![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Filters API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Filters%20API-%23bc8540)](mailto:ccloud-api-access+iam-v2-limited-availability@confluent.io?subject=Request%20to%20join%20iam/v2%20API%20Limited%20Availability&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Availability%20for%20iam/v2%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)

Make a request to update an IP filter. |

## `SELECT` examples

[![Limited Availability](https://img.shields.io/badge/Lifecycle%20Stage-Limited%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To IP Filters API](https://img.shields.io/badge/-Request%20Access%20To%20IP%20Filters%20API-%23bc8540)](mailto:ccloud-api-access+iam-v2-limited-availability@confluent.io?subject=Request%20to%20join%20iam/v2%20API%20Limited%20Availability&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Limited%20Availability%20for%20iam/v2%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)

Retrieve a sorted, filtered, paginated list of all IP filters.


```sql
SELECT
id,
api_version,
filter_name,
ip_groups,
kind,
metadata,
resource_group
FROM confluent.iam.ip_filters
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ip_filters</code> resource.

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
INSERT INTO confluent.iam.ip_filters (
data__filter_name,
data__resource_group,
data__ip_groups
)
SELECT 
'{{ filter_name }}',
'{{ resource_group }}',
'{{ ip_groups }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: ip_filters
  props:
    - name: filter_name
      value: string
    - name: resource_group
      value: string
    - name: ip_groups
      value: array
      props:
        - name: id
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>ip_filters</code> resource.

```sql
/*+ update */
UPDATE confluent.iam.ip_filters
SET 
metadata = '{{ metadata }}',
filter_name = '{{ filter_name }}',
resource_group = '{{ resource_group }}',
ip_groups = '{{ ip_groups }}'
WHERE 
id = '{{ id }}';
```

## `DELETE` example

Deletes the specified <code>ip_filters</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.iam.ip_filters
WHERE id = '{{ id }}';
```
