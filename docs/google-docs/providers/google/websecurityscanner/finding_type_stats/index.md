---
title: finding_type_stats
hide_title: false
hide_table_of_contents: false
keywords:
  - finding_type_stats
  - websecurityscanner
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

Creates, updates, deletes, gets or lists a <code>finding_type_stats</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>finding_type_stats</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.websecurityscanner.finding_type_stats" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="findingTypeStats" /> | `array` | The list of FindingTypeStats returned. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId, scanConfigsId, scanRunsId" /> | List all FindingTypeStats under a given ScanRun. |

## `SELECT` examples

List all FindingTypeStats under a given ScanRun.

```sql
SELECT
findingTypeStats
FROM google.websecurityscanner.finding_type_stats
WHERE projectsId = '{{ projectsId }}'
AND scanConfigsId = '{{ scanConfigsId }}'
AND scanRunsId = '{{ scanRunsId }}'; 
```
