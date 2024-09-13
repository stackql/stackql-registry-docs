---
title: optimized_host_stats
hide_title: false
hide_table_of_contents: false
keywords:
  - optimized_host_stats
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

Creates, updates, deletes, gets or lists a <code>optimized_host_stats</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>optimized_host_stats</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.optimized_host_stats" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="Response" /> | `object` | Encapsulates a response format for JavaScript Optimized Scenario. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_optimized_host_stats_get" /> | `SELECT` | <CopyableCode code="optimizedHostStatsId, organizationsId" /> | Similar to GetHostStats except that the response is less verbose. |

## `SELECT` examples

Similar to GetHostStats except that the response is less verbose.

```sql
SELECT
Response
FROM google.apigee.optimized_host_stats
WHERE optimizedHostStatsId = '{{ optimizedHostStatsId }}'
AND organizationsId = '{{ organizationsId }}'; 
```
