---
title: offers
hide_title: false
hide_table_of_contents: false
keywords:
  - offers
  - subscriptions_admin
  - azure    
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
<tr><td><b>Name</b></td><td><code>offers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.subscriptions_admin.offers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `properties` | `object` | Represents an offering of services against which a subscription can be created. |
| `tags` | `object` | List of key-value pairs. |
| `type` | `string` | Type of resource. |
| `location` | `string` | Location of the resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Offers_Get` | `SELECT` | `offer, resourceGroupName, subscriptionId` | Get the specified offer. |
| `Offers_List` | `SELECT` | `resourceGroupName, subscriptionId` | Get the list of offers under a resource group. |
| `Offers_ListAll` | `SELECT` | `subscriptionId` | Get the list of offers. |
| `Offers_CreateOrUpdate` | `INSERT` | `offer, resourceGroupName, subscriptionId` | Create or update the offer. |
| `Offers_Delete` | `DELETE` | `offer, resourceGroupName, subscriptionId` | Delete the specified offer. |
| `Offers_Link` | `EXEC` | `offer, resourceGroupName, subscriptionId` | Links a plan to an offer. |
| `Offers_ListMetricDefinitions` | `EXEC` | `offer, resourceGroupName, subscriptionId` | Get the metric definitions. |
| `Offers_ListMetrics` | `EXEC` | `offer, resourceGroupName, subscriptionId` | Get the offer metrics. |
| `Offers_Unlink` | `EXEC` | `offer, resourceGroupName, subscriptionId` | Unlink a plan from an offer. |
