---
title: cluster_links
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_links
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
<tr><td><b>Name</b></td><td><code>cluster_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.cluster_links" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="cluster_link_id" /> | `string` |
| <CopyableCode code="destination_cluster_id" /> | `string` |
| <CopyableCode code="kind" /> | `string` |
| <CopyableCode code="link_error" /> | `string` |
| <CopyableCode code="link_error_message" /> | `string` |
| <CopyableCode code="link_id" /> | `string` |
| <CopyableCode code="link_name" /> | `string` |
| <CopyableCode code="link_state" /> | `string` |
| <CopyableCode code="metadata" /> | `object` |
| <CopyableCode code="remote_cluster_id" /> | `string` |
| <CopyableCode code="source_cluster_id" /> | `string` |
| <CopyableCode code="tasks" /> | `array` |
| <CopyableCode code="topic_names" /> | `array` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_kafka_link" /> | `SELECT` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />``link_id`` in ``ListLinksResponseData`` is deprecated and may be removed in a future release. Use the new ``cluster_link_id`` instead. |
| <CopyableCode code="list_kafka_links" /> | `SELECT` | <CopyableCode code="cluster_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />``link_id`` in ``ListLinksResponseData`` is deprecated and may be removed in a future release. Use the new ``cluster_link_id`` instead. |
| <CopyableCode code="create_kafka_link" /> | `INSERT` | <CopyableCode code="cluster_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Cluster link creation requires source cluster security configurations in<br />the configs JSON section of the data request payload. |
| <CopyableCode code="delete_kafka_link" /> | `DELETE` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |
