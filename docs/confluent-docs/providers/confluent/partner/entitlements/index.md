---
title: entitlements
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlements
  - partner
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

Creates, updates, deletes, gets or lists a <code>entitlements</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entitlements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.partner.entitlements" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="name" /> | `string` | The name of the entitlement |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="external_id" /> | `string` | The unique external ID of the entitlement (this should be unique to customer) |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="organization" /> | `object` | The organization associated with this object. |
| <CopyableCode code="plan_id" /> | `string` | The plan ID the entitlement |
| <CopyableCode code="product_id" /> | `string` | The product ID of the entitlement |
| <CopyableCode code="resource_id" /> | `string` | The resource ID of the entitlement |
| <CopyableCode code="usage_reporting_id" /> | `string` | The usage reporting ID of the entitlement (if usage reporting uses
a different ID, otherwise, same as external_id) |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_partner_v2entitlement" /> | `SELECT` | <CopyableCode code="id" /> | [![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Partner v2](https://img.shields.io/badge/-Request%20Access%20To%20Partner%20v2-%23bc8540)](mailto:ccloud-api-access+partner-v2-early-access@confluent.io?subject=Request%20to%20join%20partner/v2%20API%20Early%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Early%20Access%20for%20partner/v2%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)

Make a request to read an entitlement. |
| <CopyableCode code="list_partner_v2entitlements" /> | `SELECT` | <CopyableCode code="" /> | [![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Partner v2](https://img.shields.io/badge/-Request%20Access%20To%20Partner%20v2-%23bc8540)](mailto:ccloud-api-access+partner-v2-early-access@confluent.io?subject=Request%20to%20join%20partner/v2%20API%20Early%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Early%20Access%20for%20partner/v2%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)

Retrieve a sorted, filtered, paginated list of all entitlements. |
| <CopyableCode code="create_partner_v2entitlement" /> | `INSERT` | <CopyableCode code="" /> | [![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Partner v2](https://img.shields.io/badge/-Request%20Access%20To%20Partner%20v2-%23bc8540)](mailto:ccloud-api-access+partner-v2-early-access@confluent.io?subject=Request%20to%20join%20partner/v2%20API%20Early%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Early%20Access%20for%20partner/v2%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)

Make a request to create an entitlement. |

## `SELECT` examples

[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Partner v2](https://img.shields.io/badge/-Request%20Access%20To%20Partner%20v2-%23bc8540)](mailto:ccloud-api-access+partner-v2-early-access@confluent.io?subject=Request%20to%20join%20partner/v2%20API%20Early%20Access&body=I%E2%80%99d%20like%20to%20join%20the%20Confluent%20Cloud%20API%20Early%20Access%20for%20partner/v2%20to%20provide%20early%20feedback%21%20My%20Cloud%20Organization%20ID%20is%20%3Cretrieve%20from%20https%3A//confluent.cloud/settings/billing/payment%3E.)

Retrieve a sorted, filtered, paginated list of all entitlements.


```sql
SELECT
id,
name,
api_version,
external_id,
kind,
metadata,
organization,
plan_id,
product_id,
resource_id,
usage_reporting_id
FROM confluent.partner.entitlements
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>entitlements</code> resource.

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
INSERT INTO confluent.partner.entitlements (
data__external_id,
data__name,
data__plan_id,
data__product_id
)
SELECT 
'{{ external_id }}',
'{{ name }}',
'{{ plan_id }}',
'{{ product_id }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: entitlements
  props:
    - name: external_id
      value: string
    - name: name
      value: string
    - name: plan_id
      value: string
    - name: product_id
      value: string
    - name: usage_reporting_id
      value: string
    - name: resource_id
      value: string
    - name: organization
      props:
        - name: id
          value: string
        - name: environment
          value: string

```
</TabItem>
</Tabs>
