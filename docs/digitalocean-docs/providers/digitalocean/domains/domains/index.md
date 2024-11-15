---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
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

Creates, updates, deletes, gets or lists a <code>domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.domains.domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="domains_get" /> | `SELECT` | <CopyableCode code="domain_name" /> | To get details about a specific domain, send a GET request to `/v2/domains/$DOMAIN_NAME`. |
| <CopyableCode code="domains_list" /> | `SELECT` | <CopyableCode code="" /> | To retrieve a list of all of the domains in your account, send a GET request to `/v2/domains`. |
| <CopyableCode code="domains_create" /> | `INSERT` | <CopyableCode code="" /> | To create a new domain, send a POST request to `/v2/domains`. Set the "name" attribute to the domain name you are adding. Optionally, you may set the "ip_address" attribute, and an A record will be automatically created pointing to the apex domain. |
| <CopyableCode code="domains_delete" /> | `DELETE` | <CopyableCode code="domain_name" /> | To delete a domain, send a DELETE request to `/v2/domains/$DOMAIN_NAME`. |

## `SELECT` examples

To retrieve a list of all of the domains in your account, send a GET request to `/v2/domains`.


```sql
SELECT
column_anon
FROM digitalocean.domains.domains
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>domains</code> resource.

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
INSERT INTO digitalocean.domains.domains (
data__name,
data__ip_address
)
SELECT 
'{{ name }}',
'{{ ip_address }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: domains
  props:
    - name: name
      value: string
    - name: ip_address
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>domains</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.domains.domains
WHERE domain_name = '{{ domain_name }}';
```
