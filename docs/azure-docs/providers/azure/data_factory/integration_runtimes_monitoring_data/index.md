---
title: integration_runtimes_monitoring_data
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtimes_monitoring_data
  - data_factory
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

Creates, updates, deletes, gets or lists a <code>integration_runtimes_monitoring_data</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_runtimes_monitoring_data</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.integration_runtimes_monitoring_data" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Integration runtime name. |
| <CopyableCode code="nodes" /> | `array` | Integration runtime node monitoring data. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="factoryName, integrationRuntimeName, resourceGroupName, subscriptionId" /> | Get the integration runtime monitoring data, which includes the monitor data for all the nodes under this integration runtime. |

## `SELECT` examples

Get the integration runtime monitoring data, which includes the monitor data for all the nodes under this integration runtime.


```sql
SELECT
name,
nodes
FROM azure.data_factory.integration_runtimes_monitoring_data
WHERE factoryName = '{{ factoryName }}'
AND integrationRuntimeName = '{{ integrationRuntimeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```