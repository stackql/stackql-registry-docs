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
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_or_update_connectv1connector_config" /> | `INSERT` | <CopyableCode code="connector_name, environment_id, kafka_cluster_id, data__connector.class, data__kafka.api.key, data__kafka.api.secret, data__name" /> | Create a new connector using the given configuration, or update the configuration for an existing connector. Returns information about the connector after the change has been made. |
| <CopyableCode code="get_connectv1connector_config" /> | `EXEC` | <CopyableCode code="connector_name, environment_id, kafka_cluster_id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Get the configuration for the connector. |
