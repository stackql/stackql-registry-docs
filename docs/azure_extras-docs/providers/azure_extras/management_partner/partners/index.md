---
title: partners
hide_title: false
hide_table_of_contents: false
keywords:
  - partners
  - management_partner
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

Creates, updates, deletes, gets or lists a <code>partners</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.management_partner.partners" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_partners', value: 'view', },
        { label: 'partners', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Identifier of the partner |
| <CopyableCode code="name" /> | `text` | Name of the partner |
| <CopyableCode code="created_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `integer` | Type of the partner |
| <CopyableCode code="object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of resource. "Microsoft.ManagementPartner/partners" |
| <CopyableCode code="updated_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Identifier of the partner |
| <CopyableCode code="name" /> | `string` | Name of the partner |
| <CopyableCode code="etag" /> | `integer` | Type of the partner |
| <CopyableCode code="properties" /> | `object` | this is the management partner properties |
| <CopyableCode code="type" /> | `string` | Type of resource. "Microsoft.ManagementPartner/partners" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="" /> | Get the management partner using the objectId and tenantId. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="partnerId" /> | Create a management partner for the objectId and tenantId. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="partnerId" /> | Delete the management partner for the objectId and tenantId. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="partnerId" /> | Update the management partner for the objectId and tenantId. |

## `SELECT` examples

Get the management partner using the objectId and tenantId.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_partners', value: 'view', },
        { label: 'partners', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
created_time,
etag,
object_id,
partner_id,
partner_name,
state,
tenant_id,
type,
updated_time,
version
FROM azure_extras.management_partner.vw_partners
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure_extras.management_partner.partners
;
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>partners</code> resource.

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
INSERT INTO azure_extras.management_partner.partners (
partnerId
)
SELECT 
'{{ partnerId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>partners</code> resource.

```sql
/*+ update */
UPDATE azure_extras.management_partner.partners
SET 

WHERE 
partnerId = '{{ partnerId }}';
```

## `DELETE` example

Deletes the specified <code>partners</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.management_partner.partners
WHERE partnerId = '{{ partnerId }}';
```
