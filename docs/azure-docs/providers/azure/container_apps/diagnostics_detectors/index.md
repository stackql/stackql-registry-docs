---
title: diagnostics_detectors
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostics_detectors
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

Creates, updates, deletes, gets or lists a <code>diagnostics_detectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>diagnostics_detectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.diagnostics_detectors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Diagnostics resource specific properties |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="containerAppName, detectorName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="containerAppName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
properties
FROM azure.container_apps.diagnostics_detectors
WHERE containerAppName = '{{ containerAppName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```