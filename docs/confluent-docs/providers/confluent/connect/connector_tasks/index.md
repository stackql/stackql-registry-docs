---
title: connector_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_tasks
  - connect
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
<tr><td><b>Name</b></td><td><code>connector_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.connect.connector_tasks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `object` | The ID of task. |
| <CopyableCode code="config" /> | `object` | Configuration parameters for the connector. These configurations<br />are the minimum set of key-value pairs (KVP) which can be used to<br />define how the connector connects Kafka to the external system.<br />Some of these KVPs are common to all the connectors, such as<br />connection parameters to Kafka, connector metadata, etc. The list<br />of common connector configurations is as follows<br /><br />  - cloud.environment<br />  - cloud.provider<br />  - connector.class<br />  - kafka.api.key<br />  - kafka.api.secret<br />  - kafka.endpoint<br />  - kafka.region<br />  - name<br /><br />A specific connector such as `GcsSink` would have additional<br />parameters such as `gcs.bucket.name`, `flush.size`, etc. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_connectv1connector_tasks" /> | `SELECT` | <CopyableCode code="connector_name, environment_id, kafka_cluster_id" /> |
