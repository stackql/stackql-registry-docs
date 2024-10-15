---
title: threat_intelligence_indicator_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - threat_intelligence_indicator_metrics
  - sentinel
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

Creates, updates, deletes, gets or lists a <code>threat_intelligence_indicator_metrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>threat_intelligence_indicator_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.threat_intelligence_indicator_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Describes threat intelligence metric |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Get threat intelligence indicators metrics (Indicators counts by Type, Threat Type, Source). |

## `SELECT` examples

Get threat intelligence indicators metrics (Indicators counts by Type, Threat Type, Source).


```sql
SELECT
properties
FROM azure.sentinel.threat_intelligence_indicator_metrics
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```