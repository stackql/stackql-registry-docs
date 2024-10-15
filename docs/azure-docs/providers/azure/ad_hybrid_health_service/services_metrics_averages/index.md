---
title: services_metrics_averages
hide_title: false
hide_table_of_contents: false
keywords:
  - services_metrics_averages
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

Creates, updates, deletes, gets or lists a <code>services_metrics_averages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services_metrics_averages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.services_metrics_averages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="key" /> | `string` | The key for the property. |
| <CopyableCode code="value" /> | `string` | The value for the key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="groupName, metricName, serviceName" /> | Gets the average of the metric values for a given metric and group combination. |

## `SELECT` examples

Gets the average of the metric values for a given metric and group combination.


```sql
SELECT
key,
value
FROM azure.ad_hybrid_health_service.services_metrics_averages
WHERE groupName = '{{ groupName }}'
AND metricName = '{{ metricName }}'
AND serviceName = '{{ serviceName }}';
```