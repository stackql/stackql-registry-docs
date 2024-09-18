---
title: key_rings
hide_title: false
hide_table_of_contents: false
keywords:
  - key_rings
  - cloudkms
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

Creates, updates, deletes, gets or lists a <code>key_rings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key_rings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudkms.key_rings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name for the KeyRing in the format `projects/*/locations/*/keyRings/*`. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which this KeyRing was created. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keyRingsId, locationsId, projectsId" /> | Returns metadata for a given KeyRing. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists KeyRings. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a new KeyRing in a given Project and Location. |

## `SELECT` examples

Lists KeyRings.

```sql
SELECT
name,
createTime
FROM google.cloudkms.key_rings
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>key_rings</code> resource.

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
INSERT INTO google.cloudkms.key_rings (
locationsId,
projectsId
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
createTime: string

```
</TabItem>
</Tabs>
