---
title: connector_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_tasks
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

Creates, updates, deletes, gets or lists a <code>connector_tasks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connector_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.connect.connector_tasks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `object` | The ID of task. |
| <CopyableCode code="config" /> | `object` | Configuration parameters for the connector. These configurations
are the minimum set of key-value pairs (KVP) which can be used to
define how the connector connects Kafka to the external system.
Some of these KVPs are common to all the connectors, such as
connection parameters to Kafka, connector metadata, etc. The list
of common connector configurations is as follows

  - cloud.environment
  - cloud.provider
  - connector.class
  - kafka.api.key
  - kafka.api.secret
  - kafka.endpoint
  - kafka.region
  - name

A specific connector such as `GcsSink` would have additional
parameters such as `gcs.bucket.name`, `flush.size`, etc. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_connectv1connector_tasks" /> | `SELECT` | <CopyableCode code="connector_name, environment_id, kafka_cluster_id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Get a list of tasks currently running for the connector. |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Get a list of tasks currently running for the connector.


```sql
SELECT
id,
config
FROM confluent.connect.connector_tasks
WHERE connector_name = '{{ connector_name }}'
AND environment_id = '{{ environment_id }}'
AND kafka_cluster_id = '{{ kafka_cluster_id }}';
```