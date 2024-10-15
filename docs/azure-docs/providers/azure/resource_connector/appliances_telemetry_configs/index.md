---
title: appliances_telemetry_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - appliances_telemetry_configs
  - resource_connector
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

Creates, updates, deletes, gets or lists a <code>appliances_telemetry_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>appliances_telemetry_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_connector.appliances_telemetry_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="telemetryInstrumentationKey" /> | `string` | Telemetry instrumentation key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the telemetry config. |

## `SELECT` examples

Gets the telemetry config.


```sql
SELECT
telemetryInstrumentationKey
FROM azure.resource_connector.appliances_telemetry_configs
WHERE subscriptionId = '{{ subscriptionId }}';
```