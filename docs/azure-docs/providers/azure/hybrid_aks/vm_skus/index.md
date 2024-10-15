---
title: vm_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - vm_skus
  - hybrid_aks
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

Creates, updates, deletes, gets or lists a <code>vm_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vm_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_aks.vm_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | Extended location pointing to the underlying infrastructure |
| <CopyableCode code="properties" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customLocationResourceUri" /> | Lists the supported VM skus for the specified custom location |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customLocationResourceUri" /> | Lists the supported VM skus for the specified custom location |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customLocationResourceUri" /> | Deletes the default VM skus resource type |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="customLocationResourceUri" /> | Puts the default VM skus resource type (one time operation, before listing the VM skus) |

## `SELECT` examples

Lists the supported VM skus for the specified custom location


```sql
SELECT
extendedLocation,
properties
FROM azure.hybrid_aks.vm_skus
WHERE customLocationResourceUri = '{{ customLocationResourceUri }}';
```
## `REPLACE` example

Replaces all fields in the specified <code>vm_skus</code> resource.

```sql
/*+ update */
REPLACE azure.hybrid_aks.vm_skus
SET 
extendedLocation = '{{ extendedLocation }}'
WHERE 
customLocationResourceUri = '{{ customLocationResourceUri }}';
```

## `DELETE` example

Deletes the specified <code>vm_skus</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_aks.vm_skus
WHERE customLocationResourceUri = '{{ customLocationResourceUri }}';
```
