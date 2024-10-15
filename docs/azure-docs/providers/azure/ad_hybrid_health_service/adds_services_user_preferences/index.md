---
title: adds_services_user_preferences
hide_title: false
hide_table_of_contents: false
keywords:
  - adds_services_user_preferences
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

Creates, updates, deletes, gets or lists a <code>adds_services_user_preferences</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>adds_services_user_preferences</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.adds_services_user_preferences" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="metricNames" /> | `array` | The name of the metric. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="featureName, serviceName" /> | Gets the user preferences for a given feature. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="featureName, serviceName" /> | Deletes the user preferences for a given feature. |
| <CopyableCode code="add" /> | `EXEC` | <CopyableCode code="featureName, serviceName" /> | Adds the user preferences for a given feature. |

## `SELECT` examples

Gets the user preferences for a given feature.


```sql
SELECT
metricNames
FROM azure.ad_hybrid_health_service.adds_services_user_preferences
WHERE featureName = '{{ featureName }}'
AND serviceName = '{{ serviceName }}';
```
## `DELETE` example

Deletes the specified <code>adds_services_user_preferences</code> resource.

```sql
/*+ delete */
DELETE FROM azure.ad_hybrid_health_service.adds_services_user_preferences
WHERE featureName = '{{ featureName }}'
AND serviceName = '{{ serviceName }}';
```
