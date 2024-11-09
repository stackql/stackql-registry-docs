---
title: connector_offsets
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_offsets
  - connect
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>connector_offsets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connector_offsets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.connect.connector_offsets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the connector. |
| <CopyableCode code="name" /> | `string` | The name of the connector. |
| <CopyableCode code="metadata" /> | `object` | Metadata of the connector offset. |
| <CopyableCode code="offsets" /> | `array` | Array of offsets which are categorised into partitions. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_connectv1connector_offsets" /> | `SELECT` | <CopyableCode code="connector_name, environment_id, kafka_cluster_id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Get the current offsets for the connector. The offsets provide information on the point in the source system, 
from which the connector is pulling in data. The offsets of a connector are continuously observed periodically and are queryable via this API. |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Get the current offsets for the connector. The offsets provide information on the point in the source system, 
from which the connector is pulling in data. The offsets of a connector are continuously observed periodically and are queryable via this API.


```sql
SELECT
id,
name,
metadata,
offsets
FROM confluent.connect.connector_offsets
WHERE connector_name = '{{ connector_name }}'
AND environment_id = '{{ environment_id }}'
AND kafka_cluster_id = '{{ kafka_cluster_id }}';
```