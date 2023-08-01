---
title: subscriber_usage_aggregates
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriber_usage_aggregates
  - commerce_admin
  - azure_extras    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriber_usage_aggregates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.commerce_admin.subscriber_usage_aggregates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Location where resource is location. |
| `properties` | `object` | Properties for aggregate usage. |
| `tags` | `object` | List of key-value pairs. |
| `type` | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `SubscriberUsageAggregates_List` | `SELECT` | `reportedEndTime, reportedStartTime, subscriptionId` |
