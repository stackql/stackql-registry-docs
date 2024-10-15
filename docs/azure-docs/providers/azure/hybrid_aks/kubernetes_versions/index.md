---
title: kubernetes_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - kubernetes_versions
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

Creates, updates, deletes, gets or lists a <code>kubernetes_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kubernetes_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_aks.kubernetes_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | Extended location pointing to the underlying infrastructure |
| <CopyableCode code="properties" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customLocationResourceUri" /> | Lists the supported kubernetes versions for the specified custom location |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customLocationResourceUri" /> | Lists the supported kubernetes versions for the specified custom location |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customLocationResourceUri" /> | Delete the default kubernetes versions resource type |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="customLocationResourceUri" /> | Puts the default kubernetes version resource type (one time operation, before listing the kubernetes versions) |

## `SELECT` examples

Lists the supported kubernetes versions for the specified custom location


```sql
SELECT
extendedLocation,
properties
FROM azure.hybrid_aks.kubernetes_versions
WHERE customLocationResourceUri = '{{ customLocationResourceUri }}';
```
## `REPLACE` example

Replaces all fields in the specified <code>kubernetes_versions</code> resource.

```sql
/*+ update */
REPLACE azure.hybrid_aks.kubernetes_versions
SET 
extendedLocation = '{{ extendedLocation }}'
WHERE 
customLocationResourceUri = '{{ customLocationResourceUri }}';
```

## `DELETE` example

Deletes the specified <code>kubernetes_versions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_aks.kubernetes_versions
WHERE customLocationResourceUri = '{{ customLocationResourceUri }}';
```
