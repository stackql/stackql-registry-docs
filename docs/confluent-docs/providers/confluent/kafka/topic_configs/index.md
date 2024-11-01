---
title: topic_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - topic_configs
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
<tr><td><b>Name</b></td><td><code>topic_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.topic_configs" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete_kafka_topic_config" /> | `DELETE` | <CopyableCode code="cluster_id, name, topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Reset the configuration parameter with given `name` to its default value. |
| <CopyableCode code="update_kafka_topic_config_batch" /> | `UPDATE` | <CopyableCode code="cluster_id, topic_name, data__data" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Update or delete a set of topic configuration parameters.<br />Also supports a dry-run mode that only validates whether the operation would succeed if the<br />``validate_only`` request property is explicitly specified and set to true. |
| <CopyableCode code="get_kafka_topic_config" /> | `EXEC` | <CopyableCode code="cluster_id, name, topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Return the configuration parameter with the given `name`. |
| <CopyableCode code="list_kafka_all_topic_configs" /> | `EXEC` | <CopyableCode code="cluster_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Return the list of configuration parameters for all topics hosted by the specified<br />cluster. |
| <CopyableCode code="list_kafka_topic_configs" /> | `EXEC` | <CopyableCode code="cluster_id, topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Return the list of configuration parameters that belong to the specified topic. |
| <CopyableCode code="update_kafka_topic_config" /> | `EXEC` | <CopyableCode code="cluster_id, name, topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Update the configuration parameter with given `name`. |
