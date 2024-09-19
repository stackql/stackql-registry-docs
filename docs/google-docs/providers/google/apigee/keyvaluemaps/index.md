---
title: keyvaluemaps
hide_title: false
hide_table_of_contents: false
keywords:
  - keyvaluemaps
  - apigee
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

Creates, updates, deletes, gets or lists a <code>keyvaluemaps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keyvaluemaps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.keyvaluemaps" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_apis_keyvaluemaps_create" /> | `INSERT` | <CopyableCode code="apisId, organizationsId" /> | Creates a key value map in an API proxy. |
| <CopyableCode code="organizations_environments_keyvaluemaps_create" /> | `INSERT` | <CopyableCode code="environmentsId, organizationsId" /> | Creates a key value map in an environment. |
| <CopyableCode code="organizations_keyvaluemaps_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a key value map in an organization. |
| <CopyableCode code="organizations_apis_keyvaluemaps_delete" /> | `DELETE` | <CopyableCode code="apisId, keyvaluemapsId, organizationsId" /> | Deletes a key value map from an API proxy. |
| <CopyableCode code="organizations_environments_keyvaluemaps_delete" /> | `DELETE` | <CopyableCode code="environmentsId, keyvaluemapsId, organizationsId" /> | Deletes a key value map from an environment. |
| <CopyableCode code="organizations_keyvaluemaps_delete" /> | `DELETE` | <CopyableCode code="keyvaluemapsId, organizationsId" /> | Deletes a key value map from an organization. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>keyvaluemaps</code> resource.

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
INSERT INTO google.apigee.keyvaluemaps (
organizationsId,
encrypted,
name
)
SELECT 
'{{ organizationsId }}',
true|false,
'{{ name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
encrypted: boolean
name: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>keyvaluemaps</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigee.keyvaluemaps
WHERE keyvaluemapsId = '{{ keyvaluemapsId }}'
AND organizationsId = '{{ organizationsId }}';
```
