---
title: managed_connector_plugins
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_connector_plugins
  - connect
  - confluent
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage confluent resources using SQL
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>managed_connector_plugins</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_connector_plugins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.connect.managed_connector_plugins" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="class" /> | `string` | The connector class name. E.g. BigQuerySink. |
| <CopyableCode code="type" /> | `string` | Type of connector, sink or source. |
| <CopyableCode code="version" /> | `string` | The version string for the connector available. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_connectv1connector_plugins" /> | `SELECT` | <CopyableCode code="environment_id, kafka_cluster_id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Return a list of Managed Connector plugins installed in the Kafka Connect cluster. |
| <CopyableCode code="validate_connectv1connector_plugin" /> | `EXEC` | <CopyableCode code="environment_id, kafka_cluster_id, plugin_name" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Validate the provided configuration values against the configuration definition. This API performs per config validation and returns suggested values and validation error messages. |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Return a list of Managed Connector plugins installed in the Kafka Connect cluster.


```sql
SELECT
class,
type,
version
FROM confluent.connect.managed_connector_plugins
WHERE environment_id = '{{ environment_id }}'
AND kafka_cluster_id = '{{ kafka_cluster_id }}';
```