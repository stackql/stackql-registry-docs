
---
title: debug_config
hide_title: false
hide_table_of_contents: false
keywords:
  - debug_config
  - dataflow
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

Creates, updates, deletes or gets an <code>debug_config</code> resource or lists <code>debug_config</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>debug_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataflow.debug_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="config" /> | `string` | The encoded debug configuration for the requested component. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_jobs_debug_get_config" /> | `SELECT` | <CopyableCode code="jobId, projectId" /> | Get encoded debug configuration for component. Not cacheable. |
| <CopyableCode code="projects_locations_jobs_debug_get_config" /> | `SELECT` | <CopyableCode code="jobId, location, projectId" /> | Get encoded debug configuration for component. Not cacheable. |

## `SELECT` examples

Get encoded debug configuration for component. Not cacheable.

```sql
SELECT
config
FROM google.dataflow.debug_config
WHERE jobId = '{{ jobId }}'
AND projectId = '{{ projectId }}'; 
```
