---
title: records
hide_title: false
hide_table_of_contents: false
keywords:
  - records
  - domains
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>records</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>records</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.domains.records" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="domains_get_record" /> | `SELECT` | <CopyableCode code="domain_name, domain_record_id" /> | To retrieve a specific domain record, send a GET request to `/v2/domains/$DOMAIN_NAME/records/$RECORD_ID`. |
| <CopyableCode code="domains_list_records" /> | `SELECT` | <CopyableCode code="domain_name" /> | To get a listing of all records configured for a domain, send a GET request to `/v2/domains/$DOMAIN_NAME/records`. The list of records returned can be filtered by using the `name` and `type` query parameters. For example, to only include A records for a domain, send a GET request to `/v2/domains/$DOMAIN_NAME/records?type=A`. `name` must be a fully qualified record name. For example, to only include records matching `sub.example.com`, send a GET request to `/v2/domains/$DOMAIN_NAME/records?name=sub.example.com`. Both name and type may be used together. |
| <CopyableCode code="domains_create_record" /> | `INSERT` | <CopyableCode code="domain_name" /> | To create a new record to a domain, send a POST request to `/v2/domains/$DOMAIN_NAME/records`. The request must include all of the required fields for the domain record type being added. See the [attribute table](#tag/Domain-Records) for details regarding record types and their respective required attributes. |
| <CopyableCode code="domains_delete_record" /> | `DELETE` | <CopyableCode code="domain_name, domain_record_id" /> | To delete a record for a domain, send a DELETE request to `/v2/domains/$DOMAIN_NAME/records/$DOMAIN_RECORD_ID`. The record will be deleted and the response status will be a 204. This indicates a successful request with no body returned. |
| <CopyableCode code="domains_patch_record" /> | `UPDATE` | <CopyableCode code="domain_name, domain_record_id, data__type" /> | To update an existing record, send a PATCH request to `/v2/domains/$DOMAIN_NAME/records/$DOMAIN_RECORD_ID`. Any attribute valid for the record type can be set to a new value for the record. See the [attribute table](#tag/Domain-Records) for details regarding record types and their respective attributes. |
| <CopyableCode code="domains_update_record" /> | `EXEC` | <CopyableCode code="domain_name, domain_record_id, data__type" /> | To update an existing record, send a PUT request to `/v2/domains/$DOMAIN_NAME/records/$DOMAIN_RECORD_ID`. Any attribute valid for the record type can be set to a new value for the record. See the [attribute table](#tag/Domain-Records) for details regarding record types and their respective attributes. |

## `SELECT` examples

To get a listing of all records configured for a domain, send a GET request to `/v2/domains/$DOMAIN_NAME/records`. The list of records returned can be filtered by using the `name` and `type` query parameters. For example, to only include A records for a domain, send a GET request to `/v2/domains/$DOMAIN_NAME/records?type=A`. `name` must be a fully qualified record name. For example, to only include records matching `sub.example.com`, send a GET request to `/v2/domains/$DOMAIN_NAME/records?name=sub.example.com`. Both name and type may be used together.


```sql
SELECT
column_anon
FROM digitalocean.domains.records
WHERE domain_name = '{{ domain_name }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>records</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO digitalocean.domains.records (
data__type,
data__name,
data__data,
data__priority,
data__port,
data__ttl,
data__weight,
data__flags,
data__tag,
domain_name
)
SELECT 
'{{ type }}',
'{{ name }}',
'{{ data }}',
'{{ priority }}',
'{{ port }}',
'{{ ttl }}',
'{{ weight }}',
'{{ flags }}',
'{{ tag }}',
'{{ domain_name }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO digitalocean.domains.records (
data__type,
data__name,
data__data,
domain_name
)
SELECT 
'{{ type }}',
'{{ name }}',
'{{ data }}',
'{{ domain_name }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: records
  props:
    - name: domain_name
      value: string
    - name: type
      value: string
    - name: name
      value: string
    - name: data
      value: string
    - name: priority
      value: integer
    - name: port
      value: integer
    - name: ttl
      value: integer
    - name: weight
      value: integer
    - name: flags
      value: integer
    - name: tag
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>records</code> resource.

```sql
/*+ update */
UPDATE digitalocean.domains.records
SET 
type = '{{ type }}',
name = '{{ name }}',
data = '{{ data }}',
priority = '{{ priority }}',
port = '{{ port }}',
ttl = '{{ ttl }}',
weight = '{{ weight }}',
flags = '{{ flags }}',
tag = '{{ tag }}'
WHERE 
domain_name = '{{ domain_name }}'
AND domain_record_id = '{{ domain_record_id }}'
AND data__type = '{{ data__type }}';
```

## `DELETE` example

Deletes the specified <code>records</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.domains.records
WHERE domain_name = '{{ domain_name }}'
AND domain_record_id = '{{ domain_record_id }}';
```
