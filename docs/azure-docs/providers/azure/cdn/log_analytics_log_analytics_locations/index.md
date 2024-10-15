---
title: log_analytics_log_analytics_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - log_analytics_log_analytics_locations
  - cdn
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

Creates, updates, deletes, gets or lists a <code>log_analytics_log_analytics_locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>log_analytics_log_analytics_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.log_analytics_log_analytics_locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="continents" /> | `array` |  |
| <CopyableCode code="countryOrRegions" /> | `array` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Get all available location names for AFD log analytics report. |

## `SELECT` examples

Get all available location names for AFD log analytics report.


```sql
SELECT
continents,
countryOrRegions
FROM azure.cdn.log_analytics_log_analytics_locations
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```