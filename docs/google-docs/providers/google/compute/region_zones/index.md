---
title: region_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - region_zones
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

Creates, updates, deletes, gets or lists a <code>region_zones</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_zones" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | [Output Only] Name of the resource. |
| <CopyableCode code="description" /> | `string` | [Output Only] Textual description of the resource. |
| <CopyableCode code="availableCpuPlatforms" /> | `array` | [Output Only] Available cpu/platform selections for the zone. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="deprecated" /> | `object` | Deprecation status for a public resource. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#zone for zones. |
| <CopyableCode code="region" /> | `string` | [Output Only] Full URL reference to the region which hosts the zone. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |
| <CopyableCode code="status" /> | `string` | [Output Only] Status of the zone, either UP or DOWN. |
| <CopyableCode code="supportsPzs" /> | `boolean` | [Output Only] Reserved for future use. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Retrieves the list of Zone resources under the specific region available to the specified project. |

## `SELECT` examples

Retrieves the list of Zone resources under the specific region available to the specified project.

```sql
SELECT
id,
name,
description,
availableCpuPlatforms,
creationTimestamp,
deprecated,
kind,
region,
selfLink,
status,
supportsPzs
FROM google.compute.region_zones
WHERE project = '{{ project }}'
AND region = '{{ region }}';
```
