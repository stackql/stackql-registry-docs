---
title: offline_collectors
hide_title: false
hide_table_of_contents: false
keywords:
  - offline_collectors
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>offline_collectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.collectors.offline_collectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Identifier |
| `name` | `string` | Name of the Collector. It must be unique on your account. |
| `description` | `string` | Description of the Collector. |
| `targetCpu` | `integer` | When CPU utilization exceeds this threshold, the Collector will slow down its rate of ingestion to lower its CPU utilization. |
| `collectorVersion` | `string` | Version of the Collector software installed. |
| `sourceSyncMode` | `string` | For installed Collectors, whether the Collector is using local source configuration management (using a JSON file), or cloud management (using the UI) |
| `ephemeral` | `boolean` | When true, the collector will be deleted after 12 hours of inactivity. For more information, see Setting a Collector as Ephemeral. |
| `cutoffRelativeTime` | `string` | Can be specified instead of cutoffTimestamp to provide a relative offset with respect to the current time. Example: use "-1h", "-1d", or "-1w" to collect data thats less than one hour, one day, or one week old, respectively. |
| `osVersion` | `string` | Version of the OS that Collector is installed on. [Installed Collectors only] |
| `cutoffTimestamp` | `integer` | 0 (collects all data)\|Only collect data from files with a modified date more recent than this timestamp, specified as milliseconds since epoch |
| `timeZone` | `string` | Time zone of the Collector. For a list of possible values, refer to the "TZ" column in this Wikipedia article. |
| `alive` | `boolean` | When a Collector is running it sends Sumo a heartbeat message every 15 seconds. If no heartbeat message is received after 30 minutes this becomes false. |
| `osTime` | `integer` | Time that the Collector has been running, in milliseconds. [Installed Collectors only] |
| `hostName` | `string` | Host name of the Collector. The hostname can be a maximum of 128 characters. |
| `collectorType` | `string` | The Collector type: Installable or Hosted |
| `osArch` | `string` | Architecture of the OS that Collector is installed on. [Installed Collectors only] |
| `links` | `array` |  |
| `category` | `string` | The Category of the Collector, used as metadata when searching data. |
| `osName` | `string` | Name of OS that Collector is installed on. [Installed Collectors only] |
| `lastSeenAlive` | `integer` | The last time the Sumo Logic service received an active heartbeat from the Collector, specified as milliseconds since epoch. |
| `fields` | `object` | JSON map of key-value fields (metadata) to apply to the Collector. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_offline_collectors` | `SELECT` | `region` |
