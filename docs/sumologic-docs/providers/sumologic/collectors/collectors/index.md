---
title: collectors
hide_title: false
hide_table_of_contents: false
keywords:
  - collectors
  - collectors
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>collectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.collectors.collectors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | Identifier |
| <CopyableCode code="name" /> | `string` | Name of the Collector. It must be unique on your account. |
| <CopyableCode code="description" /> | `string` | Description of the Collector. |
| <CopyableCode code="alive" /> | `boolean` | When a Collector is running it sends Sumo a heartbeat message every 15 seconds. If no heartbeat message is received after 30 minutes this becomes false. |
| <CopyableCode code="category" /> | `string` | The Category of the Collector, used as metadata when searching data. |
| <CopyableCode code="collectorType" /> | `string` | The Collector type: Installable or Hosted |
| <CopyableCode code="collectorVersion" /> | `string` | Version of the Collector software installed. |
| <CopyableCode code="cutoffRelativeTime" /> | `string` | Can be specified instead of cutoffTimestamp to provide a relative offset with respect to the current time. Example: use "-1h", "-1d", or "-1w" to collect data thats less than one hour, one day, or one week old, respectively. |
| <CopyableCode code="cutoffTimestamp" /> | `integer` | 0 (collects all data)\|Only collect data from files with a modified date more recent than this timestamp, specified as milliseconds since epoch |
| <CopyableCode code="ephemeral" /> | `boolean` | When true, the collector will be deleted after 12 hours of inactivity. For more information, see Setting a Collector as Ephemeral. |
| <CopyableCode code="fields" /> | `object` | JSON map of key-value fields (metadata) to apply to the Collector. |
| <CopyableCode code="hostName" /> | `string` | Host name of the Collector. The hostname can be a maximum of 128 characters. |
| <CopyableCode code="lastSeenAlive" /> | `integer` | The last time the Sumo Logic service received an active heartbeat from the Collector, specified as milliseconds since epoch. |
| <CopyableCode code="links" /> | `array` |  |
| <CopyableCode code="osArch" /> | `string` | Architecture of the OS that Collector is installed on. [Installed Collectors only] |
| <CopyableCode code="osName" /> | `string` | Name of OS that Collector is installed on. [Installed Collectors only] |
| <CopyableCode code="osTime" /> | `integer` | Time that the Collector has been running, in milliseconds. [Installed Collectors only] |
| <CopyableCode code="osVersion" /> | `string` | Version of the OS that Collector is installed on. [Installed Collectors only] |
| <CopyableCode code="sourceSyncMode" /> | `string` | For installed Collectors, whether the Collector is using local source configuration management (using a JSON file), or cloud management (using the UI) |
| <CopyableCode code="targetCpu" /> | `integer` | When CPU utilization exceeds this threshold, the Collector will slow down its rate of ingestion to lower its CPU utilization. |
| <CopyableCode code="timeZone" /> | `string` | Time zone of the Collector. For a list of possible values, refer to the "TZ" column in this Wikipedia article. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_collector_by_name" /> | `SELECT` | <CopyableCode code="name, region" /> | Get the Collector with the specified name. |
| <CopyableCode code="list_collectors" /> | `SELECT` | <CopyableCode code="region" /> | Get a list of Collectors with an optional limit and offset. |
| <CopyableCode code="create_collector" /> | `INSERT` | <CopyableCode code="region" /> | Create Hosted Collector.  This method can only be used to create Hosted Collectors. You must install a Collector manually to create an Installed Collector. |
| <CopyableCode code="delete_collector" /> | `DELETE` | <CopyableCode code="id, region" /> | Delete Collector by ID |
| <CopyableCode code="get_collector_by_id" /> | `EXEC` | <CopyableCode code="id, region" /> | Get the Collector with the specified Identifier. |
| <CopyableCode code="update_collector" /> | `EXEC` | <CopyableCode code="id, region" /> | Update a Collector |
