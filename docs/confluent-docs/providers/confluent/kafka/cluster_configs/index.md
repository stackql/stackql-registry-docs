---
title: cluster_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_configs
  - kafka
  - confluent    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Confluent Cloud resources using SQL.
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.cluster_configs" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete_kafka_cluster_config" /> | `DELETE` | <CopyableCode code="cluster_id, name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Reset the configuration parameter specified by ``name`` to its<br />default value by deleting a dynamic cluster-wide configuration. |
| <CopyableCode code="update_kafka_cluster_configs" /> | `UPDATE` | <CopyableCode code="cluster_id, data__data" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Update or delete a set of dynamic cluster-wide broker configuration parameters. |
| <CopyableCode code="get_kafka_cluster_config" /> | `EXEC` | <CopyableCode code="cluster_id, name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Return the dynamic cluster-wide broker configuration parameter specified by ``name``. |
| <CopyableCode code="list_kafka_cluster_configs" /> | `EXEC` | <CopyableCode code="cluster_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Return a list of dynamic cluster-wide broker configuration parameters for the specified Kafka<br />cluster. Returns an empty list if there are no dynamic cluster-wide broker configuration parameters. |
| <CopyableCode code="update_kafka_cluster_config" /> | `EXEC` | <CopyableCode code="cluster_id, name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Update the dynamic cluster-wide broker configuration parameter specified by ``name``. |
