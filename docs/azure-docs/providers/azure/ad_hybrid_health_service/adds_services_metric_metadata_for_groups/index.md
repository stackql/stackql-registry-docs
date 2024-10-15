---
title: adds_services_metric_metadata_for_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - adds_services_metric_metadata_for_groups
  - ad_hybrid_health_service
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

Creates, updates, deletes, gets or lists a <code>adds_services_metric_metadata_for_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>adds_services_metric_metadata_for_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.adds_services_metric_metadata_for_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="sets" /> | `array` | The list of metric set. |
| <CopyableCode code="timeStamps" /> | `array` | The list of timestamps for each metric in the metric set. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupName, metricName, serviceName" /> | Gets the service related metrics for a given metric and group combination. |

## `SELECT` examples

Gets the service related metrics for a given metric and group combination.


```sql
SELECT
sets,
timeStamps
FROM azure.ad_hybrid_health_service.adds_services_metric_metadata_for_groups
WHERE groupName = '{{ groupName }}'
AND metricName = '{{ metricName }}'
AND serviceName = '{{ serviceName }}';
```