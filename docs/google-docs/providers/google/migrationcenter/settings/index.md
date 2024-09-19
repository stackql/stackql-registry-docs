---
title: settings
hide_title: false
hide_table_of_contents: false
keywords:
  - settings
  - migrationcenter
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

Creates, updates, deletes, gets or lists a <code>settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.migrationcenter.settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of the resource. |
| <CopyableCode code="disableCloudLogging" /> | `boolean` | Disable Cloud Logging for the Migration Center API. Users are billed for the logs. |
| <CopyableCode code="preferenceSet" /> | `string` | The preference set used by default for a project. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_settings" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Gets the details of regional settings. |
| <CopyableCode code="update_settings" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId" /> | Updates the regional-level project settings. |

## `SELECT` examples

Gets the details of regional settings.

```sql
SELECT
name,
disableCloudLogging,
preferenceSet
FROM google.migrationcenter.settings
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `UPDATE` example

Updates a <code>settings</code> resource.

```sql
/*+ update */
UPDATE google.migrationcenter.settings
SET 
preferenceSet = '{{ preferenceSet }}',
disableCloudLogging = true|false
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
