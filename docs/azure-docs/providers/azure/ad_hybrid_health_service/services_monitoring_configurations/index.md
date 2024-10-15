---
title: services_monitoring_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - services_monitoring_configurations
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

Creates, updates, deletes, gets or lists a <code>services_monitoring_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services_monitoring_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.services_monitoring_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="key" /> | `string` | The key for the property. |
| <CopyableCode code="value" /> | `string` | The value for the key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceName" /> | Gets the service level monitoring configurations. |

## `SELECT` examples

Gets the service level monitoring configurations.


```sql
SELECT
key,
value
FROM azure.ad_hybrid_health_service.services_monitoring_configurations
WHERE serviceName = '{{ serviceName }}';
```