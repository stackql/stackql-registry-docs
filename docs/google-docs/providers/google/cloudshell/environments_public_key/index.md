---
title: environments_public_key
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_public_key
  - cloudshell
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

Creates, updates, deletes, gets or lists a <code>environments_public_key</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments_public_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudshell.environments_public_key" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_public_key" /> | `INSERT` | <CopyableCode code="environmentsId, usersId" /> | Adds a public SSH key to an environment, allowing clients with the corresponding private key to connect to that environment via SSH. If a key with the same content already exists, this will error with ALREADY_EXISTS. |
| <CopyableCode code="remove_public_key" /> | `DELETE` | <CopyableCode code="environmentsId, usersId" /> | Removes a public SSH key from an environment. Clients will no longer be able to connect to the environment using the corresponding private key. If a key with the same content is not present, this will error with NOT_FOUND. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>environments_public_key</code> resource.

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
INSERT INTO google.cloudshell.environments_public_key (
environmentsId,
usersId,
key
)
SELECT 
'{{ environmentsId }}',
'{{ usersId }}',
'{{ key }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: key
        value: '{{ key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>environments_public_key</code> resource.

```sql
/*+ delete */
DELETE FROM google.cloudshell.environments_public_key
WHERE environmentsId = '{{ environmentsId }}'
AND usersId = '{{ usersId }}';
```
