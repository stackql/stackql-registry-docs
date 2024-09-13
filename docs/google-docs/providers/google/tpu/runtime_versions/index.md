---
title: runtime_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - runtime_versions
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

Creates, updates, deletes or gets an <code>runtime_version</code> resource or lists <code>runtime_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>runtime_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.tpu.runtime_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="version" /> | `string` | The runtime version. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, runtimeVersionsId" /> | Gets a runtime version. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists runtime versions supported by this API. |

## `SELECT` examples

Lists runtime versions supported by this API.

```sql
SELECT
name,
version
FROM google.tpu.runtime_versions
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
