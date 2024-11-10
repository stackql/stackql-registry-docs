---
title: organizations
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations
  - org
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

Creates, updates, deletes, gets or lists a <code>organizations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.org.organizations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_organizations', value: 'view', },
        { label: 'organizations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="api_version" /> | `text` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="created_at" /> | `text` | field from the parent object |
| <CopyableCode code="display_name" /> | `text` | A human-readable name for the Organization |
| <CopyableCode code="jit_enabled" /> | `boolean` | The flag to toggle Just-In-Time user provisioning for SSO-enabled organization. Available for early access only. |
| <CopyableCode code="kind" /> | `text` | Kind defines the object this REST resource represents. |
| <CopyableCode code="resource_name" /> | `text` | field from the parent object |
| <CopyableCode code="updated_at" /> | `text` | field from the parent object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="display_name" /> | `string` | A human-readable name for the Organization |
| <CopyableCode code="jit_enabled" /> | `boolean` | The flag to toggle Just-In-Time user provisioning for SSO-enabled organization. Available for early access only. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_org_v2organization" /> | `SELECT` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to read an organization. |
| <CopyableCode code="list_org_v2organizations" /> | `SELECT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all organizations. |
| <CopyableCode code="update_org_v2organization" /> | `UPDATE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to update an organization. |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all organizations.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_organizations', value: 'view', },
        { label: 'organizations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
api_version,
created_at,
display_name,
jit_enabled,
kind,
resource_name,
updated_at
FROM confluent.org.vw_organizations
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
api_version,
display_name,
jit_enabled,
kind,
metadata
FROM confluent.org.organizations
;
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>organizations</code> resource.

```sql
/*+ update */
UPDATE confluent.org.organizations
SET 

WHERE 
id = '{{ id }}';
```
