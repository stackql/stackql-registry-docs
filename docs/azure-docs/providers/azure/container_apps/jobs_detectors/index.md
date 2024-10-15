---
title: jobs_detectors
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs_detectors
  - container_apps
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

Creates, updates, deletes, gets or lists a <code>jobs_detectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs_detectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.jobs_detectors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Diagnostics resource specific properties |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="detectorName, jobName, resourceGroupName, subscriptionId" /> | Get the diagnostics data for a Container App Job. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Get the list of diagnostics for a Container App Job. |

## `SELECT` examples

Get the list of diagnostics for a Container App Job.


```sql
SELECT
properties
FROM azure.container_apps.jobs_detectors
WHERE jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```