---
title: consumers_lags
hide_title: false
hide_table_of_contents: false
keywords:
  - consumers_lags
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
<tr><td><b>Name</b></td><td><code>consumers_lags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.consumers_lags" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_kafka_consumer_lag" /> | `EXEC` | <CopyableCode code="cluster_id, consumer_group_id, partition_id, topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Available in dedicated clusters only](https://img.shields.io/badge/-Available%20in%20dedicated%20clusters%20only-%23bc8540)](https://docs.confluent.io/cloud/current/clusters/cluster-types.html#dedicated-cluster)<br /><br />Return the consumer lag on a partition with the given `partition_id`. |
| <CopyableCode code="list_kafka_consumer_lags" /> | `EXEC` | <CopyableCode code="cluster_id, consumer_group_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Available in dedicated clusters only](https://img.shields.io/badge/-Available%20in%20dedicated%20clusters%20only-%23bc8540)](https://docs.confluent.io/cloud/current/clusters/cluster-types.html#dedicated-cluster)<br /><br />Return a list of consumer lags of the consumers belonging to the<br />specified consumer group. |
