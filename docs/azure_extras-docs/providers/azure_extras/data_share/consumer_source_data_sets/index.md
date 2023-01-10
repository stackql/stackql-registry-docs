---
title: consumer_source_data_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - consumer_source_data_sets
  - data_share
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
<tr><td><b>Name</b></td><td><code>consumer_source_data_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.data_share.consumer_source_data_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id of the azure resource |
| `name` | `string` | Name of the azure resource |
| `type` | `string` | Type of the azure resource |
| `properties` | `object` | Properties of consumer source dataSet |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ConsumerSourceDataSets_ListByShareSubscription` | `SELECT` | `accountName, api-version, resourceGroupName, shareSubscriptionName, subscriptionId` |
