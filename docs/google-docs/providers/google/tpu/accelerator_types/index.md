---
title: accelerator_types
hide_title: false
hide_table_of_contents: false
keywords:
  - accelerator_types
  - tpu
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

Creates, updates, deletes, gets or lists a <code>accelerator_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accelerator_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.tpu.accelerator_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="acceleratorConfigs" /> | `array` | The accelerator config. |
| <CopyableCode code="type" /> | `string` | The accelerator type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="acceleratorTypesId, locationsId, projectsId" /> | Gets AcceleratorType. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists accelerator types supported by this API. |

## `SELECT` examples

Lists accelerator types supported by this API.

```sql
SELECT
name,
acceleratorConfigs,
type
FROM google.tpu.accelerator_types
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
