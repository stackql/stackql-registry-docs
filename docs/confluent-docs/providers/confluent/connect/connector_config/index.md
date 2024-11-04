---
title: connector_config
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_config
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
<tr><td><b>Name</b></td><td><code>connector_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.connect.connector_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name or alias of the class (plugin) for this connector. For Custom Connector, it must be the same as connector_name. |
| <CopyableCode code="cloud.environment" /> | `string` | The cloud environment type. |
| <CopyableCode code="cloud.provider" /> | `string` | The cloud service provider, e.g. aws, azure, etc. |
| <CopyableCode code="connector.class" /> | `string` | The connector class name. E.g. BigQuerySink, GcsSink, etc. |
| <CopyableCode code="kafka.api.key" /> | `string` | The kafka cluster api key. |
| <CopyableCode code="kafka.api.secret" /> | `string` | The kafka cluster api secret key. |
| <CopyableCode code="kafka.endpoint" /> | `string` | The kafka cluster endpoint. |
| <CopyableCode code="kafka.region" /> | `string` | The kafka cluster region. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_connectv1connector_config" /> | `SELECT` | <CopyableCode code="connector_name, environment_id, kafka_cluster_id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Get the configuration for the connector. |
| <CopyableCode code="create_or_update_connectv1connector_config" /> | `INSERT` | <CopyableCode code="connector_name, environment_id, kafka_cluster_id, data__connector.class, data__kafka.api.key, data__kafka.api.secret, data__name" /> | Create a new connector using the given configuration, or update the configuration for an existing connector. Returns information about the connector after the change has been made. |
