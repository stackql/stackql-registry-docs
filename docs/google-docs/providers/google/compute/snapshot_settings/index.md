---
title: snapshot_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshot_settings
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

Creates, updates, deletes, gets or lists a <code>snapshot_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshot_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.snapshot_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="storageLocation" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project" /> | Get snapshot settings. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="project" /> | Patch snapshot settings. |

## `SELECT` examples

Get snapshot settings.

```sql
SELECT
storageLocation
FROM google.compute.snapshot_settings
WHERE project = '{{ project }}';
```

## `UPDATE` example

Updates a <code>snapshot_settings</code> resource.

```sql
/*+ update */
UPDATE google.compute.snapshot_settings
SET 
storageLocation = '{{ storageLocation }}'
WHERE 
project = '{{ project }}';
```
