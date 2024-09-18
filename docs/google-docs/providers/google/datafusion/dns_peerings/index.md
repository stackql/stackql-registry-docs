---
title: dns_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_peerings
  - datafusion
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

Creates, updates, deletes, gets or lists a <code>dns_peerings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dns_peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datafusion.dns_peerings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource name of the dns peering zone. Format: projects/{project}/locations/{location}/instances/{instance}/dnsPeerings/{dns_peering} |
| <CopyableCode code="description" /> | `string` | Optional. Optional description of the dns zone. |
| <CopyableCode code="domain" /> | `string` | Required. The dns name suffix of the zone. |
| <CopyableCode code="targetNetwork" /> | `string` | Optional. Optional target network to which dns peering should happen. |
| <CopyableCode code="targetProject" /> | `string` | Optional. Optional target project to which dns peering should happen. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Lists DNS peerings for a given resource. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Creates DNS peering on the given resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dnsPeeringsId, instancesId, locationsId, projectsId" /> | Deletes DNS peering on the given resource. |

## `SELECT` examples

Lists DNS peerings for a given resource.

```sql
SELECT
name,
description,
domain,
targetNetwork,
targetProject
FROM google.datafusion.dns_peerings
WHERE instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dns_peerings</code> resource.

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
INSERT INTO google.datafusion.dns_peerings (
instancesId,
locationsId,
projectsId,
name,
domain,
description,
targetProject,
targetNetwork
)
SELECT 
'{{ instancesId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ domain }}',
'{{ description }}',
'{{ targetProject }}',
'{{ targetNetwork }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
domain: string
description: string
targetProject: string
targetNetwork: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>dns_peerings</code> resource.

```sql
/*+ delete */
DELETE FROM google.datafusion.dns_peerings
WHERE dnsPeeringsId = '{{ dnsPeeringsId }}'
AND instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
