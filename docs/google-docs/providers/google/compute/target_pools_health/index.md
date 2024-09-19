---
title: target_pools_health
hide_title: false
hide_table_of_contents: false
keywords:
  - target_pools_health
  - compute
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

Creates, updates, deletes, gets or lists a <code>target_pools_health</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>target_pools_health</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.target_pools_health" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="healthStatus" /> | `array` |  |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of resource. Always compute#targetPoolInstanceHealth when checking the health of an instance. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_health" /> | `SELECT` | <CopyableCode code="project, region, targetPool" /> | Gets the most recent health check results for each IP for the instance that is referenced by the given target pool. |

## `SELECT` examples

Gets the most recent health check results for each IP for the instance that is referenced by the given target pool.

```sql
SELECT
healthStatus,
kind
FROM google.compute.target_pools_health
WHERE project = '{{ project }}'
AND region = '{{ region }}'
AND targetPool = '{{ targetPool }}';
```
