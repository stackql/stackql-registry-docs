---
title: services_feature_availibilities
hide_title: false
hide_table_of_contents: false
keywords:
  - services_feature_availibilities
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

Creates, updates, deletes, gets or lists a <code>services_feature_availibilities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services_feature_availibilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.services_feature_availibilities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="value" /> | `boolean` | The value. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="featureName, serviceName" /> | Checks if the service has all the pre-requisites met to use a feature. |

## `SELECT` examples

Checks if the service has all the pre-requisites met to use a feature.


```sql
SELECT
value
FROM azure.ad_hybrid_health_service.services_feature_availibilities
WHERE featureName = '{{ featureName }}'
AND serviceName = '{{ serviceName }}';
```